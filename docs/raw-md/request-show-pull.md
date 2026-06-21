---
metadata:
  - name: generator
    content: Diplodoc Platform v5.39.1
alternate:
  - https://yandex.ru/dev/dialogs/alice/doc/ru/request-show-pull.md
---
# Show.Pull

{% include notitle [neuroexpert-button](_includes/reusables/neuroexpert-button-99270fdba323.md) %}


Навык получает запрос с типом `Show.Pull`, если пользователь произносит команду [запуска утреннего шоу Алисы](https://yandex.ru/support/station/skills/alice-show.html). Метаинформация о запросе содержит данные о сессии, тип поверхности запуска и идентификатор пользователя, что позволяет персонализировать историю от навыка.

Подробнее о запросе на чтение данных для шоу Алисы см. в разделе [Навыки в утреннем шоу Алисы](https://yandex.ru/dev/dialogs/alice/doc/ru/morning-show-protocol.md).

```json
{
    "body": {
        "meta": {
            "locale": "ru-RU",
            "timezone": "Europe/Moscow",
            "client_id": "none/none (none none; none none)",
            "interfaces": {}
        },
        "session": {
            "message_id": 0,
            "session_id": "<UUID>",
            "skill_id": "SKILL_ID",
            "user_id": "USER_ID",
            "new": true,
            "application": {
                "application_id": "<APP_ID>"
            }
        },
        "request": {
            "type": "Show.Pull",
            "show_type": "MORNING"
        },
        "version": "1.0"
    }
}
```

## request {#request}

Данные, полученные от пользователя.

#|
||
**Свойство**
|
**Описание** 
||
||
`type`
|
[string](*string)

Обязательное свойство.

Тип запроса. Возможные значения:

- `Show.Pull` — запрос на чтение данных для шоу.
||
||
`show_type`
|
[string](*string)

Обязательное свойство.

Тип шоу. Возможные значения:

- `MORNING` — утреннее шоу Алисы.
|| 
|#

{% include [index-support-button](_includes/index/id-index/support-button-bd1f7751f3e1.md) %}

[*string]: Cтрока, выделяется кавычками, например `"Hello world"`.
