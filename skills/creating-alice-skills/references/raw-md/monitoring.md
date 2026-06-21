---
metadata:
  - name: generator
    content: Diplodoc Platform v5.39.1
alternate:
  - https://yandex.ru/dev/dialogs/alice/doc/ru/monitoring.md
---
# Мониторинг работы навыка

{% include notitle [neuroexpert-button](_includes/reusables/neuroexpert-button-99270fdba323.md) %}


Яндекс Диалоги позволяют анализировать работу вашего навыка — просматривать
 статистику запросов и получать отчеты об ошибках. Это поможет своевременно выявлять
 проблемы в обработке запросов от Диалогов.

## Статистика {#statistics}

Статистика доступна только для опубликованных навыков.

Чтобы посмотреть статистику, откройте [консоль разработчика](https://dialogs.yandex.ru/developer/), перейдите на страницу навыка и откройте
 вкладку **Мониторинг**.

![Вкладка Мониторинг страницы навыка в консоли разработчика](_images/monitoring/monitoring.png)

**1. Период отчета**

:   Период, за который будет построен отчет. По умолчанию выбраны сутки. Можно установить интервал дат, не превышающий полгода.

**2. Источник**

:   Для каких источников строить отчет. Под источником имеется в виду интерфейс, с помощью которого отправлялись команды в навык. Для навыков общего типа доступен только источник **Пользовательские запросы**.
    
    Содержимое отчета можно настраивать — включать и выключать каждый тип данных под графиком. Например, показывать нужный перцентиль или только ошибки `error_http_5xx`.

**3. Тип запроса**

:   Для каких запросов получать статистику. Для навыков общего типа доступен только **Запрос в навык**.

## Отчеты {#reports}

Доступны следующие отчеты:

- [Запросы в навык](#rps)
- [Тайминги](#time-limit)

#### Запросы в навык {#rps}

Первый график показывает количество запросов от Диалогов к
 навыку — среднее число запросов в секунду за определенную
 минуту. Например, на графике ниже — 23 ноября в 17.40 было
 отправлено в среднем 0,0086 запроса в секунду (в среднем за эту
 минуту).

![](_images/monitoring/rps.png)

Второй график показывает тип и количество ошибок (в штуках) или их процентное отношение от общего числа запросов за единицу времени (если выбран период сутки, то за час; час — за 5 минут; неделя — за 6 часов; месяц — за сутки; полгода — за неделю).

![](_images/monitoring/err-status.png)

#### Тайминги {#time-limit}

{% include [restricts-response-time-limit](_includes/warehouse/concepts/id-restricts/response-time-limit-1235cb6cbdbe.md) %}


График показывает, в какое время укладывается соответствующая выбранному
 перцентилю доля запросов. Время для каждого запроса считается от
 отправки запроса Диалогами до получения ответа от навыка. Например, если
 75-перцентиль равен 0,175 секунды, значит 75% от этих
 запросов уложились в 0,175 секунды.

![](_images/monitoring/time-limits.png)

## Как работать с аналитикой {#analytics}

<div style="
    border:1px solid #d1d5db;
    border-radius:20px;
    overflow:hidden;
    max-width:100%;
">
  <iframe src="https://runtime.strm.yandex.ru/player/video/vplvpzzubva6dvj5wixw?autoplay=0&mute=0"
    frameborder="0"
    allowfullscreen
    style="
      display:block;
      width:100%;
      height:360px;
      "></iframe>
</div>

## Полезные видео {#useful-video}

{% cut "Публикация и продвижение навыков (с 22:06)" %}

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

{% cut "Разработка прототипа голосового приложения (с 1:11:47)" %} 

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

{% include [index-support-button](_includes/index/id-index/support-button-0521e87b23a5.md) %}


