---
metadata:
  - name: generator
    content: Diplodoc Platform v5.39.1
alternate:
  - https://yandex.ru/dev/dialogs/alice/doc/ru/skills-promotion-badge.md
---
# Бейдж навыка

{% include notitle [neuroexpert-button](_includes/reusables/neuroexpert-button-99270fdba323.md) %}


{% note alert %}

При размещении бейджа соблюдайте правила: например, не переворачивайте бейдж, не меняйте его текст, не двигайте логотип. Пожалуйста, ознакомьтесь с [правилами](https://doc-static.yandex.net/support/dialogues/alice_badge_guide.pdf) перед тем, как использовать бейдж в своем проекте.

{% endnote %}

Бейдж сообщает пользователям о том, что возможности вашего сайта или приложения доступны в навыке Алисы. При нажатии на бейдж открывается страница [каталога](https://dialogs.yandex.ru/store), из которой пользователи смогут узнать о возможностях навыка и запустить его.

![Бейдж навыка на темном фоне](https://dialogs.s3.yandex.net/badges/v1-term1.svg)    
![Бейдж навыка на светлом фоне](https://dialogs.s3.yandex.net/badges/v1-term3.svg)

Вы можете использовать бейдж только для тех навыков, которые опубликованы в каталоге навыков. Пока бейдж доступен только на русском языке.

Бейдж можно размещать на сайтах или в веб-версиях приложений. Он встраивается на
 страницу как HTML-элемент `<img>`, обернутый в ссылку на каталог навыков. Вам не
 нужно самостоятельно формировать HTML-код бейджа — он генерируется на стороне Диалогов
 автоматически.

## Как получить код бейджа {#code}

1. Зайдите в [консоль разработчика](https://dialogs.yandex.ru/developer/) и перейдите на страницу навыка.
1. Откройте вкладку **Продвижение**.
1. В секции **Бейдж для сайта** скопируйте код для вставки на сайт. ![Код бейджа для вставки на сайт в консоли разработчика]  
    (_images/badge.png =700x)
1. Разместите код на веб-странице.

## Как использовать статическую картинку бейджа  {#image}

При необходимости вы можете использовать статическую картинку бейджа — например, если ваше
 приложение работает в офлайн-режиме. Код картинки можно скопировать из тега `img`.

## Полезные видео {#useful-video}

{% cut "Публикация и продвижение навыков (с 26:03)" %} 

<div style="
    border:1px solid #d1d5db;
    border-radius:20px;
    overflow:hidden;
    max-width:100%;
">
  <iframe src="https://runtime.strm.yandex.ru/player/video/vplverwkt63q2a6ildqc?autoplay=0&mute=0"
    frameborder="0"
    allowfullscreen
    style="
      display:block;
      width:100%;
      height:360px;
      "></iframe>
</div>

{% endcut %}

{% include [index-support-button](_includes/index/id-index/support-button-4bb5cd10ed35.md) %}


