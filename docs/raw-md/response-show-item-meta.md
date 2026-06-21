---
metadata:
  - name: generator
    content: Diplodoc Platform v5.39.1
alternate:
  - https://yandex.ru/dev/dialogs/alice/doc/ru/response-show-item-meta.md
---
# show_item_meta

{% include notitle [neuroexpert-button](_includes/reusables/neuroexpert-button-99270fdba323.md) %}


В ответе навык передает свойство `show_item_meta`. Формат ответа аналогичен [обычному сообщению от навыка](https://yandex.ru/dev/dialogs/alice/doc/ru/response.md), но имеет особенности:

- обновление состояния в ответе игнорируется (`session_state`, `user_state_update`, `application_state`);
- не отображаются кнопки (`buttons`) и картинки (`card`).

Подробнее об историях от навыков см. в разделе [Навыки в утреннем шоу Алисы](https://yandex.ru/dev/dialogs/alice/doc/ru/morning-show-protocol.md).

```json
{
  "response": {
    "show_item_meta": {
      "content_id": "2870a69a-0eaa-43c0-8900-8afa7c36c127",
      "title": "story title",
      "title_tts": "story title tts",
      "publication_date": "2020-12-03T10:39:32.195044179Z",
      "expiration_date": "2020-12-03T10:59:32.195044179Z"
    },
    "text": "story text",
    "tts": "story tts"
  },
  "version": "1.0"
}
```

## response {#response}

#|
||
**Свойство**
|
**Описание** 
||
||
`show_item_meta`
|
[object](*object)

Обязательный параметр только для сценария утреннего шоу.

Параметр историй утреннего шоу Алисы.
||
|#

## response.show_item_meta {#show-item-meta-desk}

#|
||
**Свойство**
|
**Описание** 
||
||
`content_id`
|
[string](*string)

Обязательный параметр.

Уникальный идентификатор истории. Формат UUID предпочтителен, но не является обязательным.
||
||
`title`
|
[string](*string)

Заголовок истории для экрана, необязательный параметр. Если заголовок указан, то на экране покажется:

- сам заголовок истории `title` с большой буквы;
- перенос строки;
- текст истории из параметра `text`.
||
||
`title_tts`
|
[string](*string)

Заголовок истории с голосовой разметкой (text-to-speech), необязательный параметр. Если заголовок указан, то история в шоу будет составлена из `title_tts` <пауза 200 мс> `text_tts`.
||
||
`publication_date`
|
[string](*string)

Обязательный параметр.

Дата и время создания истории. Алиса игнорирует истории старше 7 дней. Строка приводится по UTC в формате ISO 8601: YYYY-MM-DDTHH:mm:ss.sssZ.
||
||
`expiration_date`
|
[string](*string)

Дата и время, до которого история будет актуальна. Алиса не добавит в шоу историю, у которой значение `expiration_date` раньше, чем время запуска шоу. Строка приводится по UTC в формате ISO 8601: YYYY-MM-DDTHH:mm:ss.sssZ.
||
|#

{% include [index-support-button](_includes/index/id-index/support-button-cff37571b60f.md) %}

[*string]: Cтрока, выделяется кавычками, например `"Hello world"`.

[*object]: Список пар `"ключ": значение`, разделенных запятой. Выделяется фигурными скобками `{}`.
```
{
  "name": "John",
  "surname": "Smith"
}
```

