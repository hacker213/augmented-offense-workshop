# Augmented Offense — Hands-On Lab

**DEF CON Adversary Village · 2-hour hands-on**
Presenters: **Len Noe** & **Dr. Gregory Carpenter** · CW PENSEC

Four hands-on modules on how everyday access credentials are read, cloned, and —
for one of them — why they can't be. Each card in your hand is the external twin
of a subdermal implant.

---

## Start here (2 minutes)

1. **Read [SAFETY.md](SAFETY.md) first.** Authorized-use only; your own blank cards only; never a real badge.
2. Install the apps below.
3. Open **[LAB.md](LAB.md)** on your phone and follow along.

## Apps to install now

**iPhone**
- NFC Tools *(Module 1)*
- Apex Manager *(Module 4 — the VivoKey/Apex app; not the generic VivoKey/Fidesmo app)*

**Android**
- NFC Tools *(Module 1)*
- MIFARE Classic Tool — "MCT" *(Module 2, NXP-chipset phones only)*
- Apex Manager *(Module 4)*

> **Phone reality:** no phone has a 125 kHz radio, so **Module 3 is Flipper/Proxmark only**; and iPhones can't do MIFARE Classic, so **Module 2 on iPhone uses a Flipper/Proxmark**. Modules 1 & 4 are fully phone-native.

## The four modules

| # | Card | Attack | What you do | Reader |
|---|------|--------|-------------|--------|
| 1 | NTAG216 | **Fl3$hH00k** | Write an NDEF URL that fires on tap | Phone |
| 2 | MIFARE Classic 1k gen2 | forge the UID | Write a chosen badge UID onto a magic card | Flipper / Proxmark / Android |
| 3 | T5577 | **H@nd$hak3** | Copy the physical master onto your blank | Flipper / Proxmark |
| 4 | VivoKey | **Cryptobionic security** | Meet the credential with nothing to clone | Phone |

## What you'll use

- **Modules 1 & 4** — your phone.
- **Modules 2 & 3** — a **Flipper Zero** (works on its own) or a **Proxmark3 + laptop**. Both paths are in each module guide.
- **Module 3** copies a **physical master** provided at the front — read it, write it onto your own blank. Nothing to install.

## Files

- **[LAB.md](LAB.md)** — quick step-by-step for all four modules
- **[student-guides/](student-guides/)** — the full beginner walkthrough, one per module (1–4) — Markdown, Word (.docx), and PDF
- **[SAFETY.md](SAFETY.md)** — rules of engagement
- **[TOOLS.md](TOOLS.md)** — the open-source tools used, with links
- **[module1/](module1/)** — Module 1 demonstrator page + optional local beacon (read before you run)
- **[proxmark/common_keys.dic](proxmark/common_keys.dic)** / **[android/mct_common_keys.dic](android/mct_common_keys.dic)** — the common-key dictionary used to read a card back in Module 2

## Running code at a con

Never run code you haven't read. Everything here is unminified, commented, makes
no hidden network calls, and keeps all data on your own devices. Start with
[TRANSPARENCY.md](TRANSPARENCY.md).

---
*Pull, don't print. Updates land here during the session.*
