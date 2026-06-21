---
metadata:
  - name: generator
    content: Diplodoc Platform v5.39.1
alternate:
  - https://yandex.ru/dev/dialogs/alice/doc/ru/checklist.md
---
<style scoped>
    .grid-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
        gap: 30px;
        margin-bottom: 40px;
    }
    .grid-item {
        display: flex;
        flex-direction: column;
    }
</style>

# Проверка идеи

{% include notitle [neuroexpert-button](_includes/reusables/neuroexpert-button-99270fdba323.md) %}


Пользователь ожидает, что общение с персонажем навыка будет понятным, легким и полезным, похожим на диалог двух людей. Навык, который перегружает пользователя
 информацией, не будет востребован.

Воспользуйтесь чеклистом для оценки навыка еще на этапе идеи, чтобы убедиться, что он подходит для голосового формата. Если идея соответствует минимум трем из пяти
 перечисленных критериев, она успешна, и можно приступать к созданию навыка.


## <svg width="35" height="35" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg"><rect width="100" height="100" fill="white"/><path d="M90 75.9097C90 83.6916 83.6916 90 75.9097 90L24.0903 90C16.3085 90 10 83.6916 10 75.9097L10 12.1677C10 10.9705 10.9705 10 12.1677 10L75.9097 10C83.6916 10 90 16.3085 90 24.0903L90 75.9097Z" fill="#EBFAEF"/><path d="M19.5932 80.4068C2.80134 63.6149 2.80239 36.3888 19.5956 19.5956C36.3888 2.80239 63.6149 2.80134 80.4068 19.5932C97.1987 36.3851 97.1976 63.6112 80.4044 80.4044C63.6112 97.1976 36.3851 97.1987 19.5932 80.4068Z" stroke="#8AD29D" stroke-width="3"/><path d="M33.0273 47.9438L45.6252 60.5415L66.5029 38.6848" stroke="#8AD29D" stroke-width="3" stroke-miterlimit="79.8403" stroke-linecap="round" stroke-linejoin="round"/></svg> Естественность общения {#natural}

Использование навыка будет похоже на обычную беседу двух людей.

<div class="grid-container">
    <div class="grid-item">
        <p><img src="https://yastatic.net/s3/doc-binary/src/dev/dialogs/ru/like-dialogi.svg"/> <b>Хороший пример</b></p>
        <p><b>Пользователь</b>: <em>Алиса, какая погода?</em></p>
        <p><b>Алиса</b>: <em>Сейчас в городе Москва пасмурно. Градусник показывает +11°C, а ощущается как +10°C.</em></p>
        <p><b>Пользователь</b>: <em>Сколько ехать до дома?</em></p>
        <p><b>Алиса</b>: <em>Осталось ехать 24 минуты.</em></p>
    </div>
    <div class="grid-item">
        <p><img src="https://yastatic.net/s3/doc-binary/src/dev/dialogs/ru/dislike-dialogi.svg"/> <b>Плохой пример</b></p>
        <p><b>Пользователь</b>: <em>Алиса, расписание электричек Москва.</em></p>
        <p><b>Алиса</b>: <em>В какой город вы хотите уехать?</em></p>
    </div>
</div>
<div class="grid-container">
    <div class="grid-item">
        <p><b>Объяснение</b>: Можно спросить друга о погоде или водителя такси о времени в пути до дома.</p>
    </div>
    <div class="grid-item">
        <p><b>Объяснение</b>: Это запрос для поисковой строки, а не к человеку. Будет сложно воспринять на слух все возможные варианты ответа.</p>
    </div>
</div>


## <svg width="35" height="35" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg"><rect width="100" height="100" fill="white"/><path d="M90 75.9097C90 83.6916 83.6916 90 75.9097 90L24.0903 90C16.3085 90 10 83.6916 10 75.9097L10 12.1677C10 10.9705 10.9705 10 12.1677 10L75.9097 10C83.6916 10 90 16.3085 90 24.0903L90 75.9097Z" fill="#EBFAEF"/><path d="M19.5932 80.4068C2.80134 63.6149 2.80239 36.3888 19.5956 19.5956C36.3888 2.80239 63.6149 2.80134 80.4068 19.5932C97.1987 36.3851 97.1976 63.6112 80.4044 80.4044C63.6112 97.1976 36.3851 97.1987 19.5932 80.4068Z" stroke="#8AD29D" stroke-width="3"/><path d="M33.0273 47.9438L45.6252 60.5415L66.5029 38.6848" stroke="#8AD29D" stroke-width="3" stroke-miterlimit="79.8403" stroke-linecap="round" stroke-linejoin="round"/></svg> Минимум уточнений {#no-questions}

Важно, чтобы персонаж навыка делал минимум уточнений и мог сразу дать ответ. Уточняющие вопросы стоит задавать, 
 только когда нам не хватает информации для хорошего ответа. Их количество зависит от типа сценария и контекста. 
 Например, если сценарий затрагивает траты пользователя, то лучше добавить больше уточнений, чтобы исключить ошибки. 
 А при запросе на включение музыки можно сразу дать ответ.

<div class="grid-container">
    <div class="grid-item">
        <p><img src="https://yastatic.net/s3/doc-binary/src/dev/dialogs/ru/like-dialogi.svg"/> <b>Хороший пример</b></p>
        <p><b>Пользователь</b>: <em>Алиса, включи музыку.</em></p>
        <p><b>Алиса</b>: <em>Включаю.</em></p>
    </div>
    <div class="grid-item">
        <p><img src="https://yastatic.net/s3/doc-binary/src/dev/dialogs/ru/dislike-dialogi.svg"/> <b>Плохой пример</b></p>
        <p><b>Пользователь</b>: <em>Алиса, фильмы 2020 года.</em></p>
        <p><b>Алиса</b>: <em>А какой жанр?</em></p>
        <p><b>Пользователь</b>: <em>Комедии.</em></p>
        <p><b>Алиса</b>: <em>А какого режиссера хотелось бы увидеть?</em></p>
    </div>
</div>

## <svg width="35" height="35" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg"><rect width="100" height="100" fill="white"/><path d="M90 75.9097C90 83.6916 83.6916 90 75.9097 90L24.0903 90C16.3085 90 10 83.6916 10 75.9097L10 12.1677C10 10.9705 10.9705 10 12.1677 10L75.9097 10C83.6916 10 90 16.3085 90 24.0903L90 75.9097Z" fill="#EBFAEF"/><path d="M19.5932 80.4068C2.80134 63.6149 2.80239 36.3888 19.5956 19.5956C36.3888 2.80239 63.6149 2.80134 80.4068 19.5932C97.1987 36.3851 97.1976 63.6112 80.4044 80.4044C63.6112 97.1976 36.3851 97.1987 19.5932 80.4068Z" stroke="#8AD29D" stroke-width="3"/><path d="M33.0273 47.9438L45.6252 60.5415L66.5029 38.6848" stroke="#8AD29D" stroke-width="3" stroke-miterlimit="79.8403" stroke-linecap="round" stroke-linejoin="round"/></svg> Сложная навигация {#complex-navigation}

В графическом интерфейсе для достижения целевого действия нужно выполнить несколько шагов, поэтому проще воспользоваться голосом.

Голосовой сценарий не должен полностью дублировать длинный путь экранного сценария.

<div class="grid-container">
    <div class="grid-item">
        <p><img src="https://yastatic.net/s3/doc-binary/src/dev/dialogs/ru/like-dialogi.svg"/> <b>Хороший пример</b></p>
        <p><b>Пользователь</b>: <em>Алиса, включи Буратино на ЛитРес.</em></p>
        <p><b>Алиса</b>: <em>Включаю.</em></p>
    </div>
    <div class="grid-item">
        <p><img src="https://yastatic.net/s3/doc-binary/src/dev/dialogs/ru/dislike-dialogi.svg"/> <b>Плохой пример</b></p>
        <p><b>Пользователь</b>: <em>Алиса, купи билеты на фильм «Довод».</em></p>
        <p><b>Алиса</b>: <em>Скажите, в каком кинотеатре вы хотите посмотреть этот фильм?</em></p>
        <p><b>Пользователь</b>: <em>Недалеко от дома.</em></p>
        <p><b>Алиса</b>: <em>Нашла рядом с вами несколько кинотеатров.</em></p>
    </div>
</div>
<div class="grid-container">
    <div class="grid-item">
        <p><b>Объяснение</b>: Навык поможет выполнить целевое действие с помощью одной фразы вместо целого ряда последовательных команд. Например, с помощью данного примера вы одновременно запустите навык, воспользуетесь поиском онлайн-библиотеки и воспроизведете аудиокнигу.</p>
    </div>
    <div class="grid-item">
        <p><b>Объяснение</b>: Выполнение целевого действия разбито на ряд дополнительных команд, которые отнимают время пользователя.</p>
    </div>
</div>

## <svg width="35" height="35" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg"><rect width="100" height="100" fill="white"/><path d="M90 75.9097C90 83.6916 83.6916 90 75.9097 90L24.0903 90C16.3085 90 10 83.6916 10 75.9097L10 12.1677C10 10.9705 10.9705 10 12.1677 10L75.9097 10C83.6916 10 90 16.3085 90 24.0903L90 75.9097Z" fill="#EBFAEF"/><path d="M19.5932 80.4068C2.80134 63.6149 2.80239 36.3888 19.5956 19.5956C36.3888 2.80239 63.6149 2.80134 80.4068 19.5932C97.1987 36.3851 97.1976 63.6112 80.4044 80.4044C63.6112 97.1976 36.3851 97.1987 19.5932 80.4068Z" stroke="#8AD29D" stroke-width="3"/><path d="M33.0273 47.9438L45.6252 60.5415L66.5029 38.6848" stroke="#8AD29D" stroke-width="3" stroke-miterlimit="79.8403" stroke-linecap="round" stroke-linejoin="round"/></svg> Удобнее голосом {#interface}

Некоторые функции сложно найти в графическом интерфейсе, поэтому удобнее управлять ими с помощью голоса.

<div class="grid-container">
    <div class="grid-item">
        <p><img src="https://yastatic.net/s3/doc-binary/src/dev/dialogs/ru/like-dialogi.svg"/> <b>Хороший пример</b></p>
        <p><b>Пользователь</b>: <em>Алиса, включи определитель номера.</em></p>
        <p><b>Алиса</b>: <em>Включаю.</em></p>
    </div>
</div>
<div class="grid-container">
    <div class="grid-item">
        <p><b>Объяснение</b>: Проще произнести эту команду, чем искать функцию в настройках телефона.</p>
    </div>
</div>

## <svg width="35" height="35" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg"><rect width="100" height="100" fill="white"/><path d="M90 75.9097C90 83.6916 83.6916 90 75.9097 90L24.0903 90C16.3085 90 10 83.6916 10 75.9097L10 12.1677C10 10.9705 10.9705 10 12.1677 10L75.9097 10C83.6916 10 90 16.3085 90 24.0903L90 75.9097Z" fill="#EBFAEF"/><path d="M19.5932 80.4068C2.80134 63.6149 2.80239 36.3888 19.5956 19.5956C36.3888 2.80239 63.6149 2.80134 80.4068 19.5932C97.1987 36.3851 97.1976 63.6112 80.4044 80.4044C63.6112 97.1976 36.3851 97.1987 19.5932 80.4068Z" stroke="#8AD29D" stroke-width="3"/><path d="M33.0273 47.9438L45.6252 60.5415L66.5029 38.6848" stroke="#8AD29D" stroke-width="3" stroke-miterlimit="79.8403" stroke-linecap="round" stroke-linejoin="round"/></svg> Только голос {#only-voice}

Реализовать целевое действие можно только с помощью голоса. Отсутствие интерфейса не испортит пользовательский опыт.

<div class="grid-container">
    <div class="grid-item">
        <p><img src="https://yastatic.net/s3/doc-binary/src/dev/dialogs/ru/like-dialogi.svg"/> <b>Хороший пример</b></p>
        <p><b>Пользователь</b>: <em>Алиса, вызови такси до работы.</em></p>
        <p><b>Алиса</b>: <em>Какой тариф выбираем?</em></p>
        <p><b>Пользователь</b>: <em>Комфорт.</em></p>
        <p><b>Алиса</b>: <em>Вызываю.</em></p>
    </div>
    <div class="grid-item">
        <p><img src="https://yastatic.net/s3/doc-binary/src/dev/dialogs/ru/dislike-dialogi.svg"/> <b>Плохой пример</b></p>
        <p><b>Пользователь</b>: <em>Алиса, помоги купить платье.</em></p>
        <p><b>Алиса</b>: <em>Платье какого цвета вы бы хотели?</em></p>
    </div>
</div>
<div class="grid-container">
    <div class="grid-item">
        <p><b>Объяснение</b>: Адрес и другие детали поездки пользователь может сообщить голосом.</p>
    </div>
    <div class="grid-item">
        <p><b>Объяснение</b>: В данном случае необходим графический интерфейс, чтобы посмотреть возможные цвета, фасоны и т. д.</p>
    </div>
</div>


**Следующий шаг** → [Цели и аудитория навыка](https://yandex.ru/dev/dialogs/alice/doc/ru/preparation.md)

{% include [index-support-button](_includes/index/id-index/support-button-d2c7232954b9.md) %}


