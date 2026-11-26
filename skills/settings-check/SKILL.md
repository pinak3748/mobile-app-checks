---
name: settings-check
description: Checks a mobile app's settings screen against what users expect and what the App Store and Google Play require (account deletion, restore purchases, notification permission, support, legal). Use when building or reviewing a settings screen.
---

# Settings Check

Apple and Google both reject apps over settings: no account deletion, no restore purchases. This check catches it first.

## Must have (store rules)

- [ ] **Delete account**, reachable in at most 2 taps from settings. The confirm screen says what is deleted and that subscriptions must be cancelled separately in the store, with a link.
- [ ] Deletion removes the user's server data and files, then the account, then signs out.
- [ ] A **web URL** where users can request deletion (Google Play requires it).
- [ ] **Restore purchases** and a link to manage the subscription in the store, if the app sells anything.
- [ ] Privacy policy and terms links.

## Should have

- [ ] Plan status at the top ("Pro, renews Mar 3" or "Free, Upgrade").
- [ ] Notifications toggle that reflects the real OS permission; if denied, "Turn on in Settings" opens the OS settings.
- [ ] Appearance: system, light, dark. Text size follows the system.
- [ ] Data export (CSV or JSON via the share sheet), if users create data.
- [ ] Contact support opens an email prefilled with app version, OS and device.
- [ ] Rate the app opens the store listing. Never trigger the system review prompt from a button.
- [ ] Sign out warns first if the user is anonymous, since their data would be lost.
- [ ] Version and build number, open-source licences.

## Design

- Destructive rows use a danger colour, sit apart, and always confirm.
- Toggles apply instantly and roll back with a message if they fail.
- At large text sizes rows wrap, never truncate.
- Any debug menu is excluded from production builds by build flavor, not a hidden flag.

## Report

List each item as pass, fail (with file and line) or n/a. Any "must have" fail blocks release.

---
Part of the free checks from [MobileKit](https://mobilekit.co), the full idea-to-App-Store kit for Claude Code.
