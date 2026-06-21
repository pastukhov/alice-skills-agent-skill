---
metadata:
  - name: generator
    content: Diplodoc Platform v5.39.1
alternate:
  - https://yandex.ru/dev/dialogs/alice/doc/ru/sounds.md
---
# Обзор

{% include notitle [neuroexpert-button](_includes/reusables/neuroexpert-button-99270fdba323.md) %}


Навык умеет воспроизводить звуки из библиотеки Алисы. Чтобы добавить звуки к тексту, вставьте в свойство ответа `tts` тег `<speaker>`, например:

```json
{
    "tts": "<speaker audio=\"alice-sounds-game-win-1.opus\"> У вас получилось!"
}
```

Свойства и формат ответа описаны в [протоколе работы навыков](https://yandex.ru/dev/dialogs/alice/doc/ru/response.md).

Посмотрите, какие звуки доступны:

- [Вещи](https://yandex.ru/dev/dialogs/alice/doc/ru/sounds/things.md)
- [Животные](https://yandex.ru/dev/dialogs/alice/doc/ru/sounds/animals.md)
- [Игры](https://yandex.ru/dev/dialogs/alice/doc/ru/sounds/games.md)
- [Люди](https://yandex.ru/dev/dialogs/alice/doc/ru/sounds/humans.md)
- [Музыка](https://yandex.ru/dev/dialogs/alice/doc/ru/sounds/music.md)
- [Природа](https://yandex.ru/dev/dialogs/alice/doc/ru/sounds/nature.md)

{% cut "Права в отношении звуков" %}

Все права принадлежат сервису freesound.org и его пользователям — правообладателям работ.

[adriann](https://freesound.org/people/adriann), [altfuture](https://freesound.org/people/altfuture), [aurelon](https://freesound.org/people/aurelon), [billox30](https://freesound.org/people/billox30), [ceich93](https://freesound.org/people/ceich93), [craigsmith](https://freesound.org/people/craigsmith), [eggsandwichent](https://freesound.org/people/eggsandwichent), [Dean-Raul_DiArchangeli](https://freesound.org/people/Dean-Raul_DiArchangeli/), [gameaudio](https://freesound.org/people/gameaudio), [jbierfeldt](https://freesound.org/people/jbierfeldt), [ldk1609](https://freesound.org/people/ldk1609), [leitzordner](https://freesound.org/people/leitzordner), [locontrario23](https://freesound.org/people/locontrario23), [massivecarcrash](https://freesound.org/people/massivecarcrash), [michorvath](https://freesound.org/people/michorvath), [nfrae](https://freesound.org/people/nfrae), [pacway](https://freesound.org/people/pacway), [paresh](https://freesound.org/people/paresh), [plasterbrain](https://freesound.org/people/plasterbrain), [lorenzgillner](https://freesound.org/people/lorenzgillner/), [radiopassiveboy](https://freesound.org/people/radiopassiveboy), [soundmanfilms](https://freesound.org/people/soundmanfilms), [speedy](https://freesound.org/people/speedy), [steffcaffrey](https://freesound.org/people/steffcaffrey), [tempouser](https://freesound.org/people/tempouser), [timgormly](https://freesound.org/people/timgormly), [tojohnpaul](https://freesound.org/people/tojohnpaul), [trautwein](https://freesound.org/people/trautwein), [underlineddesigns](https://freesound.org/people/underlineddesigns), [vonora](https://freesound.org/people/vonora), [vurca](https://freesound.org/people/vurca), [xenognosis](https://freesound.org/people/xenognosis), [zachrau](https://freesound.org/people/zachrau/), [zajo](https://freesound.org/people/zajo), [audione](https://freesound.org/people/audione), [bluedelta](https://freesound.org/people/bluedelta), [charliemidi](https://freesound.org/people/charliemidi), [darkgot](https://freesound.org/people/darkgot), [_nuel](https://freesound.org/people/_nuel/), [deraj](https://freesound.org/people/deraj), [devy32](https://freesound.org/people/devy32), [domvoice](https://freesound.org/people/domvoice), [drmarkreuter](https://freesound.org/people/drmarkreuter), [epicwizard](https://freesound.org/people/epicwizard), [ericlichtenberg](https://freesound.org/people/ericlichtenberg), [esperri](https://freesound.org/people/esperri), [felix.blume](https://freesound.org/people/felix.blume/), [florianreichelt](https://freesound.org/people/florianreichelt), [frankie01234](https://freesound.org/people/frankie01234), [freefire66](https://freesound.org/people/freefire66), [gynation](https://freesound.org/people/gynation), [howardv](https://freesound.org/people/howardv), [iamgiorgio](https://freesound.org/people/iamgiorgio), [jacksonacademyashmore](https://freesound.org/people/jacksonacademyashmore), [josephsardin](https://freesound.org/people/josephsardin), [kangaroovindaloo](https://freesound.org/people/kangaroovindaloo), [kirmm](https://freesound.org/people/kirmm), [klangfabrik](https://freesound.org/people/klangfabrik), [kraftwerk2k1](https://freesound.org/people/kraftwerk2k1), [lloydevans09](https://freesound.org/people/lloydevans09), [misjoc](https://freesound.org/people/misjoc), [multimax2121](https://freesound.org/people/multimax2121), [oldedgar](https://freesound.org/people/oldedgar), [owlstorm](https://freesound.org/people/owlstorm), [quaker540](https://freesound.org/people/quaker540), [reitanna](https://freesound.org/people/reitanna), [rutgermuller](https://freesound.org/people/rutgermuller), [sclolex](https://freesound.org/people/sclolex), [superdaveosbourne](https://freesound.org/people/superdaveosbourne), [tekgnosis](https://freesound.org/people/tekgnosis).

Используя перечисленные звуки в навыке, вы принимаете условия лицензии [Creative Commons 0](https://creativecommons.org/publicdomain/zero/1.0/legalcode).

{% endcut %}

{% include [index-support-button](_includes/index/id-index/support-button-25577a229a74.md) %}


