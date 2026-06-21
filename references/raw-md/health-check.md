---
metadata:
  - name: generator
    content: Diplodoc Platform v5.39.1
alternate:
  - https://yandex.ru/dev/dialogs/alice/doc/ru/health-check.md
---
# Периодическая проверка ответов

{% include notitle [neuroexpert-button](_includes/reusables/neuroexpert-button-99270fdba323.md) %}


Яндекс Диалоги периодически проверяют, что опубликованные навыки работают и корректно отвечают на запросы. Если навык не отвечает несколько часов, его могут отключить. Чтобы опубликовать его повторно, придется заново проходить модерацию.

Обрабатывайте проверочные запросы, как и обычные запросы пользователей, по [протоколу HTTPS](https://yandex.ru/dev/dialogs/alice/doc/ru/protocol.md).

Запросы от Диалогов вы найдете (например, чтобы подсчитать статистику) по значению свойства `original_utterance` в запросе:

```
...
 "request": {
    "command": "",
    "original_utterance": "ping",
    "type": "SimpleUtterance",
    },
...
```

{% include [index-support-button](_includes/index/id-index/support-button-27151debcb9c.md) %}


