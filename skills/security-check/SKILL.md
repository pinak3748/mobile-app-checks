---
name: security-check
description: Pre-release security check for a mobile app and its backend: exposed keys, open database rules, unprotected server functions, purchase unlocks, AI prompt abuse, network hosts and dependencies. Use before shipping any iOS or Android app.
---

# Security Check

Finds the mistakes that leak data or run up a bill, before a stranger does.

Output: `security-check.md` in the repo root, ending in `PASS` or `FAIL`.

For check 1, run `python3 scripts/secret_scan.py <repo>` from this skill's folder first (Python 3 standard library only, nothing to install). It prints where a possible secret is, never the secret.

## Checks

Run every check. Each finding gets a severity: `critical` (data or money at risk), `high` or `low`.

1. **Secrets in the app.** API keys, service account files, signing passwords, private endpoints. A key that must ship in the app is restricted to the app's identifiers in its provider's console. Every other secret lives on the server.
2. **Data rules.** For each collection or table: who can read, who can write, and what stops one user reading another's data. A rule that allows all reads or writes is `critical`.
3. **Server functions.** Each checks the caller, validates input and rate-limits per user. A function that calls a paid service with no per-user cap is `critical`.
4. **Purchases.** Paid features unlock from the purchase provider's verdict, not a local flag the user could flip (`high`).
5. **AI features.** User text cannot override system instructions or reach other users' data. Output is filtered. Per-user daily caps exist.
6. **Abuse checks.** Device attestation (App Check, Play Integrity, App Attest) on in release builds, debug tokens removed.
7. **What leaves the phone.** List every network host the release build contacts. Each one is in the privacy policy.
8. **Dependencies.** Run the stack's audit command. A known critical issue in a shipped package is `high`.

## Rules

- A check that cannot run is reported as `not checked: <reason>`, never left out.
- Fix `critical` and `high` before release.

## Report

| # | Check | Result | Severity | Evidence | Fix |
|---|---|---|---|---|---|

Last line: `PASS` or `FAIL`.

---
Part of the free checks from [MobileKit](https://mobilekit.co), the full idea-to-App-Store kit for Claude Code.
