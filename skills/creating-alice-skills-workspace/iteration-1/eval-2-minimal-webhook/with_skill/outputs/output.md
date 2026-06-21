```js
// server.js
const http = require("http");

const PORT = process.env.PORT || 3000;

function aliceResponse(text, endSession = false) {
  return {
    response: {
      text,
      end_session: endSession,
      buttons: endSession
        ? []
        : [
            {
              title: "Помощь",
              payload: { action: "help" },
              hide: true,
            },
          ],
    },
    version: "1.0",
  };
}

function handleAlice(body) {
  const request = body.request || {};
  const type = request.type;

  if (type === "ButtonPressed" && request.payload?.action === "help") {
    return aliceResponse(
      "Я повторяю вашу команду. Скажите любую фразу или скажите: хватит."
    );
  }

  if (type === "SimpleUtterance") {
    const command = (request.command || "").trim();

    if (/\bхватит\b/i.test(command)) {
      return aliceResponse("Хорошо, завершаю сессию.", true);
    }

    if (!command) {
      return aliceResponse(
        "Привет! Скажите любую команду, и я ее повторю. Для выхода скажите: хватит."
      );
    }

    return aliceResponse(`Вы сказали: ${command}`);
  }

  return aliceResponse("Я умею обрабатывать обычные фразы и кнопку Помощь.");
}

const server = http.createServer((req, res) => {
  if (req.method !== "POST") {
    res.writeHead(405, { "Content-Type": "application/json; charset=utf-8" });
    res.end(JSON.stringify({ error: "Method Not Allowed" }));
    return;
  }

  let raw = "";

  req.on("data", (chunk) => {
    raw += chunk;
  });

  req.on("end", () => {
    try {
      const body = raw ? JSON.parse(raw) : {};
      const response = handleAlice(body);

      res.writeHead(200, { "Content-Type": "application/json; charset=utf-8" });
      res.end(JSON.stringify(response));
    } catch {
      res.writeHead(400, { "Content-Type": "application/json; charset=utf-8" });
      res.end(JSON.stringify({ error: "Invalid JSON" }));
    }
  });
});

server.listen(PORT, () => {
  console.log(`Alice webhook is listening on port ${PORT}`);
});
```

Запуск:

```bash
node server.js
```

Пример ответа на обычную реплику содержит кнопку с `payload`, поэтому нажатие `Помощь` придет как `ButtonPressed` и будет обработано через `request.payload.action`.
