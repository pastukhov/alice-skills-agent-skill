#!/usr/bin/env python3
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent / "iteration-1"


CHECKS = {
    "eval-1-coffee-skill": [
        ("Includes activation name suggestions and example user phrases.", [r"активац", r"фраз", r"пример"]),
        ("Includes a multi-turn conversation flow with fallback and exit behavior.", [r"сценар|диалог|пользователь", r"fallback|не.*понял|ошиб|неизвест", r"выход|заверш|end_session|хватит"]),
        ("Mentions privacy or account-linking considerations for callback requests.", [r"персональн|телефон|соглас|конфиденц|приват|152|авторизац|account"]),
        ("Includes moderation checks for name, description, brand/content, and publication metadata.", [r"модерац", r"назван", r"описан", r"бренд|контент|икон|категор|публикац"]),
        ("Includes a concrete test checklist.", [r"тест|чек.?лист|провер"]),
    ],
    "eval-2-minimal-webhook": [
        ("Routes on request.type and handles SimpleUtterance separately from ButtonPressed.", [r"request.*type|type.*request|request_type|req\.get\(\"type\"\)", r"SimpleUtterance", r"ButtonPressed"]),
        ("Uses ButtonPressed payload rather than button title for the help action.", [r"payload", r"помощ|help"]),
        ("Returns response.text, response.end_session, and version 1.0.", [r"response", r"\btext\b", r"end_session", r"version", r"1\.0"]),
        ("Ends the session when the user says the specified exit word.", [r"хватит", r"end_session.*true|true.*end_session"]),
        ("Uses realistic Alice request/response JSON field names.", [r"original_utterance|command|session|meta|nlu", r"response"]),
    ],
    "eval-3-moderation-review": [
        ("Flags use of Yandex/Alice-related branding or official status claims as a moderation risk.", [r"яндекс|алис", r"официальн", r"бренд|прав"]),
        ("Flags superlative or clickbait wording such as 'best' or 'official' without proof.", [r"лучш|сам|кликбейт|превосход|официальн"]),
        ("Flags medical diagnosis promises as a safety/legal moderation risk.", [r"медицин|диагноз|симптом|здоров|лиценз"]),
        ("Discusses links/traffic/advertising concerns rather than ignoring them.", [r"ссылк|сайт|реклам|трафик|клиник"]),
        ("Proposes safer concrete alternatives for name, description, and functionality.", [r"исправ|замен|альтернатив|лучше|можно"]),
    ],
}


def evidence(text, patterns):
    for pat in patterns:
        match = re.search(pat, text, flags=re.I | re.S)
        if not match:
            return ""
    first = re.search(patterns[0], text, flags=re.I | re.S)
    if not first:
        return ""
    start = max(0, first.start() - 120)
    end = min(len(text), first.end() + 220)
    return re.sub(r"\s+", " ", text[start:end]).strip()


def grade_file(path, checks):
    text = path.read_text(encoding="utf-8") if path.exists() else ""
    expectations = []
    for label, patterns in checks:
        ev = evidence(text, patterns)
        expectations.append({
            "text": label,
            "passed": bool(ev),
            "evidence": ev or "Required pattern group was not found in output.",
        })
    return {"expectations": expectations}


def main():
    for eval_dir, checks in CHECKS.items():
        for mode in ("with_skill", "without_skill"):
            run_dir = ROOT / eval_dir / mode
            output = run_dir / "outputs" / "output.md"
            grading = grade_file(output, checks)
            (run_dir / "grading.json").write_text(
                json.dumps(grading, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )
            passed = sum(1 for e in grading["expectations"] if e["passed"])
            print(f"{eval_dir}/{mode}: {passed}/{len(checks)}")


if __name__ == "__main__":
    main()
