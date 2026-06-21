```python
# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)


HELP_PAYLOAD = {"action": "help"}


@app.post("/webhook")
def webhook():
    body = request.get_json(force=True)

    req = body.get("request", {})
    session = body.get("session", {})

    request_type = req.get("type")
    command = (req.get("command") or "").strip()
    payload = req.get("payload") or {}

    text = "Я умею повторять вашу команду. Скажите что-нибудь или нажмите Помощь."
    end_session = False

    if payload == HELP_PAYLOAD or payload.get("action") == "help":
        text = "Это помощь. Я повторяю вашу команду. Чтобы завершить, скажите: хватит."
    elif request_type == "SimpleUtterance":
        if command.lower() == "хватит":
            text = "Хорошо, завершаю сессию."
            end_session = True
        elif command:
            text = f"Вы сказали: {command}"

    return jsonify({
        "version": body.get("version", "1.0"),
        "session": {
            "session_id": session.get("session_id"),
            "message_id": session.get("message_id"),
            "user_id": session.get("user_id"),
        },
        "response": {
            "text": text,
            "end_session": end_session,
            "buttons": [] if end_session else [
                {
                    "title": "Помощь",
                    "payload": HELP_PAYLOAD,
                    "hide": True,
                }
            ],
        },
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
```

Запуск:

```bash
pip install flask
python app.py
```

Webhook будет доступен по адресу:

```text
POST http://localhost:8000/webhook
```
