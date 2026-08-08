# Module 1 — "The tap that fires"

An NDEF URL that launches on tap means a stranger's web page runs in your
browser before you chose to trust it. This module lets you feel that — safely,
on your own devices, with code you can read end to end.

> **Trust model:** you attack your own second device. Your phone is the victim,
> your own laptop is the (optional) server. Nothing here connects to presenter
> hardware, presenter implants, or any shared box. Read every file before you
> run it — that's the whole spirit of this. See [`../TRANSPARENCY.md`](../TRANSPARENCY.md).

## Files
- **`index.html`** — the demonstrator page. Pure client-side, no network, no storage.
- **`beacon.js`** — optional one-time "check-in" to your own laptop (Tier 1). Opt-in.
- **`hook_server.py`** — optional local server that serves the page and logs check-ins. Python stdlib only, no installs.

## Tier 0 — everyone, zero install, nothing leaves your phone
1. On your phone, open the hosted page (GitHub Pages URL from the pod lead) — or write that URL to your NTAG216 in **NFC Tools** and tap it.
2. Watch the page show what it already knows about you without asking, and read the "sign in" note.
3. **Point:** you opened nothing, yet a page is profiling you. That's the redirect/payload hook.

Tier 0 makes **no** network requests. Confirm it: open `index.html` source — there is no `fetch`, no tracker, no off-page resource.

## Tier 1 — optional live callback, on your own laptop
For the "my phone just checked into my laptop" moment. Requires a laptop and a network you control (your own hotspot is best at con).

1. Read `beacon.js` and `hook_server.py` first.
2. On your laptop: `cd module1 && python3 hook_server.py`
3. It prints a URL like `http://<your-laptop-ip>:8000/`. Write that into your NTAG216 with NFC Tools.
4. In `index.html`, uncomment the single clearly-marked Tier-1 line at the bottom (it loads `beacon.js`).
5. Tap the tag with **your** phone. Your phone appears in your laptop's log — the callback.

The beacon talks **only** to the origin that served the page (your laptop). It sends one request and stops. It is not a control channel. If you want the full browser-control panel, that's **BeEF** — a separate, well-known tool, intentionally *not* bundled here; install it yourself if you want the deep dive.

## Defense side (same two devices)
1. Before tapping, decode the tag in NFC Tools — read the raw URI record. Would you have spotted the redirect?
2. With Tier 1 running, watch your own laptop's log catch the check-in. Write a one-line detection idea (e.g., flag unexpected NDEF-launched hosts, or an outbound hit right after an NFC intent).

## Why it's built this way
No obfuscation, no minification, no third-party calls, no data leaving your devices, stdlib-only server. At a hacker con you should be able to audit anything you run in under five minutes — these files are written to make that easy.
