---
metadata:
  - name: generator
    content: Diplodoc Platform v5.39.1
alternate:
  - https://yandex.ru/dev/dialogs/alice/doc/ru/speech-tuning.md
---
# Настройка генерации речи

{% include notitle [neuroexpert-button](_includes/reusables/neuroexpert-button-99270fdba323.md) %}


Чтобы речь навыка звучала более естественно, оформите текст с применением TTS-разметки. Разметка размещается в свойстве `response.tts`:

```json
{
  "response": {
    "text": "Добро пожаловать в Атлас.",
    "tts": "Добро пожаловать в +атлас.",
  }
}
```

Проверяйте разметку для голоса на [тестовом стенде Speechkit](https://webasr.yandex.net/ttsdemo.html). Так вы сразу услышите, как звучат изменения.

## Отмечайте ударения {#mark-accents}

Если значение слова меняется в зависимости от ударения — добавляйте перед ударными гласными знак +. Например:

- `остр+ота`
- `м+ука`

## Разделяйте слова {#word-separation}

Разбейте сложные слова на части и проставьте ударения для каждой. Например:

- `мн+ого пр+офильный`
- `с+еми пал+атинск`

## Меняйте написание слов {#change-words}

Попробуйте написать слова так, как они слышатся:

- «ненастный» — `нен+асный`
- «пожалуйста» — `пож+алуста`

## Добавляйте паузы {#add-pause}

Для дополнительной паузы используйте синтаксис `sil <[ <количество_миллисекунд> ]>`. Например, `sil <[1000]>` — это пауза длиной в 1 секунду.

```json
{
  "response": {
    "text": "Смелость города берет.",
    "tts": "смелость sil <[500]> город+а берёт",
  }
}
```

Также паузу в 50–100 мс добавляет пробел между знаком препинания и следующим словом.

## Используйте фонемы {#use-phonemes}

Задавайте произношение слов с помощью фонем и синтаксиса `слово <[произношение_по_фонемам]>`. Например:

- `транскрипция <[t r a n s k rr ii p c y j schwa]>`

{% cut "Как использовать фонемы" %} 

Фонемы:

```
a aa b bb c ch d dd e ee f ff g gg h hh i ii j k kk l ll m mm n nn oo p pp r rr s sch schwa sh ss t tt u uu v vv y yy z zh zz pau
```

Использование:

- `aa`, `ee`, `ii`, `oo`, `uu` — ударные гласные.
- `bb`, `dd`, `ff`, `gg`, `hh`, `kk`, `ll`, `mm`, `nn`, `pp`, `rr`, `ss`, `tt`, `vv`, `zz` — мягкие согласные.
- `y` — это «ы».
- `schwa` — нейтральный гласный звук, в который могут превращаться безударные «а», «е», «и», «о», «ы».
- `pau` — пауза при произнесении.

{% endcut %}


## Полезные видео {#useful-videos}

{% cut "Разработка прототипа голосового приложения (с 6:02)" %}

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

{% cut "Как научить Алису петь?" %} 

<div style="
    border:1px solid #d1d5db;
    border-radius:20px;
    overflow:hidden;
    max-width:100%;
">
  <iframe src="https://runtime.strm.yandex.ru/player/video/vplvdbzofgysoudbs7lg?autoplay=0&mute=0"
    frameborder="0"
    allowfullscreen
    style="
      display:block;
      width:100%;
      height:360px;
      "></iframe>
</div>

{% endcut %}

{% include [index-support-button](_includes/index/id-index/support-button-015159e109c1.md) %}


