#!/usr/bin/env python3
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent / "iteration-2"


CHECKS = {
    "eval-4-response-schema": [
        ("Flags missing response.end_session as a protocol problem.", [r"end_session", r"обяз|долж|нет|missing|отсутств"]),
        ("Flags unnecessary top-level session in the response.", [r"session", r"верхн|top.?level|не нуж|лишн|убрать"]),
        ("Mentions that visual cards need useful response.text fallback for voice-only devices.", [r"text", r"fallback|без экран|голос|voice|карточ"]),
        ("Flags ItemsList image requirements or changes the card to a valid/safe response.", [r"ItemsList", r"image_id|изображ|картин|без карточ|убрать card|валид"]),
        ("Provides corrected JSON with version 1.0, response.text, and response.end_session.", [r"```json|\\{", r"version", r"1\.0", r"response", r"text", r"end_session"]),
    ],
    "eval-5-account-linking": [
        ("Requires checking meta.interfaces.account_linking before starting linking.", [r"meta\.interfaces|interfaces", r"account_linking"]),
        ("Uses start_account_linking directive for authorization.", [r"start_account_linking"]),
        ("Mentions session.user.access_token or Authorization token location.", [r"access_token|Authorization", r"session\.user|заголов"]),
        ("Provides fallback behavior when account_linking is unavailable.", [r"недоступ|нет.*account_linking|fallback|альтернатив|попрос"]),
        ("Mentions saving/restoring the original user request or intent for seamless authorization.", [r"сохран|восстанов|исходн|original|intent|запрос"]),
    ],
    "eval-6-state-persistence": [
        ("Maps current session score to session_state.", [r"session_state", r"счет|счёт|score|текущ"]),
        ("Maps authorized user's cross-session progress to user_state_update.", [r"user_state_update", r"между сесс|прогресс|авториз"]),
        ("Maps device/application settings to exact response field application_state, not application_state_update.", [r"\bapplication_state\b", r"настрой|устройств|экземпляр"]),
        ("Mentions 1 KB JSON object limit for stored state.", [r"1\\s*КБ|1\\s*KB|1024"]),
        ("Mentions clearing fields with null and preserving unchanged session_state by returning it.", [r"null", r"session_state", r"верн|возвращ|сохран"]),
    ],
    "eval-7-cards-buttons-surfaces": [
        ("Requires checking screen capability or providing voice-friendly response.text fallback.", [r"screen|экран", r"response\.text|text", r"fallback|голос|без экран"]),
        ("Mentions BigImage, ImageGallery, and ItemsList card types or their selection.", [r"BigImage", r"ImageGallery", r"ItemsList"]),
        ("Mentions item count/image requirements or limits for gallery/list cards.", [r"1.?7|7|1.?5|5|image_id|лимит|изображ"]),
        ("Requires using payload for ButtonPressed handling.", [r"payload", r"ButtonPressed"]),
        ("Warns not to route ButtonPressed by visible button title.", [r"не.*title|не.*текст|не.*назван|не.*надпис|видим"]),
    ],
}


def evidence(text, patterns):
    for pat in patterns:
        match = re.search(pat, text, flags=re.I | re.S)
        if not match:
            return ""
    first = re.search(patterns[0], text, flags=re.I | re.S)
    start = max(0, first.start() - 120)
    end = min(len(text), first.end() + 260)
    return re.sub(r"\s+", " ", text[start:end]).strip()


def main():
    for eval_dir, checks in CHECKS.items():
        for mode in ("with_skill", "without_skill"):
            run_dir = ROOT / eval_dir / mode
            output = run_dir / "outputs" / "output.md"
            text = output.read_text(encoding="utf-8") if output.exists() else ""
            expectations = []
            for label, patterns in checks:
                ev = evidence(text, patterns)
                expectations.append({
                    "text": label,
                    "passed": bool(ev),
                    "evidence": ev or "Required pattern group was not found in output.",
                })
            (run_dir / "grading.json").write_text(
                json.dumps({"expectations": expectations}, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )
            passed = sum(1 for e in expectations if e["passed"])
            print(f"{eval_dir}/{mode}: {passed}/{len(checks)}")


if __name__ == "__main__":
    main()
