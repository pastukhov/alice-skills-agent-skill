---
metadata:
  - name: generator
    content: Diplodoc Platform v5.39.1
alternate:
  - https://yandex.ru/dev/dialogs/alice/doc/ru/voices.md
---
# Голоса навыков

{% include notitle [neuroexpert-button](_includes/reusables/neuroexpert-button-99270fdba323.md) %}


Чтобы улучшить синтезированную речь в навыке:

1. [Выберите голос](https://yandex.ru/dev/dialogs/alice/doc/ru/voices.md#actual) для персонажа навыка.
1. Оформите текст в [формате TTS (text-to-speech)](https://yandex.ru/dev/dialogs/alice/doc/ru/speech-tuning.md), и речь навыка зазвучит более естественно.
1. Наложите на голос [эффекты](https://yandex.ru/dev/dialogs/alice/doc/ru/speech-effects.md).

Создавая или редактируя навык в [консоли разработчика](https://dialogs.yandex.ru/developer/), вы можете выбрать голос, который будет слышать пользователь.

## Доступные голоса {#actual}

Ниже перечислены все поддерживаемые голоса, использующие глубокие нейронные сети для синтеза речи. Характеристики голосов можно посмотреть в [документации SpeechKit](https://yandex.cloud/ru/docs/speechkit/tts/voices).

{% cut "Русский язык" %}

- Филипп
- Джейн
- Омаж
- Ермил
- Захар
- Мади
- Даша
- Юлия
- Лера
- Марина
- Александр
- Кирилл
- Антон
- Маша
- Жанар
- Сауле
- Юлдуз
- Замира

{% endcut %}

{% cut "Казахский язык" %}

- Мади
- Амира
- Жанар
- Сауле

{% endcut %}

{% cut "Узбекский язык" %}

- Нигора
- Юлдуз
- Замира

{% endcut %}

{% cut "Английский язык" %}

- Джон

{% endcut %}

{% cut "Немецкий язык" %}

- Леа

{% endcut %}

{% cut "Иврит" %}

- Наоми

{% endcut %}

Вы можете протестировать синтез речи с любым из поддерживаемых голосов на [тестовом стенде SpeechKit](https://webasr.yandex.net/ttsdemo.html).

## Советы по использованию голоса {#use-alice}

- Даже если вы выбрали голос Алисы, не говорите в навыке от ее имени. Если пользователь запутается — он начнет называть стандартные команды для Алисы, которые ваш навык может не поддерживать.
    
- Старайтесь не использовать аббревиатуры и слова на иностранных языках.
    
- Для длинных текстов (от нескольких предложений) выбирайте голос Эркана Яваса: он лучше всех справляется с долгим чтением. Другие голоса подойдут для навыков с короткими фразами.
    
- Проверяйте, как звучит навык: у каждого голоса свои особенности.
    

## Полезные видео {#useful-video}

{% cut "Разработка прототипа голосового приложения (с 5:48)" %} 

<div style="
    border:1px solid #d1d5db;
    border-radius:20px;
    overflow:hidden;
    max-width:100%;
">
  <iframe src="https://runtime.strm.yandex.ru/player/video/vplvba3haj2wbsimewde?autoplay=0&mute=0"
    frameborder="0"
    allowfullscreen
    style="
      display:block;
      width:100%;
      height:360px;
      "></iframe>
</div>

{% endcut %}

{% include [index-support-button](_includes/index/id-index/support-button-9ec10631dac1.md) %}


