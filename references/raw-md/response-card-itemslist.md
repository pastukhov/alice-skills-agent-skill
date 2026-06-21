---
metadata:
  - name: generator
    content: Diplodoc Platform v5.39.1
alternate:
  - https://yandex.ru/dev/dialogs/alice/doc/ru/response-card-itemslist.md
---
# ItemsList

{% include notitle [neuroexpert-button](_includes/reusables/neuroexpert-button-99270fdba323.md) %}


В ответе навык передает свойство [`response.card.type`](#card-type) со значением `ItemsList`:

```json
{
    "card": {
        "type": "ItemsList",
        "header": {
            "text": "Заголовок списка изображений",
        },
        "items": [
            {
                "image_id": "<image_id>",
                "title": "Заголовок для изображения.",
                "description": "Описание изображения.",
                "button": {
                    "text": "Надпись на кнопке",
                    "url": "https://example.com/",
                    "payload": {}
                }
            }
        ],
        "footer": {
            "text": "Текст блока под изображением.",
            "button": {
                "text": "Надпись на кнопке",
                "url": "https://example.com/",
                "payload": {}
            }
        }
    }
}
```

[Посмотреть в интерфейсе](https://yandex.ru/dev/dialogs/alice/doc/ru/interface.md#list)

## card {#card-desc}

{% include [response-card-bigimage-response-card](_includes/response-card-bigimage/id-response-card-bigimage/response-card-3f58599a86e1.md) %}

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

Для списка от 1 до 5 изображений укажите значение `ItemsList`.
||
||
`header`
|
[object](*object)

Заголовок списка изображений.
||
||
`items[]`
|
[array](*array) of [objects](*object)

Набор от 1 до 5 изображений.
||
||
`footer`
|
[object](*object)

Кнопки под списком изображений.
||
|#

## card.header {#header-desc}

Заголовок списка изображений.

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

Обязательное свойство, если передается `header`.

Текст заголовка.

Максимум 64 символа.
||
|#

## card.items {#items-desc}

Набор от 1 до 5 изображений.

#|
||
**Свойство**
|
**Описание** 
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

Максимум 256 символов.
||
||
`button`
|
[object](*object)

Свойства кликабельного изображения.
||
|#

## card.items.button {#items-button-desc}

{% include [response-card-itemslist-card-button](_includes/response-card-itemslist/id-response-card-itemslist/card-button-64b4d8b353e2.md) %}

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

Если это свойство не передано в ответе, Диалоги используют вместо него свойство `response.card.items.title`.
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

## card.footer {#footer-desc}

Кнопки под списком изображений.

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

Обязательное свойство, если передается `footer`.

Текст первой кнопки.

Максимум 64 символа.
||
||
`button`
|
[object](*object)

Дополнительная кнопка для списка изображений.
||
|#

## card.footer.button {#footer-button-desc}

Дополнительная кнопка для списка изображений.

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

Текст кнопки, обязателен для каждой кнопки.

Максимум 64 символа.

Если для кнопки не указано свойство `url`, по нажатию текст кнопки будет отправлен навыку как реплика пользователя.
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

{% include [index-support-button](_includes/index/id-index/support-button-67d928c323ee.md) %}

[*string]: Cтрока, выделяется кавычками, например `"Hello world"`.

[*object]: Список пар `"ключ": значение`, разделенных запятой. Выделяется фигурными скобками `{}`.
```
{
  "name": "John",
  "surname": "Smith"
}
```

[*array]: Массив элементов, разделенных запятой. Элементом могут быть стандартные элементы JSON: строка, число, `true`, `false`, объект или массив. Массив выделяется квадратными скобками `[]`: ```"cities": ["Moscow", "Tokyo", "New York"] ```

