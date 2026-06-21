---
metadata:
  - name: generator
    content: Diplodoc Platform v5.39.1
alternate:
  - https://yandex.ru/dev/dialogs/alice/doc/ru/deploy-aws.md
---
# Размещение навыка в AWS

{% include notitle [neuroexpert-button](_includes/reusables/neuroexpert-button-99270fdba323.md) %}


Платформа [Amazon Web Services](https://aws.amazon.com/ru) позволяет развернуть и проверить свой навык. Если вы не пользовались платформой раньше, вы можете воспользоваться бесплатным периодом.

## Подготовка {#preparation}

Создайте [учетную запись AWS](https://aws.amazon.com/ru/free/), если у вас ее еще нет, и дождитесь активации сервиса (может занимать до 24 часов).

## Создание веб-приложения {#create}

Запустить свое приложение можно при помощи AWS Lambda или Elastic Beanstalk.

Способ с Elastic Beanstalk длиннее, поскольку требует настройки связи по протоколу HTTPS. Для этого потребуется действительный выданный сертификат.

{% list tabs %}

- Lambda

    1. Войдите в [Консоль управления AWS](https://aws.amazon.com/ru/console/).
    1. При помощи поиска найдите раздел **Lambda**.
    1. В верхнем правом углу нажмите **Create function**.
    1. Заполните поля:
        
        - **Function name** — имя функции.
        - **Runtime** — среда, в которой будет выполняться функция. Поддерживаются Node.js, Python и Ruby.
        - **Architecture** — архитектура, на которой будет выполняться функция. Выберите нужную опцию: **x86_64** или **arm64**.
        
    1. Откройте вкладку **Change default execution role**.
    1. Выберите опцию **Create a new role with basic Lambda permissions**.
    1. откройте вкладку **Advanced settings**.
    1. Выберите опцию **Enable function URL -raw**.
    1. В разделе **Auth type** выберите опцию **NONE**.
    1. Нажмите **Create function**.
    1. В открывшемся окне с описанием функции на вкладке **Functions overview** найдите **Function URL** — он потребуется для запуска навыка в [консоли разработчика Диалогов](https://dialogs.yandex.ru/developer/).
    1. В разделе **Code source** разместите исходный код вашего приложения. В некоторых средах выполнения изменения в код можно вносить прямо в этом разделе. Чтобы изменения вступили в силу, нажмите кнопку **Deploy**.
    1. Нажмите **Test**, чтобы начать тестирование приложения.

- Elastic Beanstalk

    1. Войдите в [Консоль управления AWS](https://aws.amazon.com/ru/console/).
    1. При помощи поиска найдите раздел **Elastic Beanstalk** и создайте окружение:
        
        1. В верхнем правом углу нажмите **Create a new environment**.
        1. В окне **Select environment tier** выберите опцию **Web server environment** и нажмите **Select**.
        1. В поле **Application name** введите название приложения.
        1. В разделе **Platform** выберите платформу для вашего приложения, а также его ветвь и версию.
        1. В разделе **Application code** выберите опцию **Upload your code**.
        1. Нажмите **Chose file** и загрузите архив с исходным кодом приложения.
        1. Нажмите **Create environment**.
        
    1. Найдите с помощью поиска страницу сервиса Route 53 и перейдите на нее.
    1. Создайте ресурсную запись типа А. Запись должна связывать ваше доменное имя и созданное окружение Elastic Beanstalk. Подробнее о создании такой записи читайте в [документации AWS](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/rrsets-working-with.html).
    1. С помощью поиска найдите раздел **EC2**.
        
    1. В подразделе **Load Balancers** выберите только что созданный балансировщик и перейдите в его свойство **Listeners**.
    1. Нажмите **Add listener** и измените следующие значения:
        - **Protocol** — протокол подключения. Выберите значение **HTTPS**.
        - **Port** — порт сети. Введите значение `443`.
        - **Default action Forward to...** — целевая группа из выпадающего списка.
        - **Security policy** — наиболее свежая политика безопасности.
        - **Default SSL certificate** — действительный сертификат для использованного в ресурсной записи доменного имени.
        
        Для регистрации доменных имен воспользуйтесь сервисом [Route 53](https://aws.amazon.com/route53/). Для получения сертификата используйте сервис [AWS Certificate Manager](https://aws.amazon.com/certificate-manager/).
    1. Нажмите **Add listener** еще раз и вернитесь в свойства балансировщика.
    1. Обратите внимание на желтый треугольник справа от **HTTPS**: **443** — это предупреждение о необходимости внести изменения в группу безопасности. Нажмите на него и перейдите к списку групп.
        
        1. Для каждой группы по очереди выберите вкладку **Inbound rules** и нажмите кнопку **Edit inbound rules**.
        1. Добавьте правило для **HTTPS**, указывая в поле **Source** то же значение, что и для **HTTP**.
        
    1. В новой вкладке браузера введите доменное имя, которое вы использовали в ресурсной записи, и перейдите по ссылке. На странице будет указан ответ навыка на HTTP-запрос GET.

{% endlist %}

## Добавление Webhook URL {#register}

{% include [deploy-server-webhook-common](_includes/deploy-server/id-deploy-server/webhook-common-6a9ce0def96b.md) %}


{% include [index-support-button](_includes/index/id-index/support-button-b70eef76e966.md) %}


