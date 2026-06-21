---
metadata:
  - name: generator
    content: Diplodoc Platform v5.39.1
alternate:
  - https://yandex.ru/dev/dialogs/alice/doc/ru/resource-sounds-upload.md
---
# Собственное аудио

{% include notitle [neuroexpert-button](_includes/reusables/neuroexpert-button-99270fdba323.md) %}


Помимо звуков из [стандартной библиотеки](https://yandex.ru/dev/dialogs/alice/doc/ru/sounds.md), вы можете вставить в ответы навыка собственные звуки: песни, диалоги из фильмов или детские сказки. Создавайте навыки, например чтобы изучать иностранные языки или сольфеджио, прослушивать поэзию. Загрузите голоса известных дикторов для новостных навыков.

Чтобы воспроизвести свой звук в ответе навыка:
1. В [консоли разработчика](#console-sound-load) или через [HTTP API](#http-load) загрузите на Яндекс Диалоги аудиофайл.
    
    Ограничения:
    
    - Длительность файла: до 120 секунд. Треки длиннее 120 секунд будут автоматически обрезаны до 120 секунд.
    - Размер файла: до 5 МБ.
    - Формат: MP3, WAV или OGG.
    - Общий лимит: 1 ГБ.
    
1. Чтобы аудио воспроизводилось, в ответе навыка укажите поле `tts`:
    
    ```xml
    "tts": "<speaker audio='dialogs-upload/{идентификатор навыка}/{идентификатор аудиофайла}.opus'>"
    ```
    
    Идентификатор навыка можно посмотреть в [консоли разработчика](https://dialogs.yandex.ru/developer/): на странице навыка откройте вкладку **Общие сведения** и пролистайте вниз.
    
    Идентификатор аудиофайла станет известен, когда вы загрузите файл
 на Диалоги. Найдите идентификатор на странице навыка на вкладке
 **Ресурсы** или получите из ответа сервера, если вы загружали аудиофайл через [HTTP API](#http-load).


## Загрузка аудиофайла через консоль разработчика {#console-sound-load}

1. Зайдите в [консоль разработчика](https://dialogs.yandex.ru/developer/) и откройте страницу навыка.
1. Перейдите в раздел **Ресурсы**. В нем показан список всех ресурсов, загруженных для навыка (картинки и звуки), в том числе через [HTTP API](#http-load).
1. Откройте вкладку **Звуки** и переместите в окошко аудиофайл с компьютера. Когда файл загрузится, он появится на этой странице.
1. Чтобы аудиофайл воспроизводился, добавьте в ответ навыка поле `tts`. В
 поле укажите строку со ссылкой на аудио в
 Диалогах:

    ```
    "tts": "<speaker audio=\"dialogs-upload/[{идентификатор навыка}](*skill-id)/{[идентификатор аудиофайла](*audio-id)}.opus\">"
    ```
    Чтобы
 не набирать идентификаторы вручную, на странице
 ресурсов нажмите кнопку **Скопировать**:
    
    ![Копирование идентификатора аудиофайла на вкладке Звуки раздела Ресурсы в консоли разработчика](_images/copy-linkto-audio.png)
    
    Пример:
    
    ```html
    "tts": "<speaker audio=\"dialogs-upload/0c41c02e-29dd-49a1-a065-2ae8eb4aacfb/22f850f4-33d4-456a-8979-f875d2f43d54.opus\">"
    ```
    
    [Подробнее о формате ответа навыка](https://yandex.ru/dev/dialogs/alice/doc/ru/response.md)
    


## Загрузка аудиофайла через HTTP API {#http-load}

### Авторизоваться {#auth}

Загружать аудиофайлы может только пользователь Яндекса, который
 создал навык:

1. Получите [OAuth-токен для Диалогов](https://oauth.yandex.ru/authorize?response_type=token&client_id=c473ca268cd749d3a8371351a8f2bcbd).
1. Указывайте токен в каждом запросе к Диалогам в заголовке `Authorization`:

```http
Authorization: OAuth ARAAAAAB5vpbAAQ7o9abBlrUn0nshvcHZE4Irhw
```

### Проверить свободное место {#quota}

Лимит на загрузку аудиофайлов — 1 ГБ. Диалоги конвертируют загруженные аудиофайлы в формат OPUS и обрезают их до 120 секунд. В лимите учитывается размер сжатых файлов, а не оригиналов.

Чтобы узнать, сколько места занято, отправьте запрос:

```http
GET /api/v1/status

Host: https://dialogs.yandex.net
Authorization: OAuth <OAuth-токен>
```

{% cut "curl" %}

```http
curl \
  -H 'Authorization: OAuth <OAuth-токен>' \
  'https://dialogs.yandex.net/api/v1/status'
```

{% endcut %}

Диалоги пришлют доступный объем для аудиофайлов и [картинок](https://yandex.ru/dev/dialogs/alice/doc/ru/resource-upload.md), а также занятый объем.
 Значения указаны в байтах. Лимиты аудио и картинок считаются отдельно:

```json
{
    "_images": {
        "quota": {
            "total": 104857600,
            "used": 875963
        }
    },
    "sounds": {
        "quota": {
            "total": 1073741824,
            "used": 1593859
        }
    }
}
```

### Загрузить файл {#upload-file}

Выполните запрос:

```http
POST /api/v1/skills/[<идентификатор навыка>](*skill-id)/sounds

Host: https://dialogs.yandex.net
Authorization: OAuth <OAuth-токен>
Content-Type: multipart/form-data

Content-Disposition: form-data; name="file"; filename="<путь к файлу>"
```

{% cut "curl" %} 

```http
curl \
  -H 'Authorization: OAuth <OAuth-токен>' \
  -H 'Content-Type: multipart/form-data' \
  -X POST \
  -F file=@<путь к файлу> \
  'https://dialogs.yandex.net/api/v1/skills/<идентификатор навыка>/sounds'
```

{% endcut %}

Идентификатор навыка посмотрите в [консоли разработчика](https://dialogs.yandex.ru/developer/): на странице навыка откройте вкладку **Общие сведения** и пролистайте вниз.

Если Диалоги получили файл, в ответе придет информация о файле:

```json
{
  "sound": {
    "id": <идентификатор аудиофайла>,
    "skillId": <идентификатор навыка>,
    "size": <размер файла | null>,
    "originalName": <название загружаемого файла>,
    "createdAt": <дата создания файла>,
    "isProcessed": <флаг готовности файла>,
    "error": <текст ошибки | null>
  }
}
```

Аудиофайлы
 обрабатываются асинхронно. В ответ на запрос сервер вернет информацию
 о загружаемом файле, но для использования в навыке файл будет доступен позже (обычно через несколько секунд).

Статус аудиофайла отображается в поле `isProcessed`. Чтобы проверить
 готовность, отправьте
 GET-запрос:
```http
GET /api/v1/skills/<идентификатор навыка>/sounds/<идентификатор аудиофайла>

Host: https://dialogs.yandex.net
Authorization: OAuth <OAuth-токен>
```

{% cut "curl" %} 

```http
curl \
  -H 'Authorization: OAuth <OAuth-токен>' \
  'https://dialogs.yandex.net/api/v1/skills/<идентификатор навыка>/sounds/<идентификатор аудиофайла>'
```

{% endcut %}

Аудиофайл готов:
```json
{
  "sound": {
    "id": "842e667b-bdb3-4b84-a0ae-c13a1e0b6f20",
    "skillId": "c1701dba-85ab-4aaa-b7b1-8881588fddad",
    "size": 428738,
    "originalName": "dolphin-sound.mp3",
    "createdAt": "2019-06-18T12:07:42.013Z",
    "isProcessed": true,
    "error": null
  }
}
```

### Получить список загруженных файлов {#list}

Чтобы посмотреть аудиофайлы, загруженные для навыка, отправьте запрос:

```http
GET /api/v1/skills/<идентификатор навыка>/sounds

Host: https://dialogs.yandex.net
Authorization: OAuth <OAuth-токен>
```

{% cut "curl" %} 

```http
curl \
  -H 'Authorization: OAuth <OAuth-токен>' \
  'https://dialogs.yandex.net/api/v1/skills/<идентификатор навыка>/sounds'
```

{% endcut %}

В ответ Диалоги вернут список аудиофайлов:

```json
{
  "sounds": [
    {
      "id": "842e667b-bdb3-4b84-a0ae-c13a1e0b6f20",
      ...
    },
    {
      "id": ...
    }
  ],
  "total": 2
} 
```

### Удалить файл {#delete}

Чтобы удалить аудиофайл, отправьте его идентификатор в запросе DELETE:

```http
DELETE /api/v1/skills/<идентификатор навыка>/sounds/<идентификатор аудиофайла>

Host: https://dialogs.yandex.net
Authorization: OAuth <OAuth-токен>
```

{% cut "curl" %} 

```http
curl \
  -H 'Authorization: OAuth <OAuth-токен>' \
  -X DELETE \
  'https://dialogs.yandex.net/api/v1/skills/<идентификатор навыка>/sounds/<идентификатор аудиофайла>'
```

{% endcut %}

Если аудиофайл указан верно и был успешно удален, Диалоги вернут ответ:

```json
{
  "result": "ok"
} 
```


## Полезные видео {#useful-videos}

{% cut "Разработка прототипа голосового приложения (с 1:00:54)" %}

<div style="
    border:1px solid #d1d5db;
    border-radius:20px;
    overflow:hidden;
    max-width:100%;
">
  <iframe src="https://runtime.strm.yandex.ru/player/video/vplvba3haj2wbsimewde?autoplay=0&mute=0"
    frameborder="0"
    allowfullscreen
    style="
      display:block;
      width:100%;
      height:360px;
      "></iframe>
</div>

{% endcut %}

{% include [index-support-button](_includes/index/id-index/support-button-840537f1b291.md) %}


[*skill-id]: {% include notitle [skill-id](_includes/popups-b248aa5778b6.md#skill-id) %}

[*audio-id]: {% include notitle [audio-id](_includes/popups-b248aa5778b6.md#audio-id) %}
