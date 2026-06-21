---
metadata:
  - name: generator
    content: Diplodoc Platform v5.39.1
alternate:
  - https://yandex.ru/dev/dialogs/alice/doc/ru/deploy-azure.md
---
# Размещение навыка в Azure

{% include notitle [neuroexpert-button](_includes/reusables/neuroexpert-button-99270fdba323.md) %}


Примеры навыков для Node.js и Python проверены и адаптированы для размещения на платформе [Microsoft Azure](https://azure.com). Если вы не пользовались этим сервисом раньше, вы сможете развернуть и проверить свой навык в Azure в рамках бесплатного периода.

**Виртуальная машина или веб-приложение в [Microsoft Azure](https://azure.com)**

#|
||
**Бесплатный доступ и тарификация** 
|
**Связка аккаунтов** 
|
**Командная разработка** 
|
**Поддерживаемые среды разработки** 
||
||
Пробный период включает [стартовый грант](https://azure.microsoft.com/ru-ru/free/) на 30 дней.

Виртуальные машины, базы данных и некоторые службы Azure предоставляются бесплатно в течение 12 месяцев.

Все бесплатные сервисы ограничены по ресурсам: 750 часов вычислений на виртуальных машинах в месяц, 10 приложений с Azure App Service.
|
Обязательна.

Необходимо связать [учетную запись Microsoft](https://signup.live.com/signup) с [учетной записью Azure](https://account.azure.com/signup).
|
Возможна.

Настройте доступ пользователей в [Azure Active Directory](https://docs.microsoft.com/ru-ru/azure/active-directory).
|
Поддерживаются операционные системы на базе Linux и Windows.

Среды выполнения: Node.js, Python, Java, PHP, .NET Core, Ruby.

Если необходимая среда выполнения не поддерживается во встроенных образах, ее можно развернуть с помощью пользовательского контейнера.
||
|#


## Подготовка {#preparation}

1. Создайте нужные учетные записи, если у вас их еще нет:
    
    - [Учетная запись Microsoft](https://signup.live.com/signup).
    - [Учетная запись Azure](https://azure.microsoft.com/ru-ru/free/), привязанная к аккаунту Microsoft.
    
1. Установите [Azure CLI](https://docs.microsoft.com/ru-ru/cli/azure/install-azure-cli). Выполните консольную команду `az --version` . Убедитесь, что установлена версия 2.0.80 или выше.
1. Войдите в Azure с помощью CLI, используя консольную команду `az login`. Откроется окно браузера для ввода учетных данных.

## Создание веб-приложения {#create}

{% list tabs %}

- Node.js

    1\. Установите [Node.js](https://nodejs.org/en/). С помощью команды `node --version` убедитесь, что платформа установлена.

    2\. Скачайте или скопируйте исходный код примера из [GitHub-репозитория Яндекса](https://github.com/yandex/alice-skills/tree/master/node.js/parrot/cloud).

    3\. Перейдите в каталог приложения и установите пакеты NPM с помощью команды `npm install`.

    4\. Запустите сервер разработки: выполните команду `npm start`.

    5\. Разверните приложение с помощью Azure. Используйте команду ниже, подставив вместо `<app-name>` уникальное имя приложения.
        
    {% cut "Linux"%} 

    `az webapp up --sku F1 --name <app-name>`

    {% endcut %}

    {% cut "Windows" %}

    `az webapp up --sku F1 --name <app-name> --os-type Windows`

    {% endcut %}
        
    6\. Дождитесь окончания процесса, чтобы получить URL в строке `"URL": http://***.azurewebsites.net`.

- Python

    1\. Установите [Python 3.6 или более поздней версии](https://www.python.org/downloads/). В командной строке выполните команду, чтобы убедиться, что установлена нужная версия:
        - `python3 --version` — для Linux.
        - `py -3 --version` — для Windows.
        
    2\. Cкачайте или скопируйте исходный код примера из [GitHub-репозитория Яндекса](https://github.com/yandex/alice-skills/tree/master/python/buy-elephant/azure).
        
    3\. Перейдите в каталог приложения. Создайте виртуальную среду:
        
    {% cut "Linux" %} 
    
    ```
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```

    {% endcut %}
    
    {% cut "Windows" %}
    
    ```
    py -3 -m venv .venv
    source .venv\\scripts\\activate
    pip install -r requirements.txt
    ```

    {% endcut %}
        
    4\. Запустите сервер разработки: в командной строке выполните команду `flask run.`

    5\. Разверните приложение с помощью Azure. Используйте команду ниже, подставив вместо `<app-name>` уникальное имя приложения.
        
    {% cut "Linux"%}

    `az webapp up --sku F1 --name <app-name>`

    {% endcut %}

    {% cut "Windows" %}

    `az webapp up --sku F1 --name <app-name> --os-type Windows`

    {% endcut %}
        
    6\. Дождитесь окончания процесса, чтобы получить URL в строке `"URL": http://***.azurewebsites.net`.

{% endlist %}

## Добавление Webhook URL {#register}

1. Перейдите в [консоль разработчика](https://dialogs.yandex.ru/developer/).
1. [Создайте навык](https://yandex.ru/dev/dialogs/alice/doc/ru/skill-create-console.md) и перейдите на вкладку **Настройки**.
1. В блоке **Backend** выберите **Webhook URL** и укажите URL приложения. Замените `http` на `https`.
1. Внизу страницы нажмите кнопку **Сохранить**.

## Тестирование навыка {#testing}

Подробнее о [тестировании навыка](https://yandex.ru/dev/dialogs/alice/doc/ru/test.md).

{% list tabs %}

- Node.js

    1. Проверьте работу навыка на вкладке **Тестирование**. Если все настроено правильно, появится приветствие: **Hello!**
    1. Отправьте сообщение с любым текстом и убедитесь, что вам пришел ответ с таким же содержанием.
    1. Попробуйте изменить код навыка. Откройте файл `index.js` в визуальном редакторе. Отредактируйте приветственную фразу: в тексте кода замените `'Hello!'` на `'Привет!'`.
    1. Повторно разверните приложение с помощью консольной команды `az webapp up`.
    1. Обновите страницу на вкладке **Тестирование**. Проверьте изменения в навыке.

- Python

    1. Проверьте работу навыка на вкладке **Тестирование**. Если все настроено правильно, появится приветствие: **Привет! Купи слона!**
    1. Отправьте сообщение и убедитесь, что навык отвечает.
    1. Попробуйте изменить код навыка. Откройте файл `app.py` в визуальном редакторе. Отредактируйте приветственную фразу: в тексте кода замените `'Привет! Купи слона!'` на `'Добрый день! Не желаете купить слона?'`.
    1. Повторно разверните приложение с помощью консольной команды `az webapp up`.
    1. Обновите страницу на вкладке **Тестирование**. Проверьте изменения в навыке.

{% endlist %}

Чтобы писать более сложные навыки, ознакомьтесь с [протоколом работы Яндекс Диалогов](https://yandex.ru/dev/dialogs/alice/doc/ru/protocol.md).

{% include [index-support-button](_includes/index/id-index/support-button-33c5888d8227.md) %}
