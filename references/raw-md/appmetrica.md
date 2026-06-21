---
metadata:
  - name: generator
    content: Diplodoc Platform v5.39.1
alternate:
  - https://yandex.ru/dev/dialogs/alice/doc/ru/appmetrica.md
---
# AppMetrica

{% include notitle [neuroexpert-button](_includes/reusables/neuroexpert-button-99270fdba323.md) %}


AppMetrica позволяет разработчику собирать статистику о том, как люди пользуются навыком: например, аудиторные показатели, количество и длину сессий. Собранные данные можно просматривать в веб-интерфейсе AppMetrica.

Чтобы начать собирать статистику:

1. [Добавьте приложение](https://appmetrica.yandex.ru/docs/quick-start/concepts/quick-start.html) в интерфейсе AppMetrica.
1. Скопируйте значение поля **API key (для использования в SDK)** в поле **API-ключ** настроек навыка.
1. Сохраните настройки и опубликуйте навык. Если никакие поля кроме **API-ключ** не изменялись, модерация пройдет автоматически.

Данные могут поставляться с задержкой до нескольких часов.

Вы можете настроить навык так, чтобы он генерировал собственные [события](https://appmetrica.yandex.ru/docs/data-collection/about-events.html) `analytics.events` и отправлял информацию о них вместе с [ответом](https://yandex.ru/dev/dialogs/alice/doc/ru/response.md) платформе Диалогов.

Пример такого ответа:

```json
{
    "response": {
        "text": "Здравствуйте! Это мы, хороводоведы.",
    },
    "analytics": {
        "events": [
            {
                "name": "custom event"
            },
            {
                "name": "another custom event",
                "value": {
                    "field": "some value",
                    "second field": {
                        "third field": "custom value"
                    }
                }
            }
        ]
    }
}
```

Эти события попадут в отчет блока **События** в интерфейсе [AppMetrica](https://appmetrica.yandex.ru).


## Полезные видео {#useful-videos}

{% cut "Публикация и продвижение навыков (с 18:36)" %}

<div style="
    border:1px solid #d1d5db;
    border-radius:20px;
    overflow:hidden;
    max-width:100%;
">
  <iframe src="https://runtime.strm.yandex.ru/player/video/vplverwkt63q2a6ildqc?autoplay=0&mute=0"
    frameborder="0"
    allowfullscreen
    style="
      display:block;
      width:100%;
      height:360px;
      "></iframe>
</div>

{% endcut %}

{% cut "Разработка прототипа голосового приложения (с 1:14:26)" %}

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

{% include [index-support-button](_includes/index/id-index/support-button-523b84cd912c.md) %}


