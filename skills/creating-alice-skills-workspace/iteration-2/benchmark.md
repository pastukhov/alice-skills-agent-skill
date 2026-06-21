# creating-alice-skills iteration 2 hard benchmark

## Summary

| Configuration | Passed | Total | Pass rate |
| --- | ---: | ---: | ---: |
| with_skill | 20 | 20 | 100% |
| without_skill | 17 | 20 | 85% |

## Per eval

| Eval | with_skill | without_skill | Discriminating failures |
| --- | ---: | ---: | --- |
| response-schema-repair | 5/5 | 4/5 | Baseline kept/added top-level `session` in the response instead of flagging it as unnecessary. |
| account-linking | 5/5 | 5/5 | Both outputs covered the requested authorization flow. |
| state-persistence | 5/5 | 3/5 | Baseline missed the 1 KB state limit and used `application_state_update` instead of exact response field `application_state`. |
| cards-buttons-surfaces | 5/5 | 5/5 | Both outputs covered card/button/surface rules. |

## Analyst Notes

The hard suite is more useful than iteration 1 because it tests exact protocol details from the bundled documentation. The skill prevented two important baseline mistakes:

- treating `session` as part of the response body;
- inventing `application_state_update` instead of using `application_state`.

The account-linking and cards/buttons tests still need sharper edge cases if we want stronger discrimination. Good next evals:

- ask the agent to repair an invalid `start_account_linking` response that incorrectly includes both `response` and the account-linking directive;
- ask for exact `ImageGallery` and `ItemsList` item count limits and required `image_id` placement;
- ask for a response to a `ButtonPressed` event where the title changed but payload stayed stable.

Timing and token stats were not available in subagent completion notifications, so this benchmark records pass/fail only.
