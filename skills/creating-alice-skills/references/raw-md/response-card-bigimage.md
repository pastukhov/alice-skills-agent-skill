---
metadata:
  - name: generator
    content: Diplodoc Platform v5.39.1
alternate:
  - https://yandex.ru/dev/dialogs/alice/doc/ru/response-card-bigimage.md
---
# BigImage

{% include notitle [neuroexpert-button](_includes/reusables/neuroexpert-button-99270fdba323.md) %}


В ответе навык передает свойство [`response.card.type`](#card-type) со значением `BigImage`:

```json
{
    "card": {
        "type": "BigImage",
        "image_id": "1027858/46r960da47f60207e924",
        "title": "Заголовок для изображения",
        "description": "Описание изображения.",
        "button": {
            "text": "Надпись на кнопке",
            "url": "http://example.com/",
            "payload": {}
        }
    }
}
```

[Посмотреть в интерфейсе](https://yandex.ru/dev/dialogs/alice/doc/ru/interface.md#card)

## card {#card-desc}

Описание карточки — сообщения с поддержкой изображений. Если приложению удается отобразить карточку для пользователя, свойство `response.text` не используется.

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

Тип карточки. Поддерживаемые значения см. в разделе [Формат ответа](https://yandex.ru/dev/dialogs/alice/doc/ru/response.md#response-desc).

Для одного изображения укажите значение `BigImage`.
||
|| 
`image_id`
|
[string](*string)

Идентификатор изображения, который возвращается в ответ на [запрос загрузки](https://yandex.ru/dev/dialogs/alice/doc/ru/resource-upload.md).
||
||
`title`
|
[string](*string)

Заголовок для изображения.

Максимум 128 символов.
||
||
`description`
|
[string](*string)

Описание изображения.

Максимум 1024 символа.
||
||
`button`
|
[object](*object)

Свойства кликабельного изображения.
||
|#

## card.button {#card-button-desc}

{% include [response-card-bigimage-card-button](_includes/response-card-bigimage/id-response-card-bigimage/card-button-64b4d8b353e2.md) %}

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

Текст, который будет отправлен навыку по нажатию на изображение в качестве команды пользователя.

Максимум 64 символа.

Если это свойство передано с пустым значением, свойство `request.command` в запросе будет отправлено пустым.

Если это свойство не передано в ответе, Диалоги используют вместо него свойство `response.card.title`.
||
||
`url`
|
[string](*string)

URL, который должен открываться по нажатию изображения.

Максимум 1024 байта.
||
||
`payload`
|
[object](*object)

Произвольный JSON-объект, который Яндекс Диалоги должны отправить обработчику, если пользователь нажмет изображение.

Максимум 4096 байт.
||
|#

{% include [index-support-button](_includes/index/id-index/support-button-afbe34111250.md) %}

[*string]: Cтрока, выделяется кавычками, например `"Hello world"`.


[*object]: Список пар `"ключ": значение`, разделенных запятой. Выделяется фигурными скобками `{}`.
```
{
  "name": "John",
  "surname": "Smith"
}
```