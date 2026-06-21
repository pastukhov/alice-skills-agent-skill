---
metadata:
  - name: generator
    content: Diplodoc Platform v5.39.1
alternate:
  - https://yandex.ru/dev/dialogs/alice/doc/ru/resource-upload.md
---
# Изображения

{% include notitle [neuroexpert-button](_includes/reusables/neuroexpert-button-99270fdba323.md) %}


{% note alert %}

Ограничения на загрузку изображений:
- Для одного аккаунта Яндекса можно загрузить не больше 100 МБ изображений.
- Каждый файл должен быть размером не менее 1 КБ и не более 1 МБ.
- Поддерживаются форматы PNG, JPEG, GIF, BMP, TIFF, WEBP.

При превышении лимита запросов на удаление или на загрузку вернется ответ со статусом 429.

{% endnote %}


Ваш навык может отвечать пользователю картинками. Устраивайте экскурсии по музеям, показывая
 произведения великих мастеров. Рассказывайте о кулинарных рецептах, сопровождая текст
 изображениями блюд. Загружайте фотографии вашего города — и ваш навык станет гидом для
 пользователей.

Чтобы показать изображение в ответе навыка:

1. [Подготовьте изображение](#preparation), чтобы оно корректно отображалось в навыке (например, чтобы не обрезались края).
1. Загрузите изображение на Яндекс Диалоги в [консоли разработчика](#console-images-load) или через [HTTP API](#http-images-load).
1. Добавьте ссылку на загруженное изображение в ответ навыка. При необходимости можно показать галерею из нескольких изображений. Подробнее см. в разделе [Протокол работы](https://yandex.ru/dev/dialogs/alice/doc/ru/response.md#card).


## Подготовка изображения {#preparation}

Чтобы картинка корректно отображалась в навыке (например, чтобы не обрезались ее края), ее следует предварительно обработать. Рекомендации по обработке изображений приведены в видеоуроке.

<div style="
    border:1px solid #d1d5db;
    border-radius:20px;
    overflow:hidden;
    max-width:100%;
">
  <iframe src="https://runtime.strm.yandex.ru/player/video/vplv7gjtj4mz5yyed6vs?autoplay=0&mute=0"
    frameborder="0"
    allowfullscreen
    style="
      display:block;
      width:100%;
      height:360px;
      "></iframe>
</div>

## Загрузка изображения через консоль разработчика {#console-images-load}

1. Зайдите в [консоль разработчика](https://dialogs.yandex.ru/developer/) и откройте страницу навыка.
1. Перейдите в раздел **Ресурсы**. В разделе показан список всех ресурсов, загруженных для навыка (картинки, звуки). Ресурсы, которые загружались через [HTTP API](#http-images-load), также будут отображаться в этом разделе.
1. Откройте вкладку **Изображения** и переместите в окошко нужный файл с вашего компьютера. Когда изображение будет загружено в Диалоги, оно появится в этой вкладке.
1. Чтобы показать изображение в навыке, сформируйте ответ согласно [протоколу](https://yandex.ru/dev/dialogs/alice/doc/ru/response.md).


## Загрузка изображения через HTTP API {#http-images-load}

Для одноразового использования картинку нужно загружать в ресурсы через API.

Например, в навыке картинка создается в реальном времени, затем по HTTP API она загружается на платформу Диалогов и сразу же используется для вывода в навыке. О том, как загрузить картинки в свой навык через API, смотрите в видеоуроке.

<div style="
    border:1px solid #d1d5db;
    border-radius:20px;
    overflow:hidden;
    max-width:100%;
">
  <iframe src="https://runtime.strm.yandex.ru/player/video/vplvmhgwrwkj54wdhcry?autoplay=0&mute=0"
    frameborder="0"
    allowfullscreen
    style="
      display:block;
      width:100%;
      height:360px;
      "></iframe>
</div>

### Авторизация {#auth}

Загружать картинки для навыка можно только от имени пользователя, создавшего навык. Для этого получите [OAuth-токен для Диалогов](https://oauth.yandex.ru/authorize?response_type=token&client_id=c473ca268cd749d3a8371351a8f2bcbd). Полученный токен необходимо указывать в каждом запросе к Диалогам, в заголовке
 `Authorization`:

```http
Authorization: OAuth ARAAAAAB5vpbAAQ7o9abBlrUn0nshvcHZE4Irhw
```

### Проверить занятое место {#quota}

Для каждого аккаунта Яндекса на Диалоги можно загрузить не больше 100 МБ картинок. Чтобы
 узнать, сколько места уже занято, отправьте следующий запрос:

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

Диалоги пришлют ответ с данными о доступном и израсходованном объемах для картинок и [аудиофайлов](https://yandex.ru/dev/dialogs/alice/doc/ru/resource-sounds-upload.md). Значения указаны в байтах.

```json
{
    "images": {
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

Лимиты на загрузку картинок и аудиофайлов считаются отдельно.

### Загрузить изображение из интернета {#download-internet}

Чтобы загрузить картинку для навыка из интернета, передайте URL картинки в запросе:

```http
POST /api/v1/skills/<идентификатор навыка>/images

Host: https://dialogs.yandex.net
Authorization: OAuth <OAuth-токен>
Content-Type: application/json

{ "url": "<адрес изображения>" }
```

{% cut "curl" %}

```http
curl \
  -H 'Authorization: OAuth <OAuth-токен>' \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{ "url": "<адрес изображения>" }' \
  'https://dialogs.yandex.net/api/v1/skills/<идентификатор навыка>/images'
```

{% endcut %}

Идентификатор навыка можно посмотреть в [консоли разработчика](https://dialogs.yandex.ru/developer/) — зайдите на страницу навыка, откройте вкладку **Общие сведения** и пролистайте вниз.

Если изображение удалось загрузить на Диалоги, в ответ придет информация об этом
 изображении:

```json
{
  "image": {
    "id": <идентификатор изображения>,
    "origUrl": <URL изображения>,
    "size": <размер изображения>,
    "createdAt": <дата загрузки>
  }
}
```

[Как показать изображение в ответе навыка](https://yandex.ru/dev/dialogs/alice/doc/ru/response.md#card)

### Загрузить файл изображения {#upload-file}

Чтобы загрузить файл, отправьте запрос:

```http
POST /api/v1/skills/<идентификатор навыка>/images

Host: https://dialogs.yandex.net
Authorization: OAuth <OAuth-токен>
Content-Type: multipart/form-data

<содержимое файла>
```

{% cut "curl" %}

```http
curl \
  -H 'Authorization: OAuth <OAuth-токен>' \
  -H 'Content-Type: multipart/form-data' \
  -X POST \
  -F file=@<путь к файлу> \
  'https://dialogs.yandex.net/api/v1/skills/<идентификатор навыка>/images'
```

{% endcut %}

Если Диалоги успешно получили картинку, в ответе придет информация об изображении:

```json
{
  "image": {
    "id": <идентификатор изображения>,
    "origUrl": <URL изображения>,
    "size": <размер изображения>,
    "createdAt": <дата загрузки>
  }
}
```

[Как показать изображение в ответе навыка](https://yandex.ru/dev/dialogs/alice/doc/ru/response.md#card)

### Получить список загруженных изображений {#list}

Список изображений, загруженных для навыка, можно получить следующим запросом:

```http
GET /api/v1/skills/<идентификатор навыка>/images

Host: https://dialogs.yandex.net
Authorization: OAuth <OAuth-токен>
```

{% cut "curl" %}

```http
curl \
  -H 'Authorization: OAuth <OAuth-токен>' \
  'https://dialogs.yandex.net/api/v1/skills/<идентификатор навыка>/images'
```

{% endcut %}

Диалоги возвращают список изображений, загруженных для навыка:

```json
{
  "images": [
    {
      "id": <идентификатор изображения>,
      "origUrl": <URL изображения>,
      "size": <размер изображения>,
      "createdAt": <дата загрузки>
    },
    ...
  ],
  "total": <количество загруженных изображений>
} 
```

### Удалить изображение {#delete}

Чтобы удалить загруженное изображение, отправьте его идентификатор в запросе DELETE:

```http
DELETE /api/v1/skills/<идентификатор навыка>/images/<идентификатор изображения>

Host: https://dialogs.yandex.net
Authorization: OAuth <OAuth-токен>
```

{% cut "curl" %}

```http
curl \
  -H 'Authorization: OAuth <OAuth-токен>' \
  -X DELETE \
  'https://dialogs.yandex.net/api/v1/skills/<идентификатор навыка>/images/<идентификатор изображения>'
```

{% endcut %}

Если изображение указано верно и успешно удалено, Диалоги возвращают ответ:

```json
{
  "result": "ok"
} 
```


## Полезные видео {#useful-videos}

{% cut "Разработка прототипа голосового приложения (с 34:28)" %}

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

{% include [index-support-button](_includes/index/id-index/support-button-6237cadbe735.md) %}


