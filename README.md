# Mobile App Checks for Claude Code

Three free Claude Code skills that catch what gets mobile apps rejected from the stores, or leaks user data, before you submit.

| Skill | What it catches | Output |
|---|---|---|
| [`accessibility-check`](skills/accessibility-check/SKILL.md) | Text that breaks at large sizes, missing screen reader labels, low contrast, tiny touch targets, motion without a reduce option | Pass or fail per screen, with file and line |
| [`security-check`](skills/security-check/SKILL.md) | API keys in the app, open database rules, server functions with no per-user cap, purchase unlocks a user can flip, prompt injection in AI features | `security-check.md` ending in `PASS` or `FAIL` |
| [`settings-check`](skills/settings-check/SKILL.md) | No account deletion, no restore purchases, missing support and legal links, and other settings gaps Apple and Google reject for | Checklist with every "must have" item |

Works on Flutter, React Native, native iOS (Swift) and native Android (Kotlin) projects. No dependencies: the secret scanner is plain Python 3.

## Install

### As a Claude Code plugin (recommended)

In Claude Code:

```
/plugin marketplace add pinak3748/mobile-app-checks
/plugin install mobile-app-checks@mobile-app-checks
```

### Or copy the skills into your project

```bash
git clone https://github.com/pinak3748/mobile-app-checks
mkdir -p your-app/.claude/skills
cp -r mobile-app-checks/skills/* your-app/.claude/skills/
```

Use `~/.claude/skills/` instead to have them in every project.

## Use

Open your app's folder in Claude Code and ask in plain words:

- *"Run the security check before I ship."*
- *"Check the settings screen against store rules."*
- *"Is the onboarding flow accessible?"*

It picks the right skill, runs it, and lists each finding with where it is and how to fix it.

You can also run the secret scanner on its own:

```bash
python3 skills/security-check/scripts/secret_scan.py path/to/your-app
```

It prints the file and line of each possible secret, never the secret itself, and exits non-zero when it finds one, so it works in CI.

## What's in the repo

```
.claude-plugin/
  plugin.json          plugin manifest
  marketplace.json     lets /plugin marketplace add find it
skills/
  accessibility-check/SKILL.md
  security-check/SKILL.md
  security-check/scripts/secret_scan.py
  settings-check/SKILL.md
```

## Want the whole pipeline?

These are 3 of the 58 skills in [MobileKit](https://mobilekit.co). The full kit takes an app from idea to both stores in Claude Code: research and an idea score, a product interview, three design directions, a phased build with tests, the store listing and screenshots, App Store Connect and Play Console setup, and a weekly growth routine. It shipped [Santa Radar](https://mobilekit.co/#real-run) to the App Store.

## Contributing

Found a false positive, or a store rejection these checks missed? Open an issue with the rejection text or the code that tripped it.

## License

[MIT](LICENSE), for the files in this repo only. MobileKit itself is a separate paid product.
