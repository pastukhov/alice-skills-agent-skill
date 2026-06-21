---
metadata:
  - name: generator
    content: Diplodoc Platform v5.39.1
alternate:
  - https://yandex.ru/dev/dialogs/alice/doc/ru/quickstart-visual-editors.md
---
# Без программирования

{% include notitle [neuroexpert-button](_includes/reusables/neuroexpert-button-99270fdba323.md) %}


## Создать навык в редакторе {#without-programming}

Создавайте навыки без программирования с помощью визуальных редакторов. С Алисой совместимы, например, [Aimylogic](https://app.aimylogic.com/), [Verter](https://app.verter.online/), [Pipe.bot](https://ru.pipe.bot/).

{% list tabs %}

- Создать навык в конструкторе Aimylogic

    <div style="
    border:1px solid #d1d5db;
    border-radius:20px;
    overflow:hidden;
    max-width:100%;
">
  <iframe src="https://runtime.strm.yandex.ru/player/video/vplvsvkwanftvnqcfzq3?autoplay=0&mute=0"
    frameborder="0"
    allowfullscreen
    style="
      display:block;
      width:100%;
      height:360px;
      "></iframe>
</div>

- Создать навык без программирования

    <div style="
    border:1px solid #d1d5db;
    border-radius:20px;
    overflow:hidden;
    max-width:100%;
">
  <iframe src="https://runtime.strm.yandex.ru/player/video/vplv2iwplezabnvy6zmi?autoplay=0&mute=0"
    frameborder="0"
    allowfullscreen
    style="
      display:block;
      width:100%;
      height:360px;
      "></iframe>
</div>

{% endlist %}

## Основные понятия {#basic-concepts}

- **Экран** — состояние бота, в котором он совершает действие или ряд действий.
- **Блок** — действие, которое совершает бот.
- **Интент** — блок, который дает понять боту, чего хочет пользователь.
- **Вопрос** — блок, который содержит в себе вопрос бота к пользователю.
- **Связь экранов** соединяет действия бота между собой в необходимой последовательности.

## Создание сценария {#create-skill}

1. Авторизуйтесь на [app.aimylogic.com](https://app.aimylogic.com/).
1. На главной странице Aimylogic нажмите **Создать бота**.
1. Выберите способ создания чат-бота в конструкторе.
1. Выберите язык общения и шаблон бота.
1. Введите название проекта и нажмите **В конструктор**.
1. Создайте экраны и разбейте их на блоки. Начните навык с приветствия.
1. Проставьте связи между экранами.
1. Когда сценарий будет готов, на верхней панели нажмите **Тестировать**. В открывшемся справа виджете проверьте работу навыка.

## Подключить навык к Яндекс Диалогам {#connect-skill}

1. На верхней панели конструктора нажмите кнопку **Опубликовать**.
1. Выберите канал **Алиса**.
1. Получите OAuth-токен, вставьте его в соответствующее поле и нажмите **Подключить**.
1. В списке подключений найдите канал **Алиса** и нажмите **Получить webhook**.
1. При создании навыка в [консоли разработчика](https://dialogs.yandex.ru/developer/) в блоке **Backend** выберите **Webhook URL**. Вставьте ссылку, полученную на шаге 4.
1. На вкладке **Тестирование** в консоли разработчика еще раз проверьте работу навыка перед публикацией.

{% include [index-support-button](_includes/index/id-index/support-button-d16778b15122.md) %}


