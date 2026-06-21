---
metadata:
  - name: generator
    content: Diplodoc Platform v5.39.1
alternate:
  - https://yandex.ru/dev/dialogs/alice/doc/ru/deploy-google-cloud.md
---
# Размещение навыка в Google Cloud

{% include notitle [neuroexpert-button](_includes/reusables/neuroexpert-button-99270fdba323.md) %}


В инструкции описано размещение навыка на [Google Cloud Platform](https://cloud.google.com). Если вы не пользовались этим сервисом раньше, вы сможете развернуть и проверить свой навык в Google Cloud в рамках [бесплатного периода](https://cloud.google.com/free).


**Виртуальная машина или веб-приложение на [Google Cloud Platform](https://cloud.google.com)**

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
Пробный период включает [стартовый грант](https://cloud.google.com/appengine) на 90 дней.

[Google Cloud Free Program (free tier)](https://cloud.google.com/free/docs/gcp-free-tier#free-tier-usage-limits) не ограничен по времени.

Подробнее см. тарификацию сервисов [App Engine](https://cloud.google.com/appengine/pricing) и тарификацию виртуальных машин в [Compute Engine](https://cloud.google.com/compute/all-pricing).
|
Не обязательна
|
Возможна.

Настройте политику [Identity & Access Management (IAM)](https://cloud.google.com/compute/docs/access).
|
Поддерживаются операционные системы на базе Linux и Windows.

Среды выполнения: Node.js, Java, Ruby, C#, Go, Python, PHP.

Если необходимая среда выполнения не поддерживается во встроенных образах, ее можно развернуть с помощью пользовательского контейнера.
||
|#

## Подготовка {#preparation}

1. Cоздайте нужные учетные записи, если у вас их еще нет:
    
    - [Учетная запись Google](https://accounts.google.com/).
    - [Учетная запись Google Cloud](https://cloud.google.com/free), привязанная к аккаунту Google.
    
1. Перейдите в [консоль](https://console.cloud.google.com) Google Cloud и создайте новый проект. Для этого в верхней панели нажмите **New Project** → **My first Project**.
1. Находясь в созданном проекте, слева в консоли выберите **Billing**. Убедитесь, что вам доступен стартовый грант и срок его действия не истек.
1. Включите **Сloud Build API** по [ссылке](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com). Сверху выберите, для какого проекта вы подключаете API, и нажмите **Next** → **Enable**.
1. Установите Cloud SDK и авторизируйтесь.
    
    {% cut "Windows" %} 
    
    1. Скачайте и запустите [Cloud SDK Installer](https://dl.google.com/dl/cloudsdk/channels/rapid/GoogleCloudSDKInstaller.exe).
    1. Авторизируйтесь в Cloud SDK. В открывшемся окне браузера введите учетные данные аккаунта Google.

    {% endcut %}
    
    {% cut "MacOS" %} 
    
    1. Выполните консольную команду `uname -m`, чтобы определить версию системы.
    1. Установите Сloud SDK.

        {% cut "x86_64" %}

        [Cloud SDK Installer](https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-365.0.1-darwin-x86_64.tar.gz)

        {% endcut %}
        
        {% cut "arm64" %}

        [Cloud SDK Installer](https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-365.0.1-darwin-arm.tar.gz)

        {% endcut %}

        {% cut "x86" %}

        [Cloud SDK Installer](https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-365.0.1-darwin-x86.tar.gz)

        {% endcut %}
    
    1. Выполните команду`./google-cloud-sdk/bin/gcloud init`.

    {% endcut %}
    

## Создание веб-приложения {#create}

{% list tabs %}

- Node.js

    1\. Создайте веб-приложение App Engine. Используйте консольную команду ниже, заменив `[YOUR_PROJECT_ID]` на Projeсt ID вашего проекта:
        ```
        gcloud app create --project=[YOUR_PROJECT_ID]
        ```
        
    2\. Выберите регион.

    3\. Установите [Git](https://git-scm.com/).

    4\. Установите nvm и Node.js.
        
    {% cut "Windows" %}
    
    1. Удалите Node.js, если устанавливали его ранее. Установите [NVM for Windows](https://github.com/coreybutler/nvm-windows/releases).
    1. Установите Node.js. Используйте команду `nvm install stable`.
    1. С помощью команды `node --version` убедитесь, что платформа установлена.

    {% endcut %}
    
    {% cut "MacOS" %}
    
    1. Выполните команду `curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh`.
    1. Установите Node.js. Используйте команду `nvm install stable`.
    1. С помощью команды `node --version` убедитесь, что платформа установлена.

    {% endcut %}
        
    5\. Скачайте или скопируйте исходный код примера из [GitHub-репозитория Яндекса](https://github.com/yandex/alice-skills/tree/master/node.js/parrot/google-cloud).

    6\. Перейдите в каталог приложения. Установите пакеты NPM c помощью команды `npm install`.

    7\. Запустите сервер разработки: выполните команду `npm start`.

    8\. Разверните приложение с помощью Google Cloud: выполните команду `gcloud app deploy`.

    9\. Дождитесь окончания процесса, чтобы получить URL в строке `"target url": https://***.appspot.com`.

- Python

    1. Установите [Python](https://www.python.org/downloads/).
    1. Создайте веб-приложение App Engine. Используйте консольную команду ниже, заменив `[YOUR_PROJECT_ID]` на Projeсt ID вашего проекта:
        ```
        gcloud app create --project=[YOUR_PROJECT_ID]
        ```
        
    1. Выберите регион.
    1. Установите [Git](https://git-scm.com/).
    1. Выполните консольную команду `gcloud components install app-engine-python`.
    1. Скачайте или скопируйте исходный код примера из [GitHub-репозитория Яндекса](https://github.com/yandex/alice-skills/tree/master/python/buy-elephant/google-cloud).
    1. Перейдите в каталог приложения. Создайте виртуальную среду:
        
        {% cut "Windows" %}
        
        ```
        python -m venv env
        .\env\Scripts\activate
        ```
        
        {% endcut %}
        
        {% cut "MacOS" %}
        
        ```
        python3 -m venv env
        source env/bin/activate
        ```
        {% endcut %}
        
    1. Выполните команду `pip install -r requirements.txt`.
    1. Разверните приложение с помощью Google Cloud: выполните команду `gcloud app deploy`.
    1. Дождитесь окончания процесса, чтобы получить URL в строке `"target url": https://***.appspot.com`.

{% endlist %}

## Добавление Webhook URL {#webhook}

1. Перейдите в [консоль разработчика](https://dialogs.yandex.ru/developer/).
1. [Создайте навык](https://yandex.ru/dev/dialogs/alice/doc/ru/skill-create-console.md) и перейдите на вкладку **Настройки**.
1. В блоке **Backend** в поле **Webhook URL** укажите URL приложения.
1. Внизу страницы нажмите кнопку **Сохранить**.

Чтобы писать более сложные навыки, ознакомьтесь с [протоколом работы Яндекс Диалогов](https://yandex.ru/dev/dialogs/alice/doc/ru/protocol.md).

## Тестирование навыка {#testing}

Подробнее о [тестировании навыка](https://yandex.ru/dev/dialogs/alice/doc/ru/test.md).

{% list tabs %}

- Node.js

    1\. Проверьте работу навыка на вкладке **Тестирование**. Если все настроено правильно, появится приветствие: **Hello!**

    2\. Отправьте сообщение с любым текстом и убедитесь, что вам пришел ответ с таким же содержанием.

    3\. Попробуйте изменить код навыка. Откройте файл `app.js` в визуальном редакторе. Отредактируйте приветственную фразу: в тексте кода замените `'Hello!'` на `'Привет!'`.

    4\. Повторно разверните приложение с помощью консольной команды `gcloud app deploy`.

    5\. Обновите страницу на вкладке **Тестирование**. Проверьте изменения в навыке.

- Python

    1. Проверьте работу навыка на вкладке **Тестирование**. Если все настроено правильно, появится приветствие: **Привет! Купи слона!**

    1. Отправьте сообщение и убедитесь, что навык отвечает.

    1. Попробуйте изменить код навыка. Откройте файл `main.py` в визуальном редакторе. Отредактируйте приветственную фразу: замените в тексте кода `'Привет! Купи слона!'` на `'Добрый день! Не желаете купить слона?'` в тексте кода.

    1. Повторно разверните приложение с помощью консольной команды `gcloud app deploy`.
    
    1. Обновите страницу на вкладке **Тестирование**. Проверьте изменения в навыке.

{% endlist %}

Чтобы писать более сложные навыки, ознакомьтесь с [протоколом работы Яндекс Диалогов](https://yandex.ru/dev/dialogs/alice/doc/ru/protocol.md).

{% include [index-support-button](_includes/index/id-index/support-button-9f08997ea0f6.md) %}


