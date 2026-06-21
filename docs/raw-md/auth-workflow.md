---
metadata:
  - name: generator
    content: Diplodoc Platform v5.39.1
alternate:
  - https://yandex.ru/dev/dialogs/alice/doc/ru/auth/workflow.md
---
# Порядок работы

{% include notitle [neuroexpert-button](../_includes/reusables/neuroexpert-button-99270fdba323.md) %}


В этом разделе описан общий порядок действий по добавлению авторизации в навыке и даны ссылки на необходимые инструкции.

Чтобы добавить авторизацию в навыке:

1. [Настройте авторизационный сервер](https://yandex.ru/dev/dialogs/alice/doc/ru/auth/create-server.md). Он должен работать в соответствии с [RFC](https://tools.ietf.org/html/rfc6749) и обрабатывать обязательные параметры.
1. [Дополните навык](https://yandex.ru/dev/dialogs/alice/doc/ru/auth/make-skill.md). Добавьте дополнительные проверки и ответьте пользователю.
1. [Добавьте связку аккаунтов в консоли разработчика](https://yandex.ru/dev/dialogs/alice/doc/ru/auth/add-skill-to-console.md). Укажите параметры авторизационного сервера на странице навыка.
1. [Протестируйте навык](https://yandex.ru/dev/dialogs/alice/doc/ru/auth/test-skill.md). Проверьте, как работает авторизация в консоли разработчика.
1. [Отправьте навык на модерацию](https://yandex.ru/dev/dialogs/alice/doc/ru/auth/send-to-moderation.md).

