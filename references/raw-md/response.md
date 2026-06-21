---
metadata:
  - name: generator
    content: Diplodoc Platform v5.39.1
alternate:
  - https://yandex.ru/dev/dialogs/alice/doc/ru/response.md
---
# Формат ответа

{% include notitle [neuroexpert-button](_includes/reusables/neuroexpert-button-99270fdba323.md) %}


{% include [restricts-response-time-limit](_includes/warehouse/concepts/id-restricts/response-time-limit-1235cb6cbdbe.md) %}


Обработчик навыка должен ответить на полученный от Яндекс Диалогов запрос согласно
 формату:

```json
{
  "response": {
    "text": "Здравствуйте! Это мы, хороводоведы.",
    "tts": "Здравствуйте! Это мы, хоров+одо в+еды.",
    "card": {
      "type": "...",
    },     
    "buttons": [
        {
            "title": "Надпись на кнопке",
            "payload": {},
            "url": "https://example.com/",
            "hide": true
        }
    ],
    "end_session": false,
    "directives": {}
  },
  "session_state": {
      "value": 10
  },
  "user_state_update": {
      "value": 42
  },
  "application_state": {
      "value": 37
  },
  "analytics": {
        "events": [
            {
                "name": "custom event"
            },
            {
                "name": "another custom event",
                "value": {
                    "field": "some value",
                    "second field": {
                        "third field": "custom value"
                    }
                }
            }
        ]
    },
  "version": "1.0"
}
```

## Содержимое тела ответа {#body-desc}

#|
||
**Свойство**
|
**Описание** 
||
||
[`response`](#response-desc)
|
[object](*object)

Обязательное свойство.

Данные для ответа пользователю.
||
||
`session_state`
|
[object](*object)

Объект, содержащий состояние навыка для хранения в контексте [сессии](https://yandex.ru/dev/dialogs/alice/doc/ru/session-persistence.md#store-session).
||
||
`user_state_update`
|
[object](*object)

Объект, содержащий состояние навыка для хранения в контексте [авторизованного пользователя](https://yandex.ru/dev/dialogs/alice/doc/ru/session-persistence.md#store-between-sessions).
||
||
`application_state`
|
[object](*object)

Объект, содержащий состояние навыка для хранения в контексте [экземпляра приложения пользователя](https://yandex.ru/dev/dialogs/alice/doc/ru/session-persistence.md#store-application).
||
||
[`analytics`](#analytics-desc)
|
[object](*object)

Объект с данными для аналитики.

Доступен навыкам с подключенным параметром **Настройки AppMetrica**. Подробнее см. в разделе  [AppMetrica](https://yandex.ru/dev/dialogs/alice/doc/ru/appmetrica.md).
||
||
`version`
|
[string](*string)

Обязательное свойство.

Версия протокола.

Текущая версия — 1.0.
||
|#

## response {#response-desc}

Данные для ответа пользователю.

#|
||
**Свойство**
|
**Описание** 
||
||
`text`
|
[string](*string)

Обязательное свойство.

Текст, который следует показать и озвучить пользователю.

Максимум 1024 символа. Может быть пустым (`text: ""`), если заполнено свойство `tts`.

Текст также используется, если у Алисы не получилось отобразить включенную в ответ
 карточку (свойство `response.card`). На устройствах, которые
 поддерживают только голосовое общение с навыком, это будет происходить каждый раз,
 когда навык присылает карточку в ответе.

В тексте ответа можно указать переводы строк последовательностью «\\n»,
 например: `"Отдых напрасен. Дорога крута.\nВечер прекрасен. Стучу в ворота."`
||
||
`tts`
|
[string](*string)

Ответ в формате TTS (text-to-speech).

Максимум 1024 символа.

Советы по использованию этого формата приведены в разделе [Настройка генерации речи](https://yandex.ru/dev/dialogs/alice/doc/ru/speech-tuning.md).

Вы также можете проигрывать звуки из [библиотеки Алисы](https://yandex.ru/dev/dialogs/alice/doc/ru/sounds.md) и [собственные звуки](https://yandex.ru/dev/dialogs/alice/doc/ru/resource-sounds-upload.md) (теги `<speaker>`, которые используются для ссылок
 на звуки, не учитываются в ограничении в 1024 символа на длину значения свойства
 `tts`). Фрагменты tts, собственные и библиотечные звуки можно указывать друг за другом в произвольном порядке и более одного раза каждый.
||
||
`card`
|
[object](*object)

Описание карточки — сообщения с поддержкой изображений.

Если приложению удается отобразить карточку для пользователя, свойство
 `response.text` не используется.

Содержимое зависит от типа карточки, указанного в поле `card.type`. Возможные значения:

- [`BigImage`](https://yandex.ru/dev/dialogs/alice/doc/ru/response-card-bigimage.md) — одно изображение.
- [`ItemsList`](https://yandex.ru/dev/dialogs/alice/doc/ru/response-card-itemslist.md) — список из нескольких изображений (от 1 до 5).
- [`ImageGallery`](https://yandex.ru/dev/dialogs/alice/doc/ru/response-card-imagegallery.md) — галерея из нескольких изображений (от 1 до 7).
||
||
[`buttons[]`](#buttons-desc)
|
[array](*array) of [objects](*object)

Кнопки, которые следует показать пользователю.

Все указанные кнопки выводятся после основного ответа Алисы, описанного в свойствах `response.text`
 и `response.card`.
 Кнопки можно использовать как релевантные ответу ссылки или подсказки для продолжения разговора.
||
||
`end_session`
|
[boolean](*boolean)

Обязательное свойство.

Признак конца разговора. Допустимые значения:

- `false` — сессию следует продолжить;
- `true` — сессию следует завершить.
||
||
`directives`
|
[object](*object)

Директивы.

Содержимое зависит от типа директивы.
 Возможное значение:

- `start_account_linking` — [запуск процесса авторизации в навыке](https://yandex.ru/dev/dialogs/alice/doc/ru/response-start-account-linking.md).
||
||
[`show_item_meta`](https://yandex.ru/dev/dialogs/alice/doc/ru/response-show-item-meta.md)
|
[object](*object)

Обязательный параметр только для сценария утреннего шоу.

Параметр историй утреннего шоу Алисы.
||
|#

## response.buttons {#buttons-desc}

Кнопки, которые следует показать пользователю. Все указанные кнопки выводятся после основного ответа Алисы, описанного в свойствах
 `response.text` и `response.card`.
 Кнопки можно использовать как релевантные ответу ссылки или подсказки для продолжения разговора.

[Посмотреть в интерфейсе](https://yandex.ru/dev/dialogs/alice/doc/ru/interface.md#tips)

#|
||
**Свойство**
|
**Описание** 
||
||
`title`
|
[string](*string)

Обязательное свойство для каждой кнопки.

Текст кнопки.

Максимум 64 символа.

Если для кнопки не указано свойство `url`,
 по нажатию текст кнопки будет отправлен навыку как реплика пользователя.
||
||
`url`
|
[string](*string)

URL, который должна открывать кнопка.

Максимум 1024 байта.

Если свойство `url` не указано, по нажатию кнопки навыку будет отправлен текст кнопки.
||
||
`payload`
|
[object](*object)

Произвольный JSON-объект, который Яндекс Диалоги должны отправить обработчику, если данная кнопка будет нажата.

Максимум 4096 байт.
||
||
`hide`
|
[boolean](*boolean)

Признак того, что кнопку нужно убрать после следующей реплики пользователя. Допустимые значения:

- `false` — кнопка должна оставаться активной (значение по умолчанию);
- `true` — кнопку нужно скрывать после нажатия.
||
|#

## analytics {#analytics-desc}

Объект с данными для аналитики.
 Доступен навыкам с подключенным параметром **Настройки AppMetrica**.
 Подробнее — в разделе о [подключении AppMetrica](https://yandex.ru/dev/dialogs/alice/doc/ru/appmetrica.md).

#|
||
**Свойство**
|
**Описание** 
||
||
[`events[]`](#events-desc)
|
[array](*array) of [objects](*object)

Массив событий.
||
|#


## analytics.events {#events-desc}

Массив событий.

#|
||
**Свойство**
|
**Описание** 
||
||
`name`
|
[string](*string)

Название события.
||
||
`value`
|
[objects](*object)

JSON-объект для многоуровневых событий. Допустимо не более пяти уровней вложенности события.

Многоуровневые события передаются через пары `key:value`.

Подробнее — в [документации AppMetrica](https://appmetrica.yandex.ru/docs/data-collection/about-events.html).
||
|#

{% include [index-support-button](_includes/index/id-index/support-button-e40d985839ad.md) %}

[*string]: Cтрока, выделяется кавычками, например `"Hello world"`.

[*number]: Целое или дробное число без кавычек, например `25.5`.

[*object]: Список пар `"ключ": значение`, разделенных запятой. Выделяется фигурными скобками `{}`.
```
{
  "name": "John",
  "surname": "Smith"
}
```

[*array]:
  Массив элементов, разделенных запятой. Элементом могут быть стандартные элементы JSON: строка, число, `true`, `false`, объект или массив. Массив выделяется квадратными скобками `[]`:
  
  ```"cities": ["Moscow", "Tokyo", "New York"] ```

[*boolean]: Логическое значение без кавычек: `true` (истина) или `false` (ложь).
