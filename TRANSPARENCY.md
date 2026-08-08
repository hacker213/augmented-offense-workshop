# Transparency & Trust

This is a hacker con. You should never run code you can't read. Everything in
this repo that we ask you to run is written to be audited in a few minutes.

## Our commitments for every file here
- **No obfuscation, no minification.** Source is plain and commented.
- **No hidden network calls.** The only network activity in the whole lab is the
  *optional* Tier-1 beacon in Module 1, which contacts **only your own laptop**,
  once, and says so in its comments. Everything else runs offline.
- **No data leaves your devices.** No telemetry, no analytics, no third-party
  scripts, no cookies/localStorage. We collect nothing about you.
- **No credential capture.** The Module 1 "login" illustration never reads your
  password and sends nothing. Read the handler.
- **Standard-library / no-install where possible.** The Tier-1 server is pure
  Python 3 stdlib — nothing to `pip install`, nothing to trust beyond Python.
- **Your hardware only.** Every exercise runs on your own phone and your own
  laptop. Nothing connects to presenter hardware, presenter implants, or a
  shared server. You attack — and defend — your own second device.

## Your responsibilities
- **Read before you run.** Each file opens with a plain-language "what this does
  / does not do" header. If a header ever doesn't match the code, don't run it —
  tell a presenter.
- **Controlled targets only.** Clone only the labeled lab credentials. Never a
  real badge or another person's device. See [`SAFETY.md`](SAFETY.md).
- **Your own network for Tier 1.** Run the local server only on a network you
  control (your own hotspot is ideal here).

## The tooling — what each file does / does not do
Same rules as everything else here: stdlib-only, no hidden network calls, reads
before it writes.
- **`module1/`** — the Module 1 demonstrator page (`index.html`), the optional
  one-time beacon (`beacon.js`), and the optional local server (`hook_server.py`,
  pure Python stdlib). See [`module1/README.md`](module1/README.md).
- **`proxmark/common_keys.dic`, `android/mct_common_keys.dic`** — well-known-key
  lists you select when reading a card back in Module 2. Text files; they do
  nothing on their own.

## What we deliberately did *not* ship
- The full browser-control framework (**BeEF**) is not bundled. Module 1 ships a
  tiny, readable, one-shot beacon instead, so the demo can't hide behind a big
  tool. If you want BeEF's live panel, install it yourself — it's the optional
  deep-dive, on your own gear.

Found something that doesn't match these promises? That's a bug. Flag it to a
presenter — we'd rather fix it in front of you than have you run something you
don't trust.
