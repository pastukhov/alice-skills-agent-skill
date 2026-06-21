---
metadata:
  - name: generator
    content: Diplodoc Platform v5.39.1
alternate:
  - https://yandex.ru/dev/dialogs/alice/doc/ru/request-buttonpressed.md
---
# ButtonPressed

{% include notitle [neuroexpert-button](_includes/reusables/neuroexpert-button-99270fdba323.md) %}


Навык получает запрос с типом `ButtonPressed`, если в предыдущем ответе пользователь нажал:

- отдельную кнопку (свойство `hide` со значением `true`) с непустым полем [payload](#request-desc);
- изображение (тип [BigImage](https://yandex.ru/dev/dialogs/alice/doc/ru/response-card-bigimage.md)) с непустым полем `payload` в `card.button`;
- элемент списка (тип [ItemList](https://yandex.ru/dev/dialogs/alice/doc/ru/response-card-itemslist.md)) с непустым полем `payload` в `items.button`;
- изображение из галереи (тип [ImageGallery](https://yandex.ru/dev/dialogs/alice/doc/ru/response-card-imagegallery.md)) с непустым полем `payload` в `items.button`.

```json
{
  "request": {
    "nlu": {
      "tokens": [
        "надпись",
        "на",
        "кнопке"
      ],
      "entities": [],
      "intents": {}
    },
    "payload": {}
    "type": "ButtonPressed"
  }
}
```

## request {#request-desc}

Данные, полученные от пользователя.

#|
||
**Свойство**
|
**Описание** 
||
||
[`markup`](#markup-desc)
|
[object](*object)

Формальные характеристики реплики, которые удалось выделить Яндекс Диалогам. Отсутствует, если ни одно из вложенных свойств не применимо.
||
||
`payload`
|
[string](*string)

JSON-объект, полученный с нажатой кнопкой от обработчика навыка (в ответе на предыдущий запрос), максимум 4096 байт.
||
||
[`nlu`](#nlu-desc)
|
[object](*object)

Слова и именованные сущности, которые Диалоги извлекли из запроса пользователя.

Подробное описание поддерживаемых типов сущностей см. в разделе [Именованные сущности в запросах ](https://yandex.ru/dev/dialogs/alice/doc/ru/naming-entities.md).
||
||
`tokens`
|
[object](*object)

Обозначение начала и конца именованной сущности в массиве слов. Нумерация слов в массиве начинается с 0.
||
||
`type`
|
[string](*string)

Тип ввода. Возможные значения см. в разделе [Формат запроса](https://yandex.ru/dev/dialogs/alice/doc/ru/request.md#request-desc).
||
|#

## request.markup {#markup-desc}

Формальные характеристики реплики, которые удалось выделить Яндекс Диалогам. Объект отсутствует, если ни одно из вложенных свойств не применимо.

#|
||
**Свойство**
|
**Описание** 
||
||
`dangerous_context`
|
[boolean](*boolean)

Признак реплики, которая содержит криминальный подтекст (самоубийство, разжигание ненависти, угрозы). Вы можете настроить навык на определенную реакцию для таких случаев — например, отвечать «Не понимаю, о чем вы. Пожалуйста, переформулируйте вопрос.»

Возможно только значение `true`. Если признак не применим, это свойство не включается в ответ.
||
|#

## request.nlu {#nlu-desc}

Слова и сущности, которые Диалоги извлекли из запроса пользователя.

Подробное описание поддерживаемых типов сущностей см. в разделе [Именованные сущности в запросах](https://yandex.ru/dev/dialogs/alice/doc/ru/naming-entities.md).

#|
||
**Свойство**
|
**Описание** 
||
||
`tokens[]`
|
[array](*array) of [strings](*string).

Массив слов из произнесенной пользователем фразы.

||
||
[`entities[]`](#entities-desc)
|
[array](*array) of [objects](*object).

Массив именованных сущностей.
||
||
`intents`
|
[object](*object)

Объект с данными, извлеченными из пользовательского запроса.

Подробнее см. в разделе [Обработка естественного языка (NLP)](https://yandex.ru/dev/dialogs/alice/doc/ru/nlu.md).
||
|#

## request.nlu.entities {#entities-desc}

Массив именованных сущностей.

#|
||
**Свойство**
|
**Описание** 
||
||
`start`
|
[number](*number)

Первое слово именованной сущности.
||
||
`end`
|
[number](*number)

Первое слово после именованной сущности.
||
||
`type`
|
[string](*string)

Тип именованной сущности. Возможные значения:
- `YANDEX.DATETIME` — дата и время, абсолютные или относительные.
- `YANDEX.FIO` — фамилия, имя и отчество.
- `YANDEX.GEO` — местоположение (адрес или аэропорт).
- `YANDEX.NUMBER` — число, целое или с плавающей точкой.
||
||
`value`
|
[object](*object)

Формальное описание именованной сущности.

Формат этого поля для всех поддерживаемых типов сущностей приведен в разделе [Именованные сущности в запросах ](https://yandex.ru/dev/dialogs/alice/doc/ru/naming-entities.md).
||
|#

{% include [index-support-button](_includes/index/id-index/support-button-08b8e9fe5c37.md) %}

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


