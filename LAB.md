# LAB — Step by Step

Follow your pod lead's pace. Validate every clone by reading it back before moving on.
You work on **your own** blank cards with a **Flipper Zero** (standalone) or a
**Proxmark3 + laptop** — both paths are shown per module. Module 3 copies the
**physical master puck** provided at the front; nothing you need is missing from this
repo. Never a real badge, never someone else's card. See [SAFETY.md](SAFETY.md).

---

## Module 1 — NTAG216 · the tap that fires (PHONE)

**Goal:** write a URL that launches with no app open, no button pressed.

1. Open **NFC Tools → Write → Add a record → URL/URI**.
2. In the URL/URI field, enter **`https://adversaryvillage.org/`**. *(Advanced/Tier-1 only: use the local URL `hook_server.py` prints instead, to demo the laptop callback.)*
3. **Write**, then hold the NTAG216 to the phone. Re-tap to **read it back** and confirm.
4. Now tap it to an **iPhone with no app open** — iOS surfaces the link on its own. *That's the attack: the victim did nothing.*

**Why it matters:** this is the redirect/payload hook — Handshake / Leprosy. The card behaves exactly like Len's xNT implant. A handshake becomes a phish.

*Stuck? If iPhone won't auto-open it, your record wasn't written as a **URL** type — rewrite it.*

---

## Module 2 — MIFARE Classic 1k gen2 · forge the UID

**Goal:** forge a UID of **your choosing** onto the magic gen2 card — proving the
"badge number" is not a secret. **Pick any 8-hex UID** (e.g. `DECAF123`) — make one
up or let the Flipper generate one. Read-back uses the common keys shipped in the
repo (`proxmark/common_keys.dic` / `android/mct_common_keys.dic`) — no key to set.

### Proxmark3 (needs a laptop)
```
hf mf csetuid -u <YOUR_UID>                 # forge your UID onto block 0 (gen2)
hf mf chk --1k -f proxmark/common_keys.dic  # read back with the repo's common keys
hf 14a reader                               # confirm the UID matches
```

### Flipper Zero (standalone, no laptop)
1. **NFC → Add Manually** → Mifare Classic 1K → set the UID to `<YOUR_UID>` → **Save**.
2. Open the saved card → **Write** → present the gen2 blank.
3. Read it back to confirm.

### Android (NXP chipset) — MIFARE Classic Tool
1. Load **`android/mct_common_keys.dic`** as your key file.
2. **Write Block 0** with `<YOUR_UID>` (magic/gen2 option).
3. **Read** it back with that dictionary to confirm.

**Why it matters:** crypto1 is broken, the UID isn't a secret, and a gen2 card forges the UID too. This is Len's xMagic — "I copied your badge in the elevator." Writing an arbitrary UID onto a blank is *exactly* what a cloner does after reading a victim — you just did it with your own value.

*Note: cloning a real (non-blank) card first recovers its keys with `hf mf autopwn` — ask a presenter if you want to see that full flow.*

---

## Module 3 — T5577 · clone the prox card (FLIPPER / PROXMARK — no phone)

**Goal:** copy the **physical master puck** (provided at the front) onto your T5577
and read it back — *"you all now carry the master key."* *No phone can do LF — this
one's on the reader.* You **read the master, then write it** — no value to type in.

### Flipper Zero (standalone, no laptop)
1. **125 kHz RFID → Read** → hold the **master puck** to the back → **Save** as `master`.
2. Open `master` → **Write** → present your blank T5577.
3. **Read** your T5577 → it shows the master's number. Done.

### Proxmark3 (needs a laptop)
```
lf search                            # read the MASTER puck → note the EM4100 ID
lf em 410x clone --id <that ID>      # write it onto your blank T5577
lf search                            # read the T5577 — same ID = cloned
```

**Why it matters:** legacy LF prox is a UID read-and-replay with **no authentication at all**. The entire low-frequency badge ecosystem is this. Len's xEM does it from his hand.

---

## Module 4 — VivoKey · the one you can't clone (PHONE)

**Goal:** experience a credential with nothing to dump, forge, or replay.

1. Open the **Apex Manager** app *(the VivoKey/Apex app — not the generic VivoKey/Fidesmo app)*.
2. **Scan** the VivoKey test card.
3. Watch the challenge-response / cryptographic identity. The keys **never leave the secure element**.

**Why it matters:** compare it to Modules 2–3 — no dump, no UID to forge, no replay. This is what credential security *should* look like, and it's the implant (Apex/Spark) you can scan and still never become.

---

## Where this leaves defenders
UID ≠ identity. Retire LF prox and bare MIFARE Classic. Move to challenge-response, identity-bound credentials. Treat tap-to-URL as untrusted input. And ask the hard question JunkBond closes on: *what does defender visibility even look like when the tool is under the operator's skin?*

See **[TOOLS.md](TOOLS.md)** to reproduce all of this at home.
