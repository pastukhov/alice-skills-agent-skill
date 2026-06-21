---
name: creating-alice-skills
description: Use when designing, implementing, reviewing, testing, publishing, or troubleshooting Yandex Alice skills, Яндекс Диалоги, Алиса voice skills, webhook protocol 1.0, request/response JSON, NLU, cards, buttons, account linking, moderation, or AppMetrica for Alice skills.
---

# Creating Alice Skills

## Overview

Use this skill to help an agent create production-ready Yandex Alice skills. The core principle is to treat an Alice skill as a moderated conversational product plus a strict webhook API: design the user journey first, then implement the JSON protocol, then test moderation and runtime behavior.

This skill is platform-neutral. It does not assume a specific agent runtime, programming language, or deployment target.

## Reference Routing

Read only the references needed for the task:

| Need | Read |
| --- | --- |
| First orientation or broad implementation task | `references/alice-skills-agent-guide.md` |
| Exact list of downloaded source pages | `references/source-pages.md` |
| Request webhook fields | `references/raw-md/request.md`, then the matching `request-*.md` file |
| Response webhook fields | `references/raw-md/response.md`, then the matching card/directive file |
| State persistence | `references/raw-md/session-persistence.md` |
| NLU, intents, entities, utterance handling | `references/raw-md/nlu.md`, `references/raw-md/naming-entities.md`, `references/raw-md/word-processing.md` |
| Buttons, images, cards | `references/raw-md/buttons.md`, `references/raw-md/resource-upload.md`, `references/raw-md/response-card-*.md` |
| Speech, voices, sounds | `references/raw-md/speech-tuning.md`, `references/raw-md/speech-effects.md`, `references/raw-md/voices.md`, `references/raw-md/sounds.md` |
| Account linking / OAuth | `references/raw-md/auth-*.md`, `references/raw-md/response-start-account-linking.md` |
| Moderation and publication | `references/raw-md/requirements.md`, `references/raw-md/moderation.md`, `references/raw-md/publish*.md`, `references/raw-md/publication.md` |
| Deployment | `references/raw-md/deploy-overview.md` and the chosen `deploy-*.md` |
| Testing, monitoring, analytics | `references/raw-md/test.md`, `references/raw-md/health-check.md`, `references/raw-md/monitoring.md`, `references/raw-md/appmetrica.md` |

When the task is high-stakes or the user plans to publish, prefer exact source pages over memory. Requirements can change, and the official legal/moderation rules have priority over summaries.

## Workflow

1. Clarify the skill concept: audience, user goal, activation name, public/private status, surfaces, language, sensitive data, and whether account linking is needed.
2. Check moderation risks early: name, activation phrases, description, brand usage, prohibited content, privacy, advertising, and icon/category fit.
3. Design the conversation: first launch, happy path, fallback path, repeated clarification, help, cancel/exit, and end-session behavior.
4. Choose protocol features: `SimpleUtterance`, `ButtonPressed`, optional `Show.Pull`, state storage, NLU intents/entities, cards, buttons, audio, and analytics events.
5. Implement a webhook that accepts Alice request JSON and returns protocol `1.0` response JSON.
6. Validate every response against core requirements: `response.text`, `response.end_session`, `version`, length limits, fallback text for visual cards, and no unsupported surface assumptions.
7. Prepare console settings and publication metadata.
8. Test in console and with realistic transcripts before sending to moderation.
9. Add monitoring, health checks, and analytics for public or business-critical skills.

## Webhook Contract Quick Reference

Incoming request:

- `meta`: locale, timezone, client, supported interfaces such as `screen`, `account_linking`, `audio_player`.
- `request`: user input. Common types are `SimpleUtterance`, `ButtonPressed`, and `Show.Pull`.
- `session`: session, message, skill, user, and application identifiers; `session.new` marks a new conversation.
- `state`: saved session, user, or application state.
- `version`: protocol version, currently `1.0`.

Minimal response:

```json
{
  "response": {
    "text": "Здравствуйте! Чем помочь?",
    "end_session": false
  },
  "version": "1.0"
}
```

Response essentials:

- `response.text`: required; shown and spoken unless `tts` overrides speech. Keep within documented limits.
- `response.tts`: optional speech markup, voices, pauses, and sounds.
- `response.buttons`: optional suggestions or links; use `payload` for later `ButtonPressed` handling.
- `response.card`: optional visual response; always keep useful `response.text` fallback.
- `response.end_session`: required boolean.
- `session_state`, `user_state_update`, `application_state`: optional state writes.
- `analytics.events`: optional AppMetrica events when configured.

## Design Checks

Before writing code, produce or verify:

- Activation phrase and alternate phrases users can pronounce.
- Opening line that explains what the skill can do.
- At least one example command for the catalog or description.
- Fallback wording for unknown input.
- Exit phrase and response with `end_session: true`.
- Surface-specific behavior for devices with and without `screen`.
- Privacy and account-linking behavior if personal data is used.

## Implementation Guidance

Prefer small handlers by intent:

- Route on `request.type` first.
- For `SimpleUtterance`, route on NLU intents or normalized `request.command`.
- For `ButtonPressed`, route on `request.payload`, not on button title.
- Read previous state from `state.session`, `state.user`, or `state.application`.
- Return the same `session_state` when it must persist unchanged inside a session.
- Avoid using deprecated or discouraged fields when the docs provide a newer field.

Do not hard-code assumptions that every device has a screen, account linking, or audio player. Check `meta.interfaces` before using visual cards, OAuth linking prompts, or audio-player behavior.

## Testing Checklist

Test at least these scenarios:

- First launch with `session.new = true`.
- Empty command after activation phrase.
- Normal `SimpleUtterance` happy path.
- Unknown command and fallback.
- Button click and expected `payload`.
- Device without `screen` when cards are used.
- Device without `account_linking` when OAuth is used.
- State creation, state persistence, and state clearing.
- Explicit exit with `end_session: true`.
- Moderation-facing metadata: name, activation phrases, description, examples, icon, and category.

## Common Mistakes

| Mistake | Correction |
| --- | --- |
| Building the webhook before checking moderation constraints | Check requirements before investing in implementation. Names, brands, and content can block publication. |
| Treating visual cards as the whole answer | Keep `response.text` useful for voice-only devices and card rendering failures. |
| Routing button clicks by displayed text | Use `payload`; titles are UI text and can change. |
| Dropping `session_state` accidentally | Return it again when unchanged state must remain available in later turns. |
| Starting account linking without interface checks | Check `meta.interfaces.account_linking` and provide a non-linking fallback. |
| Assuming official docs never change | For publishing, verify relevant `references/raw-md/*.md` pages and current legal requirements. |

## Expected Output Patterns

When asked to create a skill spec, return:

1. Skill concept and user goal.
2. Activation name suggestions.
3. Conversation flow with sample user and Alice turns.
4. State model.
5. API features needed.
6. Moderation risks.
7. Test checklist.

When asked to implement, return or modify:

1. Webhook endpoint.
2. Request parser and intent/router logic.
3. Response builder that always includes required fields.
4. Tests using realistic Alice request JSON.
5. Deployment notes for the selected platform.

When asked to review, prioritize:

1. Protocol correctness.
2. Moderation and privacy risks.
3. Broken conversation paths.
4. Surface compatibility.
5. Missing tests and monitoring.
