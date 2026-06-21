# creating-alice-skills

Universal agent skill for designing, implementing, reviewing, testing, publishing, and troubleshooting Yandex Alice skills.

## Contents

- `SKILL.md` - main skill instructions and reference routing.
- `references/alice-skills-agent-guide.md` - short practical guide for agents.
- `references/source-pages.md` - downloaded official source index.
- `references/raw-md/*.md` - official Yandex Dialogs Alice documentation pages in Markdown.
- `evals/evals.json` - realistic evaluation prompts for validating the skill.

## Installation

Copy the whole `creating-alice-skills` directory into the skills directory used by your agent runtime. The only required file is `SKILL.md`; keep `references/` with it so the skill remains self-contained.

Generic setup:

- Copy the directory to the runtime's configured `skills/` directory.
- Keep the folder name `creating-alice-skills`.
- Ensure the agent can read bundled files using the relative paths referenced from `SKILL.md`.
- For custom runtimes, load `SKILL.md` as the triggerable skill body and expose `references/` and `evals/` under the same relative paths.

## Quick Validation

Check that:

- `SKILL.md` has YAML frontmatter with `name` and `description`.
- `name` is `creating-alice-skills`.
- `references/raw-md/` contains the official Alice documentation pages.
- `evals/evals.json` parses as JSON.
