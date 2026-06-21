---
metadata:
  - name: generator
    content: Diplodoc Platform v5.39.1
alternate:
  - https://yandex.ru/dev/dialogs/alice/doc/ru/speech-effects.md
---
# Наложение эффектов

{% include notitle [neuroexpert-button](_includes/reusables/neuroexpert-button-99270fdba323.md) %}


Чтобы добавить эффекты в синтезированную речь, вставьте в свойство `tts` ответа тег `<speaker>`, например:

```json
{
    "tts": "<speaker effect="megaphone">Ехал Грека через реку"
}
```

Эффекты работают для всех [голосов](https://yandex.ru/dev/dialogs/alice/doc/ru/voices.md), кроме Алисы.

Там, где эффект должен закончиться, добавьте тег и поставьте вместо имени эффекта дефис. В этом примере через мегафон будет сказана только первая строка стихотворения:

```json
{
    "tts": "<speaker effect="megaphone">Ехал Грека через реку<speaker effect="-"> видит Грека в реке рак"
}
```

Доступные эффекты:
- `behind_the_wall` — голос из-за стены;
    
    <audio style="width: 200px;" title="alice-effect-behind_the_wall" controls="controls" oncontextmenu="return false" controlslist="nodownload">Ваш браузер не поддерживает элемент <code>audio</code>.<source src="https://yastatic.net/s3/doc-binary/src/dev/dialogs/ru/alice-effect-behind_the_wall.mp3" type="audio/mp3"></audio>
    
    
- `hamster` — голос хомяка;

    <audio style="width: 200px;" title="alice-effect-hamster" controls="controls" oncontextmenu="return false" controlslist="nodownload">Ваш браузер не поддерживает элемент <code>audio</code>.<source src="https://yastatic.net/s3/doc-binary/src/dev/dialogs/ru/alice-effect-hamster.mp3" type="audio/mp3"></audio>
    
    
- `megaphone` — голос через мегафон;

    <audio style="width: 200px;" title="alice-effect-megaphone" controls="controls" oncontextmenu="return false" controlslist="nodownload">Ваш браузер не поддерживает элемент <code>audio</code>.<source src="https://yastatic.net/s3/doc-binary/src/dev/dialogs/ru/alice-effect-megaphone.mp3" type="audio/mp3"></audio>

    
- `pitch_down` — низкий голос;

    <audio style="width: 200px;" title="alice-effect-pitch_down" controls="controls" oncontextmenu="return false" controlslist="nodownload">Ваш браузер не поддерживает элемент <code>audio</code>.<source src="https://yastatic.net/s3/doc-binary/src/dev/dialogs/ru/alice-effect-pitch_down.mp3" type="audio/mp3"></audio>

    
- `psychodelic` — психоделический голос;

    <audio style="width: 200px;" title="alice-effect-psychodelic" controls="controls" oncontextmenu="return false" controlslist="nodownload">Ваш браузер не поддерживает элемент <code>audio</code>.<source src="https://yastatic.net/s3/doc-binary/src/dev/dialogs/ru/alice-effect-psychodelic.mp3" type="audio/mp3"></audio>

    
- `pulse` — голос с прерываниями;

    <audio style="width: 200px;" title="alice-effect-pulse" controls="controls" oncontextmenu="return false" controlslist="nodownload">Ваш браузер не поддерживает элемент <code>audio</code>.<source src="https://yastatic.net/s3/doc-binary/src/dev/dialogs/ru/alice-effect-pulse.mp3" type="audio/mp3"></audio>

    
- `train_announce` — громкоговоритель на вокзале.

    <audio style="width: 200px;" title="alice-effect-train_announce" controls="controls" oncontextmenu="return false" controlslist="nodownload">Ваш браузер не поддерживает элемент <code>audio</code>.<source src="https://yastatic.net/s3/doc-binary/src/dev/dialogs/ru/alice-effect-train_announce.mp3" type="audio/mp3"></audio>

{% include [index-support-button](_includes/index/id-index/support-button-ea86e39877eb.md) %}

