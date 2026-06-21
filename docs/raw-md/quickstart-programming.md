---
metadata:
  - name: generator
    content: Diplodoc Platform v5.39.1
alternate:
  - https://yandex.ru/dev/dialogs/alice/doc/ru/quickstart-programming.md
---
# Программистам

{% include notitle [neuroexpert-button](_includes/reusables/neuroexpert-button-99270fdba323.md) %}


Эта инструкция поможет вам подготовить код на Node.js, Python, PHP, R, Go, Java или C#, запустить его и протестировать навык.

Для примера создадим навык <q>Попугай</q>: он повторяет все, что написал или сказал пользователь.

## Создайте функцию {#prepare-code}

{% cut " Если вы не работали с Yandex Cloud" %}

1. Перейдите по [ссылке](https://console.cloud.yandex.ru/). Примите условия и нажмите кнопку **Войти**.
1. Введите название нового облака и нажмите кнопку **Создать**.

{% endcut %}

Создайте в Yandex Cloud функцию для навыка:

1. Откройте [консоль управления](https://console.cloud.yandex.ru/).
1. Выберите **Cloud Functions**.
1. Нажмите кнопку **Создать функцию**.
1. Введите имя функции. Условия:
    
    - длина — от 3 до 63 символов;
    - может содержать строчные буквы латинского алфавита, цифры и дефисы;
    - первый символ — буква, последний — не дефис.
        
        Например, `my-first-function`.
    
1. Нажмите кнопку **Создать**.
1. Если у вас нет платежного аккаунта, [зарегистрируйте](https://cloud.yandex.ru/docs/billing/quickstart/index) его.

Платежный аккаунт необходим для любых сервисов Yandex Cloud, даже бесплатных. Функции Cloud Functions для навыков Алисы не тарифицируются — Yandex Cloud не будет списывать деньги с вашей карты.

Сразу после создания функция содержит только метаинформацию: имя, описание, уникальный идентификатор и т. д. Вы добавите в функцию код навыка на следующем шаге.

## Создайте версию функции {#create}

Каждая версия функции — это исходный код на языке программирования. Поддерживаются Node.js, Python, Go, Java, C#, PHP, R.

{% list tabs %}

- Node.js

    1\. Сохраните пример кода в файл с названием `index.js` (или скачайте готовый файл с [GitHub](https://github.com/yandex-cloud/examples/blob/master/serverless/functions/alice/nodejs/parrot/index.js)) и создайте ZIP-архив `parrot-js.zip` с этим файлом.
        
    ```javascript
    module.exports.handler = async (event, context) => {
        const {version, session, request} = event;
    
        let text = "Hello! I\'ll repeat anything you say to me.";
        if (request["original_utterance"].length > 0)
            text = request["original_utterance"];
        return {
            version,
            session,
            response: {
                text: text,
                end_session: false,
            },
        };
    };
    ```
        
    2\. В [консоли управления](https://console.cloud.yandex.ru/) в каталоге, где хотите создать версию функции, откройте **Cloud Functions**

    3\. Выберите функцию.

    4\. В разделе **Последняя версия** нажмите кнопку **Создать в редакторе**.

    5\. Задайте параметры версии:
        
    - **Среда выполнения**: `nodejs12`.
    - **Таймаут, секунды**: 2.
    - **Память**: 128 МБ.
    - **Сервисный аккаунт**: Не выбрано.
        
    6\. Подготовьте код функции:
        
    - **Способ**: ZIP-архив.
    - **Файл**: `parrot-js.zip`.
    - **Точка входа**: `index.handler`.
        
    7\. В правом верхнем углу нажмите кнопку **Создать версию**.

- Python

    1\. Сохраните пример кода в файл с названием `parrot.py` (или скачайте готовый файл с [GitHub](https://github.com/yandex-cloud/examples/blob/master/serverless/functions/alice/python/parrot/parrot.py)) и создайте ZIP-архив `parrot-py.zip` с этим файлом.
        
    ```python
    def handler(event, context):
        """
        Entry-point for Serverless Function.
        :param event: request payload.
        :param context: information about current execution context.
        :return: response to be serialized as JSON.
        """
        text = "Hello! I\'ll repeat anything you say to me."
        if "request" in event and \
                "original_utterance" in event["request"] \
                and len(event["request"]["original_utterance"]) > 0:
            text = event["request"]["original_utterance"]
        return {
            "version": event["version"],
            "session": event["session"],
            "response": {
                "text": text,
                "end_session": "false"
            },
        }
    ```
        
    2\. В [консоли управления](https://console.cloud.yandex.ru/) в каталоге, где хотите создать версию функции, откройте **Cloud Functions**

    3\. Выберите функцию.

    4\. В разделе **Последняя версия** нажмите кнопку **Создать в редакторе**.

    5\. Задайте параметры версии:
        
    - **Среда выполнения**: `python37`.
    - **Таймаут, секунды**: 2.
    - **Память**: 128 МБ.
    - **Сервисный аккаунт**: Не выбрано.
        
    6\. Подготовьте код функции:
        
    - **Способ**: ZIP-архив.
    - **Файл**: `parrot-py.zip`.
    - **Точка входа**: `parrot.handler`.
        
    7\. В правом верхнем углу нажмите кнопку **Создать версию**.

- PHP

    1\. Сохраните пример кода в файл с названием `parrot.php` и создайте ZIP-архив `parrot-php.zip` с этим файлом.
        
    ```php
    <?php
    
    function handler($event, $context) {
        $version = $event["version"];
        $session = $event["session"];
        $request = $event["request"];
    
        $text = "Hello! I'll repeat anything you say to me.";
        if (strlen($request["original_utterance"]) > 0) {
            $text = $request["original_utterance"];
        }
    
        return array(
            "version" => $version,
            "session" => $session,
            "response" => array(
                "text" => $text,
                "end_session" => false
            )
        );
    }
    ```
        
    2\. В [консоли управления](https://console.cloud.yandex.ru/) в каталоге, где хотите создать версию функции, откройте **Cloud Functions**.

    3\. Выберите функцию.

    4\. В разделе **Последняя версия** нажмите кнопку **Создать в редакторе**.

    5\. Задайте параметры версии:
        
    - **Среда выполнения**: `php74`.
    - **Таймаут, секунды**: 2.
    - **Память**: 128 МБ.
    - **Сервисный аккаунт**: Не выбрано.
        
    6\. Подготовьте код функции:
        
    - **Способ**: ZIP-архив.
    - **Файл**: `parrot-php.zip`.
    - **Точка входа**: `parrot.handler`.
        
    7\. В правом верхнем углу нажмите кнопку **Создать версию**.

- R

    1\. Сохраните пример кода в файл с названием `parrot.r` и создайте ZIP-архив `parrot-r.zip` с этим файлом.
        
    ```r
    handler <- function(event, context) {
        version <- event$version
        session <- event$session
        request <- event$request
    
        text <- "Hello! I\'ll repeat anything you say to me."
    
        if (nchar(request[["original_utterance"]]) > 0) {
            text <- request[["original_utterance"]]
        }
    
        return(list(
            version = version,
            session = session,
            response = list(
                text = text,
                end_session = FALSE
            )
        ))
    }
    ```
        
    2\. В [консоли управления](https://console.cloud.yandex.ru/) в каталоге, где хотите создать версию функции, откройте **Cloud Functions**.

    3\. Выберите функцию.

    4\. В разделе **Последняя версия** нажмите кнопку **Создать в редакторе**.

    5\. Задайте параметры версии:
        
    - **Среда выполнения**: `r40`.
    - **Таймаут, секунды**: 2.
    - **Память**: 128 МБ.
    - **Сервисный аккаунт**: Не выбрано.
        
    6\. Подготовьте код функции:
        
    - **Способ**: ZIP-архив.
    - **Файл**: `parrot-r.zip`.
    - **Точка входа**: `parrot.handler`.
        
    7\. В правом верхнем углу нажмите кнопку **Создать версию**.

- Go

    1\. Сохраните пример кода в файл с названием `parrot.go` и создайте ZIP-архив `parrot-go.zip` с этим файлом.
    
    ```javascript
    package main
    
    import (
        "context"
        "encoding/json"
        "fmt"
    )
    
    type Event struct {
        Version string   `json:"version"`
        Session struct{} `json:"session"`
        Request struct {
            OriginalUtterance string `json:"original_utterance"`
        } `json:"request"`
    }
    
    type Response struct {
        Version string   `json:"version"`
        Session struct{} `json:"session"`
        Result  struct {
            Text      string `json:"text"`
            EndSession bool   `json:"end_session"`
        } `json:"response"`
    }
    
    func Handler(ctx context.Context, event []byte) (*Response, error) {
        var input Event
        err := json.Unmarshal(event, &input)
        if err != nil {
            return nil, fmt.Errorf("an error has occurred when parsing event: %v", err)
        }
    
        text := "Hello! I'll repeat anything you say to me."
        if input.Request.OriginalUtterance != "" {
            text = input.Request.OriginalUtterance
        }
    
        return &Response{
            Version: input.Version,
            Session: input.Session,
            Result: struct {
                Text      string `json:"text"`
                EndSession bool   `json:"end_session"`
            }{
                Text:      text,
                EndSession: false,
            },
        }, nil
    }
    ```
    
    2\. В [консоли управления](https://console.cloud.yandex.ru/) в каталоге, где хотите создать версию функции, откройте **Cloud Functions**.

    3\. Выберите функцию.

    4\. В разделе **Последняя версия** нажмите кнопку **Создать в редакторе**.

    5\. Задайте параметры версии:
        
    - **Среда выполнения**: `golang119`.
    - **Таймаут, секунды**: 2.
    - **Память**: 128 МБ.
    - **Сервисный аккаунт**: Не выбрано.
        
    6\. Подготовьте код функции:
        
    - **Способ**: ZIP-архив.
    - **Файл**: `parrot-go.zip`.
    - **Точка входа**: `parrot.Handler`.
        
    7\. В правом верхнем углу нажмите кнопку **Создать версию**.

- Java

    1\. Сохраните пример кода в файл с названием `Handler.java` и создайте ZIP-архив `parrot-java.zip` с этим файлом.
    
    ```java
    import java.util.HashMap;
    import java.util.Map;
    import java.util.function.Function;
    
    class Request {
      Map<String, String> queryStringParameters;
      Map<String, Object> request;
      Object version;
      Object session;
    }
    
    class Response {
      private Object version;
      private Object session;
      private Map<String, Object> response;
    
        public Response(Object version, Object session, Map<String, Object> response) {
            this.version = version;
            this.session = session;
            this.response = response;
        }
    }
    
    public class Handler implements Function<Request, Response> {
    
        @Override
        public Response apply(Request request) {
            Map<String, Object> response = new HashMap<>();
    
            Object version = request.version;
            Object session = request.session;
            String originalUtterance = (String) request.request.get("original_utterance");
            String text = "Hello! I'll repeat anything you say to me.";
    
            if (originalUtterance != null && originalUtterance.length() > 0) {
                text = originalUtterance;
            }
    
            response.put("text", text);
            response.put("end_session", false);
    
            return new Response(version, session, response);
        }
    }
    ```
    
    2\. В [консоли управления](https://console.cloud.yandex.ru/) в каталоге, где хотите создать версию функции, откройте **Cloud Functions**.

    3\. Выберите функцию.

    4\. В разделе **Последняя версия** нажмите кнопку **Создать в редакторе**.

    5\. Задайте параметры версии:
        
    - **Среда выполнения**: `java17`.
    - **Таймаут, секунды**: 2.
    - **Память**: 128 МБ.
    - **Сервисный аккаунт**: Не выбрано.
        
    6\. Подготовьте код функции:
        
    - **Способ**: ZIP-архив.
    - **Файл**: `parrot-java.zip`.
    - **Точка входа**: `Handler`.
        
    7\. В правом верхнем углу нажмите кнопку **Создать версию**.

- C#

    1\. Сохраните пример кода в файл с названием `Handler.cs` и создайте ZIP-архив `parrot-csharp.zip` с этим файлом.
        
    ```java
    using System;
    using System.Text.Json;
    
    public class Request
    {
        public string version { get; set; }
        public JsonElement session { get; set; }
        public JsonElement request { get; set; }
    }
    
    public class Response
    {
        public string version { get; set; }
        public JsonElement session { get; set; }
        public object response { get; set; }
    
        public Response(string version, JsonElement session, object response)
        {
            this.version = version;
            this.session = session;
            this.response = response;
        }
    }
    
    public class Handler
    {
        public Response FunctionHandler(Request r)
        {
            string version = r.version;
            JsonElement session = r.session;
            JsonElement request = r.request;
    
            string text = "Hello! I'll repeat anything you say to me.";
            if (request.GetProperty("original_utterance").ToString().Length > 0)
                text = request.GetProperty("original_utterance").ToString();
    
            var responseObj = new
            {
                text = text,
                end_session = false,
            };
    
            return new Response(version, session, responseObj);
        }
    }
    ```
        
    2\. В [консоли управления](https://console.cloud.yandex.ru/) в каталоге, где хотите создать версию функции, откройте **Cloud Functions**.

    3\. Выберите функцию.

    4\. В разделе **Последняя версия** нажмите кнопку **Создать в редакторе**.
    
    5\. Задайте параметры версии:
        
    - **Среда выполнения**: `dotnet6`.
    - **Таймаут, секунды**: 2.
    - **Память**: 128 МБ.
    - **Сервисный аккаунт**: Не выбрано.
        
    6\. Подготовьте код функции:
        
    - **Способ**: ZIP-архив.
    - **Файл**: `parrot-csharp.zip`.
    - **Точка входа**: `Handler`.
        
    7\. В правом верхнем углу нажмите кнопку **Создать версию**.

{% endlist %}

Вне зависимости от таймаута в настройках версии Яндекс Диалоги будут ждать ответа функции не больше 4,5 секунды.

Откроется страница функции, где в блоке **История версий** появится ваша версия с тегом `$latest`.

## Укажите функцию в настройках навыка {#register}

После того как навык заработает, зарегистрируйте его:

1. Перейдите в [консоль разработчика навыка](https://dialogs.yandex.ru/developer/).
1. [Создайте навык](https://yandex.ru/dev/dialogs/alice/doc/ru/skill-create-console.md) и перейдите на вкладку **Настройки**.
1. В блоке **Backend** выберите вариант **Функция в Яндекс Облаке**.
1. Из выпадающего списка выберите функцию.
1. Заполните обязательные поля в блоках **Основные настройки** и **Публикация в каталоге**.
1. Внизу страницы нажмите кнопку **Сохранить**.

В списке отображаются функции, которые вы имеете право просматривать. Но навык заработает, только если вы имеете право запускать функцию. Разрешение на запуск входит в роли Yandex Cloud [functions.functionInvoker](https://cloud.yandex.ru/docs/functions/security/#functions-invoker), [editor](https://cloud.yandex.ru/docs/functions/security/#editor) и выше.

## Проверьте работу навыка {#check}

1. На странице навыка откройте вкладку **Тестирование**.
1. Если все настроено правильно, навык предложит начать беседу: «Hello! I'll repeat anything you say to me».
1. Отправьте сообщение с любым текстом и убедитесь, что вам пришел такой же ответ.
1. Попробуйте изменить код навыка. Откройте функцию во вкладке **Редактор** в [консоли Yandex Cloud](https://console.cloud.yandex.ru/) и отредактируйте код:
    
    {% cut "Измените приветственную фразу" %}

    Найдите строку и измените текст в кавычках. Например:

    {% list tabs %}

    - Node.js

        До: `let text = 'Hello! I\'ll repeat anything you say to me.'`
    
        После: `let text = 'Hello! I\'ll repeat anything you say to me twice.'`

    - Python

        До: `text = 'Hello! I\'ll repeat anything you say to me.'`
    
        После: `text = 'Hello! I\'ll repeat anything you say to me twice.'.`

    {% endlist %}

    {% endcut %}

    {% cut "Измените ответ" %}
    
    Добавьте еще один повтор реплики:

    {% list tabs %}

    - Node.js

        До: `text = request['original_utterance'];`
    
        После: `text = request['original_utterance'].concat('\n').repeat(2);`

    - Python

        До: `text = event['request']['original_utterance']`
        
        После: `text = '\n'.join(2*[event['request']['original_utterance']])`

    {% endlist %}

    {% endcut %}

    Чтобы сохранить новую версию функции, нажмите **Создать версию**. Проверьте изменения в навыке.
    
1. Попробуйте заменить код и среду выполнения в рамках одной функции. Функция останется активной, и накопленная статистика сохранится.

## Что дальше {#next}

- Попробуйте выполнить другие функции, которые возвращают в ответе [изображения](https://yandex.ru/dev/dialogs/alice/doc/ru/resource-upload.md) и проигрывают [звуки](https://yandex.ru/dev/dialogs/alice/doc/ru/resource-sounds-upload.md).
- Узнайте обо всех дополнительных возможностях в [протоколе работы Яндекс Диалогов](https://yandex.ru/dev/dialogs/alice/doc/ru/protocol.md) и [модели программирования Cloud Functions](https://cloud.yandex.ru/docs/functions/concepts/function#programming-model).

## Полезные видео {#useful-video}

{% cut "Школа Алисы. Как бесплатно разместить навык в Yandex Cloud" %}

<div style="
    border:1px solid #d1d5db;
    border-radius:20px;
    overflow:hidden;
    max-width:100%;
">
  <iframe src="https://runtime.strm.yandex.ru/player/video/vplvmbmwed25qlf7wyts?autoplay=0&mute=0"
    frameborder="0"
    allowfullscreen
    style="
      display:block;
      width:100%;
      height:360px;
      "></iframe>
</div>

{% endcut %}

{% cut "Навык за 20 минут" %}

<div style="
    border:1px solid #d1d5db;
    border-radius:20px;
    overflow:hidden;
    max-width:100%;
">
  <iframe src="https://runtime.strm.yandex.ru/player/video/vplvhmmgmqpj5hodbg7l?autoplay=0&mute=0"
    frameborder="0"
    allowfullscreen
    style="
      display:block;
      width:100%;
      height:360px;
      "></iframe>
</div>

{% endcut %}

{% include [index-support-button](_includes/index/id-index/support-button-5db80e993157.md) %}
