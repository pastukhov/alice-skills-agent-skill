---
metadata:
  - name: generator
    content: Diplodoc Platform v5.39.1
alternate:
  - https://yandex.ru/dev/dialogs/alice/doc/ru/request.md
---
# Формат запроса

{% include notitle [neuroexpert-button](_includes/reusables/neuroexpert-button-99270fdba323.md) %}


При каждом обращении к навыку Яндекс Диалоги отправляют POST-запрос на **Backend**, указанный при публикации.

```json
{
  "meta": {
    "locale": "ru-RU",
    "timezone": "Europe/Moscow",
    "client_id": "ru.yandex.searchplugin/7.16 (none none; android 4.4.2)",
    "interfaces": {
      "screen": {},
      "account_linking": {},
      "audio_player": {}
    }
  },
  "request": {
    "type": "...",
  },
  "session": {
    "message_id": 0,
    "session_id": "2eac4854-fce721f3-b845abba-20d60",
    "skill_id": "3ad36498-f5rd-4079-a14b-788652932056",
    "user_id": "47C73714B580ED2469056E71081159529FFC676A4E5B059D629A819E857DC2F8",
    "user": {
      "user_id": "6C91DA5198D1758C6A9F63A7C5CDDF09359F683B13A18A151FBF4C8B092BB0C2",
      "access_token": "AgAAAAAB4vpbAAApoR1oaCd5yR6eiXSHqOGT8dT"
    },
    "application": {
      "application_id": "47C73714B580ED2469056E71081159529FFC676A4E5B059D629A819E857DC2F8"
    },
    "new": true
  },
  "state": {
    "session": {
      "value": 10
    },
    "user": {
      "value": 42
    },
    "application": {
      "value": 37
    }
  },  
  "version": "1.0"
}
```

## Содержимое тела запроса {#body-desc}

#|
||**Свойство** |**Описание**||
||
[`meta`](#meta-desc)
|
[object](*object)

Информация об устройстве, с помощью которого пользователь разговаривает с Алисой.
||
||
[`request`](#request-desc)
|
[object](*object)

Данные, полученные от пользователя.

Содержимое зависит от типа ввода, указанного в поле `request.type`.
||
||
[`session`](#session-desc)
|
[object](*object)

Данные о сессии. Сессия — это период относительно непрерывного взаимодействия пользователя с навыком.

{% include [concepts-session](_includes/warehouse/concepts/id-concepts/session-6b976df83627.md) %}
||
||
[`state`](#state-desc)
|
[object](*object)

Данные о сохраненном состоянии.
||
||
`version`
|
[string](*string)

Версия протокола.

Текущая версия — 1.0.
||
|#

## meta {#meta-desc}

Информация об устройстве, с помощью которого пользователь разговаривает с Алисой.

#|
||**Свойство** |**Описание**||
||
`locale`
|
[string](*string)

Язык в POSIX-формате, максимум 64 символа.
||
||
`timezone`
|
[string](*string)

Название часового пояса, включая алиасы, максимум 64 символа.
||
||
`client_id`
|
[string](*string)

Не рекомендуется к использованию. Интерфейсы, доступные на клиентском устройстве, перечислены в свойстве `interfaces`.

Идентификатор устройства и приложения, в котором идет разговор, максимум 1024 символа.
||
||
[`interfaces`](#interfaces-desc)
|
[object](*object)

Интерфейсы, доступные на устройстве пользователя.
||
|#

## meta.interfaces {#interfaces-desc}

Интерфейсы, доступные на устройстве пользователя.

#|
||**Свойство** |**Описание**||
||
`screen`
|
[object](*object)

Пользователь может видеть ответ навыка на экране и открывать ссылки в браузере.
||
||
`account_linking`
|
[object](*object)

У пользователя есть возможность запросить [связку аккаунтов](https://yandex.ru/dev/dialogs/alice/doc/ru/auth/when-to-use.md).
||
||
`audio_player`
|
[object](*object)

На устройстве пользователя есть аудиоплеер. 
||
|#

## request {#request-desc}

Данные, полученные от пользователя.

#|
||**Свойство** |**Описание**||
||
`type`
|
[string](*string)

Обязательное свойство.

Тип ввода. Возможные значения:

- `"SimpleUtterance"` — [голосовой ввод](https://yandex.ru/dev/dialogs/alice/doc/ru/request-simpleutterance.md).
- `"ButtonPressed"` — [нажатие кнопки](https://yandex.ru/dev/dialogs/alice/doc/ru/request-buttonpressed.md).
- `"Show.Pull"` — [запрос на чтение данных для шоу](https://yandex.ru/dev/dialogs/alice/doc/ru/request-show-pull.md).
||
|#

## session {#session-desc}

{% include [request-session-data](_includes/request/id-request/session-data-066946a56e5d.md) %}


{% include [concepts-session](_includes/warehouse/concepts/id-concepts/session-6b976df83627.md) %}

#|
||**Свойство** |**Описание**||
||
`session_id`
|
[string](*string)

Уникальный идентификатор сессии, максимум 64 символа.
||
||
`message_id`
|
[number](*number)

Идентификатор сообщения в рамках сессии, максимум 8 символов.
Инкрементируется с каждым следующим запросом.
||
||
`skill_id`
|
[string](*string)

Идентификатор вызываемого навыка, присвоенный при создании.

Чтобы узнать идентификатор своего навыка, откройте его в [консоли разработчика](https://dialogs.yandex.ru/developer/) — идентификатор можно скопировать на вкладке **Общие сведения**, внизу страницы.
||
||
`user_id`
|
[string](*string)

Свойство не поддерживается — вместо него следует использовать новое, полностью аналогичное свойство [`session.application.application_id`](#application-desc).

Идентификатор экземпляра приложения, в котором пользователь общается с Алисой, максимум 64 символа.

Даже если пользователь вошел в один и тот же аккаунт в приложение Яндекс для Android и iOS, Яндекс Диалоги присвоят отдельный `user_id` каждому из этих приложений.
||
||
[`user`](#user-desc)
|
[object](*object)

Атрибуты пользователя Яндекса, который взаимодействует с навыком. Если пользователь не авторизован в приложении, свойства `user` в запросе не будет.
||
||
[`application`](#application-desc)
|
[object](*object)

Данные о приложении, с помощью которого пользователь взаимодействует с навыком.
||
||
`new`
|
[boolean](*boolean)

Признак новой сессии. Возможные значения:

- `true` — пользователь начинает новый разговор с навыком;
- `false` — запрос отправлен в рамках уже начатого разговора.
||
|#

## session.user {#user-desc}

Атрибуты пользователя Яндекса, который взаимодействует с навыком. Если пользователь не авторизован в приложении, свойства `user` в запросе не будет.

#|
||**Свойство** |**Описание**||
||
`user_id`
|
[string](*string)

Идентификатор пользователя Яндекса, единый для всех приложений и устройств.

Этот идентификатор уникален для пары «пользователь — навык»: в разных навыках значение свойства `user_id` для одного и того же пользователя будет различаться.
||
||
`access_token`
|
[string](*string)

Токен для OAuth-авторизации, который также передается в заголовке `Authorization` для навыков с настроенной [связкой аккаунтов](https://yandex.ru/dev/dialogs/alice/doc/ru/auth/when-to-use.md).

Это JSON-свойство можно использовать, например, при реализации навыка в Yandex Cloud Functions (Диалоги вызывают функции с параметром [integration=raw](https://cloud.yandex.ru/docs/functions/concepts/function-invoke#http),который не позволяет получать заголовки клиентского запроса).
||
|#

## session.application {#application-desc}

Данные о приложении, с помощью которого пользователь взаимодействует с навыком.

#|
||**Свойство** |**Описание**||
||
`application_id`
|
[string](*string)

Идентификатор экземпляра приложения, в котором пользователь общается с Алисой, максимум 64 символа.

Даже если пользователь вошел в один и тот же аккаунт в приложение Яндекс для Android и iOS, Яндекс Диалоги присвоят отдельный `application_id` каждому из этих приложений.

Этот идентификатор уникален для пары «приложение — навык»: в разных навыках значение свойства `application_id` для одного и того же пользователя будет различаться.
||
|#

## state {#state-desc}

Данные о сохраненном состоянии.

#|
||**Свойство** |**Описание**||
||
`session`
|
[object](*object)

Состояние навыка в контексте [сессии](https://yandex.ru/dev/dialogs/alice/doc/ru/session-persistence.md#store-session).
||
||
`user`
|
[object](*object)

Состояние навыка в контексте [авторизованного пользователя](https://yandex.ru/dev/dialogs/alice/doc/ru/session-persistence.md#store-between-sessions).
||
||
`application`
|
[object](*object)

Состояние навыка в контексте [экземпляра приложения пользователя](https://yandex.ru/dev/dialogs/alice/doc/ru/session-persistence.md#store-application).
||
|#

{% include [index-support-button](_includes/index/id-index/support-button-9f06b32e2ffb.md) %}

[*string]: Cтрока, выделяется кавычками, например `"Hello world"`.

[*number]: Целое или дробное число без кавычек, например `25.5`.

[*boolean]: Логическое значение без кавычек: `true` (истина) или `false` (ложь).

[*array]: Массив элементов, разделенных запятой. Элементом могут быть стандартные элементы JSON: строка, число, `true`, `false`, объект или массив. Массив выделяется квадратными скобками `[]`: ```"cities": ["Moscow", "Tokyo", "New York"] ```

[*object]: Список пар `"ключ": значение`, разделенных запятой. Выделяется фигурными скобками `{}`.
```
{
  "name": "John",
  "surname": "Smith"
}
```
