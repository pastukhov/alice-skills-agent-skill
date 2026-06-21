---
metadata:
  - name: generator
    content: Diplodoc Platform v5.39.1
alternate:
  - https://yandex.ru/dev/dialogs/alice/doc/ru/naming-entities.md
---
# Именованные сущности в запросах 

{% include notitle [neuroexpert-button](_includes/reusables/neuroexpert-button-99270fdba323.md) %}


После того, как пользователь произносит команду, Диалоги распознают ее текст и извлекают _именованные сущности_ (named entities) — слова и фразы, которые описывают определенные объекты.

Сейчас Диалоги распознают:

- [имена](#fio) (фамилия, имя, отчество);
- [указания на местоположение](#geo);
- [даты и время](#datetime);
- [целые и дробные числа](#number).

Все извлеченные сущности включаются в [запрос к навыку](https://yandex.ru/dev/dialogs/alice/doc/ru/request.md) в свойстве `request.nlu.entities`.

<div style="
    border:1px solid #d1d5db;
    border-radius:20px;
    overflow:hidden;
    max-width:100%;
">
  <iframe src="https://runtime.strm.yandex.ru/player/video/vplvihf2jrmoislnwqym?autoplay=0&mute=0"
    frameborder="0"
    allowfullscreen
    style="
      display:block;
      width:100%;
      height:360px;
      "></iframe>
</div>

## Имя, фамилия, отчество {#fio}

Диалоги распознают и связывают друг с другом имена, фамилии и отчества.

Примеры оформления имен в запросе к навыку:

{% list tabs %}

- Все возможные поля

  Фраза «Антон Павлович Чехов»:

  ```
  "type": "YANDEX.FIO",
  "value": {
    "first_name": "антон",
    "patronymic_name": "павлович",
    "last_name": "чехов"
  }
  ```

- Фамилия и имя

  Фраза «Лев Толстой»:
  ```
  "type": "YANDEX.FIO",
  "value": {
    "first_name": "лев",
    "last_name": "толстой"
  }
  ```

- Имя и отчество, и еще одно имя

  Фраза «Василий Иванович и Петька»:
  ```
  {
    "type": "YANDEX.FIO",
    "value": {
      "first_name": "василий",
      "patronymic_name": "иванович"
    },
  },
  {
    "type": "YANDEX.FIO",
    "value": {
      "first_name": "петька"
    }
  }
  ```

{% endlist %}

## Местоположение {#geo}

Диалоги распознают указания на место:

- `country` — страна;
- `city` — город;
- `street` — улица;
- `house_number` — номер дома;
- `airport` — название аэропорта.

Примеры местоположения в запросе к навыку:

{% list tabs %}

- Полный адрес

  Фраза «Адрес — Россия, Москва, улица Льва Толстого, шестнадцать»:
  ```
  "type": "YANDEX.GEO",
  "value": {
    "country": "россия",
    "city": "москва",
    "street": "улица льва толстого",
    "house_number": "16"
  }
  ```

- Упоминание аэропорта

  Фраза «В аэропорту Внуково»:
  ```
  "type": "YANDEX.GEO",
  "value": {
    "airport": "аэропорт внуково",
  }
  ```

{% endlist %}

## Дата и время {#datetime}

Диалоги распознают упоминания даты и времени, а также относительную дату и время. Например, именованной сущностью станет как фраза «в 1968 году», так и фраза «40 лет назад»:

- `year` — точный год;
- `year_is_relative` — признак того, что в поле `year` указано относительное количество лет;
- `month` — месяц;
- `month_is_relative` — признак того, что в поле `month` указано относительное количество месяцев;
- `day` — день;
- `day_is_relative` — признак того, что в поле `day` указано относительное количество дней;
- `hour` — час;
- `hour_is_relative` — признак того, что в поле `hour` указано относительное количество часов;
- `minute` — минута;
- `minute_is_relative` — признак того, что в поле `minute` указано относительное количество минут.

Примеры даты и времени в запросе к навыку:

{% list tabs %}

- Полная дата и время

  Фраза «в двадцать два часа тридцать минут пятнадцатого сентября тысяча девятьсот восемьдесят второго года»:
  ```
  "type": "YANDEX.DATETIME",
  "value": {
    "year": 1982,
    "month": 9,
    "day": 15,
    "hour": 22,
    "minute": 30,
  }
  ```

- Относительная дата

  Фраза «вчера вечером»:
  ```
  "type": "YANDEX.DATETIME",
  "value": {
    "day": -1,
    "day_is_relative": true
  }
  ```

{% endlist %}  

## Число {#number}

Диалоги распознают целые и дробные числа:

- `integer` — целое число;
- `float` — десятичная дробь.

Примеры чисел в запросе к навыку:

{% list tabs %}

- Целое число

  Фраза «тридцать три попугая»:
  ```
  "type": "YANDEX.NUMBER",
  "value": 33
  ```

- Десятичная дробь

  Фраза «четыре целых пять десятых»:
  ```
  "type": "YANDEX.NUMBER",
  "value": 4.5
  ```

{% endlist %}  

{% include [index-support-button](_includes/index/id-index/support-button-85a4bf821971.md) %}


