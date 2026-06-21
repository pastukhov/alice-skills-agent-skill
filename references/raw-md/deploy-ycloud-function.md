---
metadata:
  - name: generator
    content: Diplodoc Platform v5.39.1
alternate:
  - https://yandex.ru/dev/dialogs/alice/doc/ru/deploy-ycloud-function.md
---
# Размещение навыка в Yandex Cloud

{% include notitle [neuroexpert-button](_includes/reusables/neuroexpert-button-99270fdba323.md) %}


Сервис Yandex Cloud Functions позволяет запускать ваш код в обслуживаемой среде в виде [функции](https://cloud.yandex.ru/docs/functions/concepts/function). Сервис автоматически настраивает необходимое окружение в зависимости от нагрузки — вы платите только за количество вызовов функции и затраченные вычислительные ресурсы.

Функции сервиса Cloud Functions, используемые для навыков Алисы, бесплатны и не тарифицируются.

{% cut "Посмотреть видео «Как бесплатно разместить навык Алисы в Yandex Cloud»" %}


<div style="
    border:1px solid #d1d5db;
    border-radius:20px;
    overflow:hidden;
    max-width:100%;
">
  <iframe src="https://runtime.strm.yandex.ru/player/video/vplvmbmwed25qlf7wyts?autoplay=0&mute=0"
    frameborder="0"
    allowfullscreen
    style="
      display:block;
      width:100%;
      height:360px;
      "></iframe>
</div>

{% endcut %}

В качестве примера будет создан навык «Попугай», который повторяет все, что ему написал или сказал пользователь. Пример реализован на двух языках программирования: Python и Node.js.

## Подготовка {#preparation}

Перед началом вам необходимо зарегистрировать [платежный аккаунт](https://cloud.yandex.ru/docs/billing/quickstart/index) в Yandex Cloud.

Сразу после регистрации в Yandex Cloud вам станет доступно рабочее пространство — облако. Создайте в облаке [функцию для навыка](https://cloud.yandex.ru/docs/functions/solutions/alice-skill#create-function).

## Создание веб-приложения {#create}

{% list tabs %}

- Node.js

    Создайте веб-приложение на базе Node.js по [инструкции в документации](https://yandex.ru/dev/dialogs/alice/doc/ru/quickstart-programming.md).

    Для работы навыка скачайте с GitHub файл с примером [index.js](https://github.com/yandex-cloud/examples/blob/master/serverless/functions/alice/nodejs/parrot/index.js).

- Python

    Создайте веб-приложение на базе Python по [инструкции в документации](https://yandex.ru/dev/dialogs/alice/doc/ru/quickstart-programming.md).

    Для работы навыка скачайте с GitHub файл с примером [parrot.py](https://github.com/yandex-cloud/examples/blob/master/serverless/functions/alice/python/parrot/parrot.py).

{% endlist %}

## Добавление в навык ссылки на функцию {#register}

После того, как навык заработает, его можно зарегистрировать:

1. Перейдите в [консоль разработчика навыка](https://dialogs.yandex.ru/developer/).
1. Откройте вкладку **Настройки**.
1. В блоке **Backend** выберите вариант **Функция в Yandex Cloud**.
1. Из выпадающего списка выберите нужную функцию.
    
    В списке отображаются функции, которые вы имеете право просматривать, но навык будет работать только если ваш аккаунт может запускать выбранную функцию. Разрешение на запуск входит в роли Yandex Cloud serverless.functions.invoker, [editor](https://cloud.yandex.ru/docs/functions/security/#editor) и выше.
    
1. Внизу страницы нажмите кнопку **Сохранить**.
1. Проверьте работу навыка на вкладке **Тестирование**. Подробнее см. раздел [Тестирование навыка](https://yandex.ru/dev/dialogs/alice/doc/ru/test.md).

Чтобы писать более сложные навыки, ознакомьтесь с [протоколом работы Яндекс Диалогов](https://yandex.ru/dev/dialogs/alice/doc/ru/protocol.md).

{% include [index-support-button](_includes/index/id-index/support-button-0b4480a5dc1a.md) %}


