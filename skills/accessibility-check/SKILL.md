---
name: accessibility-check
description: Checks a mobile app screen or flow for accessibility problems (text scaling, contrast, screen reader labels, touch targets, colour, motion, forms). Use when building or reviewing any iOS, Android, Flutter or React Native screen.
---

# Accessibility Check

Many users change their text size or a display setting. A screen that breaks for them is a bug, and often a bad store review.

## Rules

- **Text scales.** Every screen works at the largest system text size: nothing clipped, nothing overlapping, every action reachable. Layouts grow and wrap; they never shrink text to fit.
- **Contrast.** Body text 4.5:1 against its background, large text and icons 3:1, in light and dark mode.
- **Screen readers.** Every control has a label that says what it does. Meaningful images have a description; decoration is hidden. Reading order follows visual order. Custom controls announce role and state.
- **Touch targets** at least 44x44 pt on iOS, 48x48 dp on Android, with space between them.
- **Never colour alone.** Errors, selection and status also use an icon, text or shape.
- **Motion.** With reduce-motion on, large movement and parallax become a fade or nothing. Nothing flashes more than 3 times a second.
- **Forms.** Visible label per field, errors next to the field in words, keyboard type matches the input.
- **Time.** Nothing important disappears on a timer the user cannot extend.
- **Sound and haptics** add to a message, never the only signal.

## How to run it

1. List the screens in scope.
2. For each screen, go through every rule above and record `pass`, `fail` (with file and line) or `not checked: reason`.
3. A text-scaling failure or a missing label on a primary action is **high** severity. Fix highs before release.
4. End with a table: screen, rule, result, fix.

## In the store listing

Claim only the accessibility features that passed this check.

---
Part of the free checks from [MobileKit](https://mobilekit.co), the full idea-to-App-Store kit for Claude Code.
