---
metadata:
  - name: generator
    content: Diplodoc Platform v5.39.1
alternate:
  - https://yandex.ru/dev/dialogs/alice/doc/ru/deploy-server.md
---
# Размещение навыка на своем сервере

{% include notitle [neuroexpert-button](_includes/reusables/neuroexpert-button-99270fdba323.md) %}


Есть множество вариантов размещения навыка на собственном сервере. Пример навыка на Python адаптирован для размещения при помощи менеджера контейнеров [Dokku](https://dokku.com/).


{% note info %}

Помните, что для размещения навыка на собственном сервере у вас должен быть домен.

{% endnote %}


## Подготовка {#setup}

1. Установите Dokku одним из методов:
    
    - [простой метод установки](https://dokku.com/docs/getting-started/installation/);
    - [альтернативный метод установки](https://dokku.com/docs/getting-started/advanced-installation/#configuring).
    
    Для систем на Debian введите команду
    ```
    wget https://raw.githubusercontent.com/dokku/dokku/v0.26.8/bootstrap.sh;
    sudo DOKKU_TAG=v0.26.8 bash bootstrap.sh
    ```
    
    Установка длится 5–10 минут.
    
1. Установите SSH-ключ. Перед выполнением следующей команды убедитесь, что ключ уже доступен в файле `~/.ssh/authorized_keys`.
    ```
    cat ~/.ssh/authorized_keys | dokku ssh-keys:add admin
    ```
    
1. Настройте виртуальный хост. Вместо `example.com` укажите домен, к которому у вас есть доступ и который содержит `A record` или `CNAME`, указывающий на IP вашего сервера.
    ```
    dokku domains:set-global example.com
    ```
    
    Вы также можете использовать IP вашего сервера.
    
    ```
    dokku domains:set-global 10.0.0.2
    ```
    

## Размещение веб-приложения {#dockerfile}

Подробнее о размещении приложения читайте в [документации Dokku](https://dokku.com/docs/deployment/application-deployment/#deploying-to-dokku).

1. Разверните приложение. Скачайте или скопируйте исходный код примера из [GitHub-репозитория Яндекса](https://github.com/yandex/alice-skills/tree/master/python/buy-elephant/now). Для этого на вашем сервере должен быть включен SSH-доступ к github.
    ```
    git clone https://github.com/yandex/alice-skills/tree/master/python/buy-elephant/now
    ```
    
1. Соберите приложение.
    ```
    dokku apps:create buy-elephant
    ```
    
1. Создайте резервные службы. Dokku не предоставляет поддержку баз данных по умолчанию, но ее можно подключить при помощи [плагинов](https://dokku.com/docs/community/plugins/#official-plugins-beta). Для установки плагинов нужно сменить пользователя на root. Например, [Postgress](https://github.com/dokku/dokku-postgres):
    ```
    sudo dokku plugin:install https://github.com/dokku/dokku-postgres.git
    ```
    
    Создайте базу данных `mydatabase`:
    
    ```
    dokku postgres:create mydatabase
    ```
    
    После установки укажите базу данных в приложении:
    
    ```
    dokku postgres:link mydatabase buy-elephant
    ```
    
1. Разместите приложение.
    ```
    cd buy-elephant
    git remote add dokku dokku@example.com:buy-elephant
    git push dokku main:master
    ```
    
    Как только размещение завершится, будет сгенерирован URL приложения. Например:
    
    ```
    =====> Application deployed:
    http://buy-elephant.example.com
    ```
    
1. Чтобы поддержать https-запросы, надо импортировать SSL-сертификаты из плагина Dokku.
    ```
    dokku certs:add buy-elephant server.crt server.key
    ```
    

## Добавление Webhook URL {#webhook}

1. Перейдите в [консоль разработчика навыка](https://dialogs.yandex.ru/developer/).
1. Откройте вкладку **Настройки**.
1. В блоке **Backend** в поле **Webhook URL** укажите URL приложения.
1. Внизу страницы нажмите кнопку **Сохранить**.
1. Проверьте работу навыка на вкладке **Тестирование**. Подробнее см. раздел [Тестирование навыка](https://yandex.ru/dev/dialogs/alice/doc/ru/test.md).

## Тестирование навыка {#testing}

Подробнее о [тестировании навыка](https://yandex.ru/dev/dialogs/alice/doc/ru/test.md).

1. Проверьте работу навыка на вкладке **Тестирование**. Если все настроено правильно, появится приветствие: **Привет! Купи слона!**
1. Отправьте сообщение и убедитесь, что навык отвечает.
1. Попробуйте изменить код навыка. Откройте файл `api.py` в визуальном редакторе. Отредактируйте приветственную фразу: в тексте кода замените `'Привет! Купи слона!'` на `'Добрый день! Не желаете купить слона?'`.
1. Повторно разверните приложение с помощью консольной команды:
    ```
    dokku ps:rebuild buy-elephant
    ```
    
1. Обновите страницу на вкладке **Тестирование**. Проверьте изменения в навыке.

{% include [deploy-azure-complex-skills](_includes/deploy-azure/id-deploy-azure/complex-skills-053193ffd2bb.md) %}


{% include [index-support-button](_includes/index/id-index/support-button-9fb99b828fa9.md) %}


