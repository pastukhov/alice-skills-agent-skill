---
metadata:
  - name: generator
    content: Diplodoc Platform v5.39.1
alternate:
  - https://yandex.ru/dev/dialogs/alice/doc/ru/sounds/things.md
---
<style>
/* убираем серые строки */
.dc-doc-page .yfm table tr:nth-child(2n) {
    background: var(--g-color-base-background);
}
</style>

# Вещи

{% include notitle [neuroexpert-button](../_includes/reusables/neuroexpert-button-99270fdba323.md) %}


Чтобы добавить звуки к произносимому тексту, добавьте в свойство `tts` ответа тег `<speaker>`, например:

```json
{
    "tts": "<speaker audio=\"alice-sounds-game-win-1.opus\"> У вас получилось!"
}
```

#|
||**Звук** |**Код звука для TTS** ||
||
Бензопила

<audio controls src="https://yastatic.net/s3/doc-binary/src/dev/dialogs/ru/alice-sounds-things-chainsaw-1.mp3"></audio>

|
```
<speaker audio="alice-sounds-things-chainsaw-1.opus">
```
||
||
Взрыв

<audio controls src="https://yastatic.net/s3/doc-binary/src/dev/dialogs/ru/alice-sounds-things-explosion-1.mp3"></audio>
|
```
<speaker audio="alice-sounds-things-explosion-1.opus">
```
||
||
Вода (наливается в стакан)

<audio controls src="https://yastatic.net/s3/doc-binary/src/dev/dialogs/ru/alice-sounds-things-water-3.mp3"></audio>
|
```
<speaker audio="alice-sounds-things-water-3.opus">
```
||
||
Вода №1 (льется)

<audio controls src="https://yastatic.net/s3/doc-binary/src/dev/dialogs/ru/alice-sounds-things-water-1.mp3"></audio>
|
```
<speaker audio="alice-sounds-things-water-1.opus">
```
||
||
Вода №2 (бурлит)

<audio controls src="https://yastatic.net/s3/doc-binary/src/dev/dialogs/ru/alice-sounds-things-water-2.mp3"></audio>
|
```
<speaker audio="alice-sounds-things-water-2.opus">
```
||
||
Выключатель №1

<audio controls src="https://yastatic.net/s3/doc-binary/src/dev/dialogs/ru/alice-sounds-things-switch-1.mp3"></audio>
|
```
<speaker audio="alice-sounds-things-switch-1.opus">
```
||
||
Выключатель №2

<audio controls src="https://yastatic.net/s3/doc-binary/src/dev/dialogs/ru/alice-sounds-things-switch-2.mp3"></audio>
|
```
<speaker audio="alice-sounds-things-switch-2.opus">
```
||
||
Выстрел (дробовик)

<audio controls src="https://yastatic.net/s3/doc-binary/src/dev/dialogs/ru/alice-sounds-things-gun-1.mp3"></audio>
|
```
<speaker audio="alice-sounds-things-gun-1.opus">
```
||
||
Гудок корабля №1

<audio controls src="https://yastatic.net/s3/doc-binary/src/dev/dialogs/ru/alice-sounds-transport-ship-horn-1.mp3"></audio>
|
```
<speaker audio="alice-sounds-transport-ship-horn-1.opus">
```
||
||
Гудок корабля №2

<audio controls src="https://yastatic.net/s3/doc-binary/src/dev/dialogs/ru/alice-sounds-transport-ship-horn-2.mp3"></audio>
|
```
<speaker audio="alice-sounds-transport-ship-horn-2.opus">
```
||
||
Дверь №1

<audio controls src="https://yastatic.net/s3/doc-binary/src/dev/dialogs/ru/alice-sounds-things-door-1.mp3"></audio>
|
```
<speaker audio="alice-sounds-things-door-1.opus">
```
||
||
Дверь №2

<audio controls src="https://yastatic.net/s3/doc-binary/src/dev/dialogs/ru/alice-sounds-things-door-2.mp3"></audio>
|
```
<speaker audio="alice-sounds-things-door-2.opus">
```
||
||
Звон бокалов

<audio controls src="https://yastatic.net/s3/doc-binary/src/dev/dialogs/ru/alice-sounds-things-glass-2.mp3"></audio>
|
```
<speaker audio="alice-sounds-things-glass-2.opus">
```
||
||
Колокол №1

<audio controls src="https://yastatic.net/s3/doc-binary/src/dev/dialogs/ru/alice-sounds-things-bell-1.mp3"></audio>
|
```
<speaker audio="alice-sounds-things-bell-1.opus">
```
||
||
Колокол №2

<audio controls src="https://yastatic.net/s3/doc-binary/src/dev/dialogs/ru/alice-sounds-things-bell-2.mp3"></audio>
|
```
<speaker audio="alice-sounds-things-bell-2.opus">
```
||
||
Машина (заводится)

<audio controls src="https://yastatic.net/s3/doc-binary/src/dev/dialogs/ru/alice-sounds-things-car-1.mp3"></audio>
|
```
<speaker audio="alice-sounds-things-car-1.opus">
```
||
||
Машина (не заводится)

<audio controls src="https://yastatic.net/s3/doc-binary/src/dev/dialogs/ru/alice-sounds-things-car-2.mp3"></audio>
|
```
<speaker audio="alice-sounds-things-car-2.opus">
```
||
||
Меч (выходит из ножен)

<audio controls src="https://yastatic.net/s3/doc-binary/src/dev/dialogs/ru/alice-sounds-things-sword-2.mp3"></audio>
|
```
<speaker audio="alice-sounds-things-sword-2.opus">
```
||
||
Меч (парирование)

<audio controls src="https://yastatic.net/s3/doc-binary/src/dev/dialogs/ru/alice-sounds-things-sword-1.mp3"></audio>
|
```
<speaker audio="alice-sounds-things-sword-1.opus">
```
||
||
Меч (поединок)

<audio controls src="https://yastatic.net/s3/doc-binary/src/dev/dialogs/ru/alice-sounds-things-sword-3.mp3"></audio>
|
```
<speaker audio="alice-sounds-things-sword-3.opus">
```
||
||
Сирена №1

<audio controls src="https://yastatic.net/s3/doc-binary/src/dev/dialogs/ru/alice-sounds-things-siren-1.mp3"></audio>
|
```
<speaker audio="alice-sounds-things-siren-1.opus">
```
||
||
Сирена №2

<audio controls src="https://yastatic.net/s3/doc-binary/src/dev/dialogs/ru/alice-sounds-things-siren-2.mp3"></audio>
|
```
<speaker audio="alice-sounds-things-siren-2.opus">
```
||
||
Старый телефон №1

<audio controls src="https://yastatic.net/s3/doc-binary/src/dev/dialogs/ru/alice-sounds-things-old-phone-1.mp3"></audio>
|
```
<speaker audio="alice-sounds-things-old-phone-1.opus">
```
||
||
Старый телефон №2

<audio controls src="https://yastatic.net/s3/doc-binary/src/dev/dialogs/ru/alice-sounds-things-old-phone-2.mp3"></audio>
|
```
<speaker audio="alice-sounds-things-old-phone-2.opus">
```
||
||
Стекло (разбивается)

<audio controls src="https://yastatic.net/s3/doc-binary/src/dev/dialogs/ru/alice-sounds-things-glass-1.mp3"></audio>
|
```
<speaker audio="alice-sounds-things-glass-1.opus">
```
||
||
Строительство (отбойный молоток)

<audio controls src="https://yastatic.net/s3/doc-binary/src/dev/dialogs/ru/alice-sounds-things-construction-2.mp3"></audio>
|
```
<speaker audio="alice-sounds-things-construction-2.opus">
```
||
||
Строительство (пила и молоток)

<audio controls src="https://yastatic.net/s3/doc-binary/src/dev/dialogs/ru/alice-sounds-things-construction-1.mp3"></audio>
|
```
<speaker audio="alice-sounds-things-construction-1.opus">
```
||
||
Телефон №1 (звонок)

<audio controls src="https://yastatic.net/s3/doc-binary/src/dev/dialogs/ru/alice-sounds-things-phone-1.mp3"></audio>
|
```
<speaker audio="alice-sounds-things-phone-1.opus">
```
||
||
Телефон №2 (звонок)

<audio controls src="https://yastatic.net/s3/doc-binary/src/dev/dialogs/ru/alice-sounds-things-phone-2.mp3"></audio>
|
```
<speaker audio="alice-sounds-things-phone-2.opus">
```
||
||
Телефон №3 (набор номера)

<audio controls src="https://yastatic.net/s3/doc-binary/src/dev/dialogs/ru/alice-sounds-things-phone-3.mp3"></audio>
|
```
<speaker audio="alice-sounds-things-phone-3.opus">
```
||
||
Телефон №4 (гудок)

<audio controls src="https://yastatic.net/s3/doc-binary/src/dev/dialogs/ru/alice-sounds-things-phone-4.mp3"></audio>
|
```
<speaker audio="alice-sounds-things-phone-4.opus">
```
||
||
Телефон №5 (гудок)

<audio controls src="https://yastatic.net/s3/doc-binary/src/dev/dialogs/ru/alice-sounds-things-phone-5.mp3"></audio>
|
```
<speaker audio="alice-sounds-things-phone-5.opus">
```
||
||
Унитаз

<audio controls src="https://yastatic.net/s3/doc-binary/src/dev/dialogs/ru/alice-sounds-things-toilet-1.mp3"></audio>
|
```
<speaker audio="alice-sounds-things-toilet-1.opus">
```
||
||
Часы с кукушкой №1

<audio controls src="https://yastatic.net/s3/doc-binary/src/dev/dialogs/ru/alice-sounds-things-cuckoo-clock-1.mp3"></audio>
|
```
<speaker audio="alice-sounds-things-cuckoo-clock-1.opus">
```
||
||
Часы с кукушкой №2

<audio controls src="https://yastatic.net/s3/doc-binary/src/dev/dialogs/ru/alice-sounds-things-cuckoo-clock-2.mp3"></audio>
|
```
<speaker audio="alice-sounds-things-cuckoo-clock-2.opus">
```
||
|#

{% include [index-support-button](../_includes/index/id-index/support-button-fe7d7ef9b128.md) %}