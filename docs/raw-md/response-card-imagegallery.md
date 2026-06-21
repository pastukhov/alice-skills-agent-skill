---
metadata:
  - name: generator
    content: Diplodoc Platform v5.39.1
alternate:
  - https://yandex.ru/dev/dialogs/alice/doc/ru/response-card-imagegallery.md
---
# ImageGallery

{% include notitle [neuroexpert-button](_includes/reusables/neuroexpert-button-99270fdba323.md) %}


В ответе навык передает свойство [`response.card.type`](#card-type) со значением `ImageGallery`:

```json
{
    "card": {
        "type": "ImageGallery",
        "items": [
            {
                "image_id": "1030496/2769eea171ad1d7bbbfa",
                "title": "Картинка 1",
                "button": {
                    "text": "Надпись на кнопке",
                    "url": "https://example.com/",
                    "payload": {}
                }
            },
            {
                "image_id": "1521360/ac3f78abed55b67789d2",
                "title": "Картинка 2",
                "button": {
                    "text": "Надпись на кнопке",
                    "url": "https://example.com/",
                    "payload": {}
                }
            }
        ]  
    }
}
```

[Посмотреть в интерфейсе](https://yandex.ru/dev/dialogs/alice/doc/ru/interface.md#images-list)

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

Для галереи от 1 до 10 изображений укажите значение `ImageGallery`.
||
||
`items[]`
|
[array](*array) of [objects](*object)

Набор от 1 до 10 изображений .
||
|#

## card.items {#items-desc}

Набор от 1 до 10 изображений.

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

Заголовок для изображения. Максимум 128 символов.
||
||
`button`
|
[object](*object)

Свойства кликабельного изображения.
||
|#

## card.items.button {#items-button-desc}

{% include [response-card-imagegallery-card-button](_includes/response-card-imagegallery/id-response-card-imagegallery/card-button-64b4d8b353e2.md) %}

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

Текст, который будет отправлен навыку по нажатию изображения в качестве команды пользователя.

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

{% include [index-support-button](_includes/index/id-index/support-button-c8a592ebb1ed.md) %}

[*string]: Cтрока, выделяется кавычками, например `"Hello world"`.

[*object]: Список пар `"ключ": значение`, разделенных запятой. Выделяется фигурными скобками `{}`.
```
{
  "name": "John",
  "surname": "Smith"
}
```

[*array]: Массив элементов, разделенных запятой. Элементом могут быть стандартные элементы JSON: строка, число, `true`, `false`, объект или массив. Массив выделяется квадратными скобками `[]`: ```"cities": ["Moscow", "Tokyo", "New York"] ```
