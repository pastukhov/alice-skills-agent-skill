---
metadata:
  - name: generator
    content: Diplodoc Platform v5.39.1
alternate:
  - https://yandex.ru/dev/dialogs/alice/doc/ru/guides-and-examples.md
---
# Полезные ссылки

{% include notitle [neuroexpert-button](_includes/reusables/neuroexpert-button-99270fdba323.md) %}


На этой странице собраны полезные ресурсы для работы с платформой [Яндекс Диалоги](https://dialogs.yandex.ru/).

## Основное {#main}

- [NewAliceSkills](https://t.me/NewAliceSkills) — каталог новых навыков.
- [YaDialogsNews](https://t.me/yadialogsnews) — новости Яндекс Диалогов.
- [Telegram-сообщество разработчиков навыков Алисы](https://t.me/yadialogschat) — итоги программы поощрения и премии Алисы.


## Визуальные конструкторы {#visual}

Конструкторы — это сервисы, которые помогают проектировать и создавать навыки без программирования. Несколько примеров:

- [aimylogic](https://aimylogic.com/ru/skills) — универсальный конструктор навыков для всех голосовых ассистентов;
    
- [verter.online](https://www.verter.online) — полностью бесплатный сервис для создания навыков Алисы;
    
- [pipe.bot](https://pipe.bot) — конструктор чат-ботов с поддержкой Алисы;
    
- [fabble.io](https://fabble.io) — инструмент помогает проектировать и прототипировать навыки.
    


## SDK и Open-source проекты {#sdk}

Открытые SDK от сообщества разработчиков, шаблоны навыков и open-source проекты, которые помогут начать разработку навыков:

{% list tabs %}

- JS/TS

    - [fletcherist/yandex-dialogs-sdk](https://github.com/fletcherist/yandex-dialogs-sdk);
        
    - [skoif/Yandex-Dialogs](https://github.com/skoif/Yandex-Dialogs);
        
    - [vitalets/alice-renderer](https://github.com/vitalets/alice-renderer) — библиотека для формирования ответов в навыках Алисы;
        
    - [vitalets/alice-types](https://github.com/vitalets/alice-types) — тайпинги для протокола запросов/ответов в навыках Алисы.
        

    Шаблоны навыков:

    - Пример на TypeScript: [sameoldmadness/alice-ts](https://github.com/sameoldmadness/alice-ts);
        
    - Быстрый старт навыка на Node.js: [vitalets/alice-skill-starter](https://github.com/vitalets/alice-skill-starter).
        

    Open-source навыки:

    - [popstas/yandex-dialogs-whatis](https://github.com/popstas/yandex-dialogs-whatis) — навык «Вторая память» на [fletcherist/yandex-dialogs-sdk](https://github.com/fletcherist/yandex-dialogs-sdk).

- Python

    - [Dikower/Alice_SeaBattle_YandexHackathone](https://github.com/Dikower/Alice_SeaBattle_YandexHackathone/blob/master/alice_sdk.py);
        
    - [mahenzon/aioAlice](https://github.com/mahenzon/aioalice) — асинхронная библиотека для взаимодействия с Алисой на Python 3.6+;
        
    - [borzunov/alice_scripts](https://github.com/borzunov/alice_scripts) — библиотека позволяет писать многоэтапные сценарии без callback-ов и ручного хранения информации о состоянии диалога;
        
    - [dialogic](https://github.com/avidale/dialogic) — общая обертка для навыков в Алисе, ботов в Telegram на Python 3.6+;
        
    - [format37/alice](https://github.com/format37/alice) — сокращенный пример aiohttp-сервера;
        
    - [itookyourboo/BaseSkill](https://github.com/itookyourboo/BaseSkill) — фреймворк для разработки навыков Алисы на Python;

    - [K1rL3s/aliceio](https://github.com/K1rL3s/aliceio) — фреймворк для разработки навыков на Python 3.8+.
        

    Шаблоны навыков:

    - Примеры на Python + aioAlice: [surik00/aioAlice](https://github.com/surik00/aioalice/tree/master/examples);
        
    - Примеры на Python + alice_scripts: [borzunov/alice_scripts](https://github.com/borzunov/alice_scripts#Примеры);
        
    - [alice-skills/show-template](https://github.com/yandex/alice-skills/tree/master/python/show-template) — шаблон навыка с поддержкой Утреннего шоу;
        
    - [avidale/synonym-skill](https://github.com/avidale/synonym-skill) — шаблон навыка, который подсказывает синонимы к слову;
        
    - [peleccom/chat_gpt_yandex_alice](https://github.com/peleccom/chat_gpt_yandex_alice) — шаблон навыка с использованием GhatGPT.
        

    Open-source навыки:

    - [demo-alice-translate-skill](https://github.com/avidale/demo-alice-translate-skill) — навык [Крот-полиглот](https://dialogs.yandex.ru/store/skills/622af903-krot-poliglot) на Python с использованием встроенных интентов, хранилища состояния и связки с API Яндекс Переводчика;
    - [StopChangingTheName/alice-skills](https://github.com/StopChangingTheName/alice-skills) — навык [Знатоки истории](https://dialogs.yandex.ru/store/skills/1424e7f5-ege-po-istorii);
    - [let-robots-reign/RussianHistory_Quiz](https://github.com/let-robots-reign/RussianHistory_Quiz) — навык «Викторина по истории России»;
    - [vb64/bulls_cows](https://github.com/vb64/bulls_cows) — навык [Бычки и коровки](https://alice.ya.ru/s/59166701-101b-44b3-b7e3-b7e078036890) на Python/Flask и [Google App Engine](https://cloud.google.com/appengine).

- PHP

    - [mesilov/yandex-dialogs-php-sdk](https://github.com/mesilov/yandex-dialogs-php-sdk.git);
        
    - [jeyroik/alice-extas](https://github.com/jeyroik/alice-extas);
        
    - [jeyroik/php-yandex-alisa-advanced](https://github.com/jeyroik/php-yandex-alisa-advanced);
        
    - [Danil005/php-yandex-alisa](https://github.com/Danil005/php-yandex-alisa);
        
    - [thesoultaker48/yandex-dialogs-php](https://github.com/thesoultaker48/yandex-dialogs-php);
        
    - [zz-anton/ru.foralice.yandex-dialogs-api-hide-my-oauth](https://github.com/zz-anton/ru.foralice.yandex-dialogs-api-hide-my-oauth) — PHP-скрипт для работы сервиса [ImgAdmin](https://imgAdmin.forAlice.ru) с использованием OAuth идентификатора пользователя.
        

    Шаблоны навыков:

    - [AlexSuperStar/Yandex-Alisa-PHP-Example](https://github.com/AlexSuperStar/Yandex-Alisa-PHP-Example);
        
    - [jeyroik/php-yandex-alisa-simple](https://github.com/jeyroik/php-yandex-alisa-simple);
        
    - [artlux/alicebotoauth](https://github.com/artlux/alicebotoauth/blob/master/auth_yandex.php);
        
    - Приватный навык на PHP для управления брокерским счетом через [Тинькофф Инвестиции OpenAPI](https://github.com/TinkoffCreditSystems/invest-openapi): [denismosolov/oliver](https://github.com/denismosolov/oliver).
        

- Go

    - [toby3d/dialogs](https://github.com/toby3d/dialogs);
        
    - [bbrodriges/mielofon](https://github.com/bbrodriges/mielofon);
        
    - [AlekSi/alice](https://github.com/AlekSi/alice);
        
    - [azzzak/alice](https://github.com/azzzak/alice).
        

    Open-source навыки:

    - [ShoshinNikita/radio-t-bot](https://github.com/ShoshinNikita/radio-t-bot) — навык «Радио-Т».

- Kotlin

    - [SavinMike/alice-kotlin-bot](https://github.com/SavinMike/alice-kotlin-bot);
        
    - [Just AI Conversational Framework](https://github.com/just-ai/jaicf-kotlin/tree/master/channels/yandex-alice);
        
    - [alice/kotlin](https://github.com/yandex-cloud/examples/tree/master/serverless/functions/alice/kotlin) — шаблон навыка на JAICF для запуска в Yandex Cloud;
        
    - [morfeusys/profit-skill](https://github.com/morfeusys/profit-skill);

    - [danbeldev/alice-ktx](https://github.com/danbeldev/alice-ktx) — [фреймворк](https://danbeldev.github.io/alice-ktx/) на Kotlin с DSL для быстрого создания навыков Алисы.


    Шаблонный проект на Kotlin: [alice-jaicf-template](https://github.com/just-ai/alice-jaicf-template).

- C#

    - [alexvolchetsky/yandex.alice.sdk](https://github.com/alexvolchetsky/yandex.alice.sdk);
        
    - [granstel/Yandex Dialogs.Models](https://github.com/granstel/Yandex.Dialogs.Models).
        

    Шаблоны навыков:

    - Пример на С# и .NET Core: [seralexeev/alice-dotnet](https://github.com/seralexeev/alice-dotnet);
        
    - Шаблонный проект на C# (Алиса, Telegram, Chat2Desk): [granstel/Templates.Chatbot](https://github.com/granstel/Templates.Chatbot);
        
    - Пример навыка на C# для изучения программистского английского: [xoposhiy/prog-eng-alice](https://github.com/xoposhiy/prog-eng-alice).
        

    Open-source навыки:

    - [DenisNP/AliceHook](https://github.com/DenisNP/AliceHook) — навык [Колдун хочу](https://dialogs.yandex.ru/store/skills/85384c00-moj-ispolnitel);
    - [xoposhiy/prog-eng-alice](https://github.com/xoposhiy/prog-eng-alice) – навык Алисы для изучения программистского английского;
    - [granstel/FillInTheTextBot](https://github.com/granstel/FillInTheTextBot) — навык [Занимательные истории](https://dialogs.yandex.ru/store/skills/12ef2083-sochinyal);

{% endlist %}

Другие примеры навыков для быстрого старта смотрите в официальном репозитории [yandex/alice-skills](https://github.com/yandex/alice-skills) и [каталоге навыков](https://dialogs.yandex.ru/store/skills).


## Тестирование навыков {#testing}

Open-source библиотеки для автоматического тестирования навыков:

- [yandex-dialogs-client](https://github.com/popstas/yandex-dialogs-client) — примеры автотестов;
- [alice-nearby](https://github.com/azzzak/alice-nearby) — утилита с веб-интерфейсом для локального тестирования;
- [Эмулятор Алисы](https://github.com/vb64/test.helper.yandex.alice.flask) — для юнит-тестов навыков, реализованных как приложение Python/Flask;
- [alice-tester](https://github.com/vitalets/alice-tester) — библиотека для автоматического тестирования навыков под Node.js;
- [alice-cloud-proxy](https://github.com/vitalets/alice-cloud-proxy) — облачная функция для проксирования запросов в основной **Webhook URL** навыка;
- [botank](https://github.com/avidale/botank) — библиотека для автоматического тестирования навыков Алисы на любых языках.


## Дополнительные библиотеки {#libraries}

- [DeepPavlov](https://deeppavlov.ai) ([обучающее видео](https://www.youtube.com/watch?v=L0lFGcmDQiU)) — библиотека для построения диалоговых систем;
- [alice-entities-library](https://github.com/denismosolov/alice-entities-library) — репозиторий сущностей, которые могут пригодиться при написании грамматики;
- Работа с изображениями:
    - [ImgAdmin](https://imgAdmin.forAlice.ru) — администратор изображений;
    - [alice-asset-manager](https://github.com/vitalets/alice-asset-manager) — Node.js API для загрузки изображений и звуков в навыки.
    
- Умный дом:
    - [popstas/yandex-dialogs-smarthome-mqtt](https://github.com/popstas/yandex-dialogs-smarthome-mqtt) — проект для подключения Умного дома к MQTT-устройствам;
    - [munrexio/yandex2mqtt](https://github.com/munrexio/yandex2mqtt) — мост из Умного дома в MQTT на Node.js;
    - [subnetsRU/alice-command-skill](https://github.com/subnetsRU/alice-command-skill) — пример навыка для Умного дома, который позволяет выполнять несколько сценариев за одну команду и по таймеру;
    - [devicegallery.ru](https://devicegallery.ru/) — каталог совместимых с Алисой устройств.
    


## Наши чаты в Telegram {#telegram-chat}

- [yadialogschat](https://t.me/yadialogschat) — сообщество для разработчиков Яндекс Диалогов;
- [station_yandex](https://t.me/station_yandex) — чат для пользователей Яндекс Станции, Умного дома и устройств с Алисой;
- [yandexflood](https://t.me/yandexflood) — неформальный чат для пользователей Яндекс Станции, сервисов Музыка и Диалоги;
- [yandexcloud_chat](https://t.me/yandexcloud_chat) — чат для вопросов о Yandex Cloud.


## Что еще? {#more}

- [yandexdb](https://t.me/yandexdb) — новостной канал про Яндекс Станцию, Умный дом и Алису;
    
- [yadialogsbot](https://t.me/yadialogsbot) — бот для мониторинга позиции навыка в каталоге;
    
- [База знаний Диалогов](https://wiki.yaboard.com/w/Категория:Диалоги) — статьи о платформе Яндекс Диалоги, а также инструкции и советы об использовании и написании своих навыков.

{% include [index-support-button](_includes/index/id-index/support-button-202f28ced5ac.md) %}


