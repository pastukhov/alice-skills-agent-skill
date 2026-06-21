---
metadata:
  - name: generator
    content: Diplodoc Platform v5.39.1
alternate:
  - https://yandex.ru/dev/dialogs/alice/doc/ru/response-start-account-linking.md
---
# start_account_linking

{% include notitle [neuroexpert-button](_includes/reusables/neuroexpert-button-99270fdba323.md) %}


Если навык понимает, что для выполнения запроса пользователя требуется авторизация (запрашиваются приватные данные) на стороннем сервисе, то он отправляет Диалогам ответ с директивой `start_account_linking`. Эта директива дает команду на показ карточки авторизации и начала связки аккаунтов.

Подробнее об авторизации в связанных аккаунтах см. в разделе [Как устроена авторизация](https://yandex.ru/dev/dialogs/alice/doc/ru/auth/how-it-works.md).

```json
{
  "response": {
    "text": "Книга Чародеи",
    "tts": "Вы покупаете книгу Чародеи",
    "end_session": false,
    "directives": {
        "start_account_linking": {}
    }
  },
  "version": "1.0"
}
```

## directives {#directives-desk}

#|
||
**Свойство**
|
**Описание** 
||
||
`start_account_linking`
|
[string](*string)

Директива запуска авторизации для связки аккаунтов.
||
|#

{% include [index-support-button](_includes/index/id-index/support-button-cea967dcc3ff.md) %}

[*string]: Cтрока, выделяется кавычками, например `"Hello world"`.
