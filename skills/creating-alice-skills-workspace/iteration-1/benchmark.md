# creating-alice-skills iteration 1 benchmark

## Summary

| Configuration | Passed | Total | Pass rate |
| --- | ---: | ---: | ---: |
| with_skill | 15 | 15 | 100% |
| without_skill | 14 | 15 | 93.3% |

## Per eval

| Eval | with_skill | without_skill | Notes |
| --- | ---: | ---: | --- |
| coffee-skill-design | 5/5 | 5/5 | Both outputs covered the broad design checklist. The with-skill output was more explicit about Alice protocol details such as `end_session`, payloads, ping, and response fields. |
| minimal-webhook | 5/5 | 4/5 | Baseline missed the exact routing assertion in the heuristic grader because it used `request_type` indirection; semantically it was close. With-skill output stayed closer to current response format and did not add a top-level `session` object. |
| moderation-review | 5/5 | 5/5 | Both outputs identified the main moderation risks. The with-skill output included more official-doc-like details about prohibited Yandex/Alice naming and verification. |

## Analyst notes

The current assertions are useful smoke tests, but two of the three evals are not strongly discriminating because a capable baseline can answer them from general knowledge. For a stronger next iteration, add evals that require exact details from the bundled docs:

- response schema: detect and fix invalid top-level fields, missing `version`, missing `end_session`, card fallback text, and state persistence behavior;
- moderation: exact constraints for activation names, brand confirmation, public/private moderation differences, and clickbait wording;
- account linking: require checking `meta.interfaces.account_linking`, `start_account_linking`, and token locations;
- surfaces: behavior with and without `screen`, `audio_player`, and visual cards.

Timing and token stats were not available in subagent completion notifications, so this benchmark records pass/fail only.
