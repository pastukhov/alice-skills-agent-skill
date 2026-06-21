---
metadata:
  - name: generator
    content: Diplodoc Platform v5.39.1
alternate:
  - https://yandex.ru/dev/dialogs/alice/doc/ru/session-persistence.md
---
# Хранение состояния

{% include notitle [neuroexpert-button](_includes/reusables/neuroexpert-button-99270fdba323.md) %}


Возможность работает в тестовом режиме и активно развивается, поэтому протокол ее использования может меняться.

API Яндекс Диалогов позволяет сохранять данные внутри сессии навыка, а если пользователь авторизован на поверхности, где работает навык, — то и между сессиями.

{% list tabs %}

- Как и где хранить данные

  <div style="
    border:1px solid #d1d5db;
    border-radius:20px;
    overflow:hidden;
    max-width:100%;
">
  <iframe src="https://runtime.strm.yandex.ru/player/video/vplv7flxlfgztwxpsaj5?autoplay=0&mute=0"
    frameborder="0"
    allowfullscreen
    style="
      display:block;
      width:100%;
      height:360px;
      "></iframe>
</div>

- Кеширование в навыках

  <div style="
    border:1px solid #d1d5db;
    border-radius:20px;
    overflow:hidden;
    max-width:100%;
">
  <iframe src="https://runtime.strm.yandex.ru/player/video/vplvin4wqcvtt75onh25?autoplay=0&mute=0"
    frameborder="0"
    allowfullscreen
    style="
      display:block;
      width:100%;
      height:360px;
      "></iframe>
</div>

{% endlist %}

## Первоначальная настройка {#setup}

Подключите возможность сохранять состояние (стейт):

1. В [консоли разработчика](https://dialogs.yandex.ru/developer/) откройте страницу настроек навыка.
1. В блоке **Основные настройки** найдите опцию **Хранилище**.
1. Выберите **Использовать хранилище данных в навыке**.

## Хранение стейта сессии {#store-session}

Чтобы сохранить данные внутри сессии, навык должен отправить свойство `session_state` в ответе. Записанное значение придет в следующем запросе в навык. Данные хранятся до конца сессии.

{% include [concepts-session](_includes/warehouse/concepts/id-concepts/session-6b976df83627.md) %}


Максимальный размер JSON-объекта `session_state` — 1 КБ:

```json
{
  "response": {
    "text": "Здравствуйте! Это мы, хороводоведы.",
    "tts": "Здравствуйте! Это мы, хоров+одо в+еды.",
    "end_session": false
  },
  "session_state": {
      "value": 10
  },
  "version": "1.0"
}
```

Стейт сессии перестанет храниться, если в ответе навыка не вернуть свойство `session_state`. Если для запроса стейт не меняется, но его нужно хранить, навыку следует вернуть тот же объект `session_state`, что пришел в запросе.

Пример запроса с сохраненным стейтом:

```json
{
  "meta": {
    "locale": "ru-RU",
    "timezone": "Europe/Moscow",
    "client_id": "ru.yandex.searchplugin/5.80 (Samsung Galaxy; Android 4.4)",
    "interfaces": {
      "screen": { }
    }
  },
  "request": {
    "command": "привет",
    "original_utterance": "привет",
    "type": "SimpleUtterance",
    "markup": {
      "dangerous_context": true
    },
    "payload": {},
    "nlu": {
      "tokens": [
         "привет"
      ],
      "entities": [
      ]
    }
  },
  "session": {
    "new": true,
    "message_id": 4,
    "session_id": "2eac4854-fce721f3-b845abba-20d60",
    "skill_id": "3ad36498-f5rd-4079-a14b-788652932056",
    "user_id": "AC9WC3DF6FCE052E45A4566A48E6B7193774B84814CE49A922E163B8B29881DC",
    "application": {
      "application_id": "AC9WC3DF6FCE052E45A4566A48E6B7193774B84814CE49A922E163B8B29881DC"
    },
  },
  "state": {
    "session": {
      "value": 10
    }
  },
  "version": "1.0"
}
```

## Хранение стейта между сессиями {#store-between-sessions}

Стейт навыка хранится только для пользователей, которые авторизовались с помощью Яндекс ID.

Чтобы сохранить данные о пользователе, навык должен отправить в ответе свойство `user_state_update`. Максимальный размер JSON-объекта — 1 КБ:

```json
{
  "response": {
    "text": "Здравствуйте! Это мы, хороводоведы.",
    "tts": "Здравствуйте! Это мы, хоров+одо в+еды.",
    "end_session": false
  },
  "session": {
    "session_id": "2eac4854-fce721f3-b845abba-20d60",
    "message_id": 4,
    "user_id": "AC9WC3DF6FCE052E45A4566A48E6B7193774B84814CE49A922E163B8B29881DC",
    "application": {
      "application_id": "AC9WC3DF6FCE052E45A4566A48E6B7193774B84814CE49A922E163B8B29881DC"
    },
  },
  "user_state_update": {
      "value": 42
  },
  "version": "1.0"
}
```

Чтобы удалить поле, записанное в стейт пользователя, навык должен отправить это поле со значением `null`.

Сохраненное значение придет в следующем запросе в навык:

```json
{
  "meta": {
    "locale": "ru-RU",
    "timezone": "Europe/Moscow",
    "client_id": "ru.yandex.searchplugin/5.80 (Samsung Galaxy; Android 4.4)",
    "interfaces": {
      "screen": { }
    }
  },
  "request": {
    "command": "привет",
    "original_utterance": "привет",
    "type": "SimpleUtterance",
    "markup": {
      "dangerous_context": true
    },
    "payload": {},
    "nlu": {
      "tokens": [
         "привет"
      ],
      "entities": [
      ]
    }
  },
  "session": {
    "new": true,
    "message_id": 4,
    "session_id": "2eac4854-fce721f3-b845abba-20d60",
    "skill_id": "3ad36498-f5rd-4079-a14b-788652932056",
    "user_id": "AC9WC3DF6FCE052E45A4566A48E6B7193774B84814CE49A922E163B8B29881DC",
    "application": {
      "application_id": "AC9WC3DF6FCE052E45A4566A48E6B7193774B84814CE49A922E163B8B29881DC"
    },
    "user": {
      "user_id": "8D7196B4A8AA15CFF3B7B3046738C03F234A7E638FFE33B23F2350BBD940B644"
    }
  },
  "state": {
    "user": {
      "value": 42
    }
  },
  "version": "1.0"
}
```

## Хранение стейта для экземпляра приложения {#store-application}

Экземпляр приложения — это конкретное приложение (например, Браузер, приложение Яндекс, Навигатор) или устройство. Разрез хранения равносилен [`session.application.application_id`](https://yandex.ru/dev/dialogs/alice/doc/ru/request.md#application-id) для навыка.

Стейт для экземпляра приложения сохраняет взаимодействие с пользователем для одной поверхности, не распространяя его на другие поверхности пользователя.

Если поверхность Алисы не поддерживает авторизацию или пользователь не авторизован на поверхности, хранение в разрезе экземпляра приложения — единственный способ сохранить контекст между сессиями.

Чтобы сохранить стейт навыка для экземпляра приложения, навык должен отправить свойство `application_state` в ответе:

```json
{
  "response": {
    "text": "Здравствуйте! Это мы, хороводоведы.",
    "tts": "Здравствуйте! Это мы, хоров+одо в+еды.",
    "end_session": false
  },
  "application_state": {
      "value": 37
  },
  "version": "1.0"
}
```

Сохраненный стейт придет в следующем запросе в навык:

```json
{
  "meta": {
    "locale": "ru-RU",
    "timezone": "Europe/Moscow",
    "client_id": "ru.yandex.searchplugin/5.80 (Samsung Galaxy; Android 4.4)",
    "interfaces": {
      "screen": { }
    }
  },
  "request": {
    "command": "привет",
    "original_utterance": "привет",
    "type": "SimpleUtterance",
    "markup": {
      "dangerous_context": true
    },
    "payload": {},
    "nlu": {
      "tokens": [
         "привет"
      ],
      "entities": [
      ]
    }
  },
  "session": {
    "new": true,
    "message_id": 4,
    "session_id": "2eac4854-fce721f3-b845abba-20d60",
    "skill_id": "3ad36498-f5rd-4079-a14b-788652932056",
    "user_id": "AC9WC3DF6FCE052E45A4566A48E6B7193774B84814CE49A922E163B8B29881DC",
    "application": {
      "application_id": "AC9WC3DF6FCE052E45A4566A48E6B7193774B84814CE49A922E163B8B29881DC"
    },
    "user": {
      "user_id": "8D7196B4A8AA15CFF3B7B3046738C03F234A7E638FFE33B23F2350BBD940B644"
    }
  },
  "state": {
    "application": {
      "value": 37
    }
  },
  "version": "1.0"
}
```

Стейт для экземпляра приложения продолжает храниться, если в ответе навыка не вернуть `application_state`. Если для запроса стейт навыка для экземпляра приложения не изменяется, то можно не присылать `application_state` в ответе или отправить его со значением `null`.

Чтобы очистить сохраненный стейт приложения, навык может отправить это поле со значением `{}` — пустым словарем.

## Полезные видео {#useful-video}

{% cut "Разработка прототипа голосового приложения (с 38:51)" %}

<div style="
    border:1px solid #d1d5db;
    border-radius:20px;
    overflow:hidden;
    max-width:100%;
">
  <iframe src="https://runtime.strm.yandex.ru/player/video/vplvba3haj2wbsimewde?autoplay=0&mute=0"
    frameborder="0"
    allowfullscreen
    style="
      display:block;
      width:100%;
      height:360px;
      "></iframe>
</div>

{% endcut %}


## Часто задаваемые вопросы {#troubleshooting}

{% cut "Как сохранить историю общения с пользователем?" %}

В настройках включите опцию **Использовать хранилище данных в навыке**, чтобы сохранять историю авторизованных пользователей. Историю неавторизованных сохраняйте на своем сервере: на Диалогах это пока невозможно.

{% endcut %}

{% cut "Можно ли сохранять стейт навыка между сессиями?" %}

Да, если пользователь авторизован на устройстве, а в настройках навыка включена опция **Использовать хранилище данных в навыке**. Для неавторизованных пользователей Диалоги сохраняют историю только внутри сессии.

{% endcut %}

{% include [index-support-button](_includes/index/id-index/support-button-919edb4c6878.md) %}

