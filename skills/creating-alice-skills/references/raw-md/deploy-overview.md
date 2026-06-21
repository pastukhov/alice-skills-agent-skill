---
metadata:
  - name: generator
    content: Diplodoc Platform v5.39.1
alternate:
  - https://yandex.ru/dev/dialogs/alice/doc/ru/deploy-overview.md
---
# Подготовка сервера с навыком

{% include notitle [neuroexpert-button](_includes/reusables/neuroexpert-button-99270fdba323.md) %}


Навык сначала надо где-то разместить. В этом разделе собраны инструкции для некоторых способов:

- [В Yandex Cloud](https://yandex.ru/dev/dialogs/alice/doc/ru/deploy-ycloud-function.md) — простой и бесплатный способ.
- [В Vercel](https://yandex.ru/dev/dialogs/alice/doc/ru/deploy-vercel.md).
- [В Microsoft Azure](https://yandex.ru/dev/dialogs/alice/doc/ru/deploy-azure.md).
- [В Google Cloud](https://yandex.ru/dev/dialogs/alice/doc/ru/deploy-google-cloud.md).
- [В Amazon Web Services](https://yandex.ru/dev/dialogs/alice/doc/ru/deploy-aws.md).
- [На своем сервере](https://yandex.ru/dev/dialogs/alice/doc/ru/deploy-server.md).

## Не знаете, что выбрать? {#what-to-choose}

Посмотрите таблицы со сравнением этих и других способов.

{% cut "Функция в Yandex Cloud — поддержка облачных сервисов и бессерверных (serverless) приложений" %}

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
Cloud Functions, которые вы используете для навыков Алисы, бесплатны и не тарифицируются.

В остальных случаях см. [тарификацию ресурсов Yandex Cloud](https://cloud.yandex.ru/docs/compute/pricing).
|
Обязательна.

В консоли Диалогов в параметре **Backend** отображаются функции, которые вы имеете право просматривать.

Но навык будет работать, только если ваш аккаунт может запускать выбранную функцию.

Разрешение на запуск входит в роли Yandex Cloud serverless-functions-invoker, [editor](https://cloud.yandex.ru/docs/functions/security/#editor) и выше.
|
Возможна.

Назначайте другим пользователям [роли для доступа](https://cloud.yandex.ru/docs/functions/security) к функции.
|
Node.js, Python, Go, Java, .NET Core, PHP, R, Bash
||
|#

{% endcut %}

{% cut "Сервисы с поддержкой Webhook" %}

**Веб-приложение в [Firebase](https://firebase.google.com)**

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
Бесплатный план содержит 10 ГБ дискового пространства, 360 МБ трафика в день и поддерживает до 100 одновременных подключений.

Подробнее см. в [тарификации Firebase](https://firebase.google.com/pricing).
|
Не обязательна.

Вы можете интегрировать аккаунт с [Google Cloud Platform](https://firebase.google.com/docs/storage/gcp-integration) и [GitHub](https://firebase.google.com/docs/hosting/github-integration).
|
Возможна.

Назначайте роли для доступа к проекту, используя политику [Identity & Access Management (IAM)](https://firebase.google.com/docs/projects/iam/permissions).
|
Node.js, Java, C#, Go, Python
||
|#

**Проект в [Vercel](https://vercel.com)**

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
Бесплатный план содержит 100 ГБ дискового пространства, 100 ГБ ежемесячного трафика и неограниченное количество проектов.
|
Обязательна.

Необходимо привязать аккаунт [GitHub](https://vercel.com/docs/git/vercel-for-github), [GitLab](https://vercel.com/docs/git/vercel-for-gitlab) или [Bitbucket](https://vercel.com/docs/git/vercel-for-bitbucket).
|
Возможна в платной версии.

Подробнее см. [документацию Vercel](https://vercel.com/docs/platform/users-and-teams).
|
Node.js, Go, Python, Ruby
||
|#

{% endcut %}

{% cut "Сервисы с поддержкой Webhook и облачных сервисов" %}

**Виртуальная машина в [Yandex Cloud](https://cloud.yandex.ru/)**

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
Пробный период включает [стартовый грант](https://cloud.yandex.ru/docs/free-trial) на 60 дней.

В остальных случаях см. [тарификацию ресурсов Yandex Cloud](https://cloud.yandex.ru/docs/compute/pricing).
|
Не обязательна.

Вы можете создать [сервисный аккаунт](https://cloud.yandex.ru/docs/iam/concepts/users/service-accounts). Это позволит гибко настраивать права доступа к ресурсам Yandex Cloud.
|
Возможна.

Назначайте другим пользователям [права доступа](https://cloud.yandex.ru/docs/compute/security).
|
Поддерживаются операционные системы на базе Linux и Windows. Среды выполнения — без ограничений.
||

|#

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

**Виртуальная машина или веб-приложение в [Amazon Web Services](https://aws.amazon.com/ru)**

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
[Уровень бесплатного использования](https://aws.amazon.com/ru/free/) длится 12 месяцев.

Подробнее см. [тарификацию сервисов AWS](https://aws.amazon.com/ru/pricing).

Все бесплатные сервисы ограничены по ресурсам: 750 часов вычислений на виртуальных машинах в месяц.
|
Не обязательна
|
Возможна.

Настройте доступ пользователей в сервисе [Identity & Access Management (IAM)](https://aws.amazon.com/ru/iam).
|
Поддерживаются операционные системы на базе Linux и Windows.

Среды выполнения: Node.js, Python, Go, Java, .NET Core, PHP, Ruby.
||

|#

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

{% endcut %}

## Не нашли свой способ? {#common-steps}

Разместить навык можно на любом сервере. Работает это так:

1. Создайте сервер, который ожидает запросы с помощью вебхука.
1. Укажите ссылку на ваш сервер (Webhook URL) при создании навыка в консоли.
1. Когда пользователь запускает навык или что-то делает в нем, платформа Диалогов передает эти запросы на ваш сервер по указанной ссылке. Формат запросов и ответов — в [справочнике API](https://yandex.ru/dev/dialogs/alice/doc/ru/protocol.md).

Как попробовать:

1. Скачайте или скопируйте исходный код примера из [GitHub-репозитория Яндекса](https://github.com/yandex/alice-skills).
1. Разместите его привычным для вас способом.
1. Получите Webhook URL, на который платформа Диалогов будет отправлять запросы.
1. Создайте навык в консоли и укажите в нем ваш Webhook URL.


{% note tip %}

[Напишите нам](https://yandex.ru/dev/dialogs/alice/doc/ru/feedback.md), какой инструкции вам не хватает в документации. Если у вас есть готовый пример, приложите его. Так вы поможете другим пользователям Диалогов и сделаете Алису еще лучше.

{% endnote %}


{% include [index-support-button](_includes/index/id-index/support-button-caba7f6a075f.md) %}


