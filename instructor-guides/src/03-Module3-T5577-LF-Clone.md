---
title: "Augmented Offense — Module 3: H@nd$hak3 (T5577 125 kHz LF)"
author: "Len Noe & Dr. Gregory Carpenter · CW PENSEC"
date: "~19 min (1:04–1:23) · Flipper or Proxmark — no phone"
---

# Module 3 — H@nd$hak3 (T5577 125 kHz LF), for complete beginners

**You have never used a Proxmark or Flipper? Perfect — this assumes that.**
Follow it top to bottom. Do exactly what each numbered step says and check the
green **"✅ You should see"** box before moving on. The **"⚠️ If not"** box tells
you what to do when something's wrong.

**Implant analog:** xEM / flexEM. **Time:** ~19 minutes.

> **No phone can do this module.** 125 kHz has no radio in any phone. You need a
> **Flipper Zero** (works on its own) or a **Proxmark3** (needs a laptop). We can
> hand you a Flipper if you don't have a reader.

---

## 1. What are you about to do, in plain English?

The old **125 kHz "prox" fob** is the round keyfob or thin white card that opens
a lot of doors. It has **no password** — it just shouts a number, and the door
believes it. That's the entire security model, and it's broken.

At the front of the room there is a **master puck** (213's own retired door-strike
key). You are going to **read its number and copy it onto your own blank card.**
When you're done, your card opens whatever the master opens — *"you all now carry
the master key."* That's the point: copying a prox card is trivial and needs no
secret.

You are copying **213's provided master**, on **your own blank card**. Never copy
a real, in-use badge.

---

## 2. Mini-glossary

- **EM4100** — the most common 125 kHz prox format. Its number is 10 hex
  characters (0–9, A–F).
- **T5577** — a blank card you can write any prox number onto. That's your target.
- **Master puck** — the physical card at the front you'll copy from.
- **Reader** — your **Flipper Zero** (handheld, standalone) or **Proxmark3**
  (board on a USB cable, needs a laptop).

---

## 3. What you need at your seat

- [ ] A **Flipper Zero** *or* a **Proxmark3 + laptop** (ask a pod lead if you need a Flipper)
- [ ] Your blank **T5577 card**
- [ ] Brief access to the **master puck** (shared at the front / passed around by a pod lead)
- [ ] The pod **demo reader** to test your finished card

---

## 4. Pick your path — DO ONLY ONE

**This module has two paths. You do ONE of them, based on the reader in your hand.
They are alternatives, NOT steps — do not do both.**

- Holding a **Flipper Zero**? → do **Path A**, then stop. *(Skip Path B entirely.)*
- Holding a **Proxmark3 + laptop**? → **skip Path A** and do **Path B**.

> Not sure which you have? The Flipper is a small handheld with a screen and a
> dolphin. The Proxmark is a bare circuit board on a USB cable. Ask a pod lead.

---

## Path A — Flipper Zero  *(skip this whole section if you're using a Proxmark)*

The Flipper is a handheld with a screen and arrow buttons. The **125 kHz antenna
runs around the edges** — the master puck and your T5577 sit **flat on the back**
of the Flipper.

**Buttons:** center round button = **OK/Select**. Arrows move. **Back** = previous
screen.

> Menu wording varies slightly by firmware. If a label isn't exact, pick the
> closest match — the flow is the same.

### A1. Open the 125 kHz app
1. Press **OK** for the main menu.
2. Arrow to **125 kHz RFID** and press **OK**.

### A2. Read the master puck
1. Choose **Read**.
2. Hold the **master puck flat against the back** of the Flipper and keep it still.

**✅ You should see** a card read, showing a format like **EM4100** and a number.

⚠️ **If not:** "Reading..." forever → the puck isn't positioned right. Lay it flat
centered on the back, don't move it, and wait. Only one card on the reader at a time.

### A3. Save it
1. Choose **Save**, name it `master`, confirm.

### A4. Write it onto your blank T5577
1. From **125 kHz RFID → Saved**, open `master`.
2. Choose **Write**.
3. Put your **blank T5577 flat on the back** of the Flipper and hold still.

**✅ You should see** **"Successfully written"** (or similar).

⚠️ **If not:** "Write failed" → the T5577 slipped. Re-center it on the back and try
again. Make sure it's the **blank T5577**, not the master.

### A5. Prove it worked
1. From **125 kHz RFID**, choose **Read**.
2. Hold your **T5577** to the back.

**✅ You should see** the **same number as the master.** Your card is now a copy.
Tap it on the pod **demo reader** to confirm it reacts like the master. 🎉

> **🛑 STOP — you're done with Module 3.** Do NOT continue into Path B below;
> that's the Proxmark version of the exact same thing. Move on to Module 4.

---

## Path B — Proxmark3  *(the alternative to Path A — skip this if you already did Path A on a Flipper)*

The Proxmark3 is a small board on a USB cable. The flat **round coil is the LF
(125 kHz) antenna** — cards go there. Everything below is typed at the Proxmark
console.

### B1. Open the console
1. Plug the Proxmark3 into the laptop's USB.
2. In a terminal, type `pm3` and press **Enter**. (If "not found," try `./pm3`
   from the Proxmark folder, or ask a pod lead.)

**✅ You should see** a prompt:
```
[usb] pm3 -->
```
`[usb]` means it's connected. Type every command below at this prompt.

⚠️ **If not:** `[offline]` → not connected. Replug the USB, try another port,
run `pm3` again.

### B2. Read the master puck (get its number)
1. Lay the **master puck flat on the round LF antenna.**
2. Type: `lf search` and press Enter.

**✅ You should see** it identify the card, e.g. `EM410x ID found` with a
10-hex number like `1A2B3C4D5E`. **Write that number down** — it's what you clone.

⚠️ **If not:** "No known 125 kHz tags found" → re-center the puck on the coil and
run `lf search` again.

### B3. Write it onto your blank T5577
1. Take the master off, lay your **blank T5577** on the antenna.
2. Type, replacing `1A2B3C4D5E` with the number from B2:
```
lf em 410x clone --id 1A2B3C4D5E
```

**✅ You should see** a confirmation that it wrote the EM4100 ID to the T5577.

*(If B2 reported HID instead of EM4100, use `lf hid clone` with the values it
showed — ask a pod lead; most master pucks are EM4100.)*

### B4. Prove it worked
1. Keep the T5577 on the antenna. Type: `lf search`

**✅ You should see** the **same number** you wrote. That's the clone confirmed.
Tap it on the pod **demo reader**.

> **🛑 STOP — you're done with Module 3.** (Path A was the Flipper version of this
> same thing — you didn't need it.) Move on to Module 4.

---

## 5. How do I know I succeeded?

Whichever **one** path you did ends the same way: **read your T5577 and see the
master's number**, then **the pod demo reader reacts to your card the same as the
master.** If both are true, you cloned the master.

---

## 6. Why it matters

You just copied a door key by holding it near a $30 gadget — no password, no
hack, no trace. Every low-frequency prox badge on Earth works exactly like this.
An implant (like an xEM) *is* that copy: no card to carry — the operator walks up
and they're the key.

**Defensive angle:** physical access control that trusts a broadcast number has
no defense here — the reader can't tell a clone from the original, and it can't
tell a card from a hand. Retire 125 kHz prox.

---

## 7. Troubleshooting

| What you see | What it means | What to do |
|---|---|---|
| "Reading…" never finishes | card not positioned | lay it flat/centered (Flipper back / Proxmark round coil), hold still, one card only |
| Proxmark: "No known 125 kHz tags" | reader can't see it | re-center on the coil, retry `lf search` |
| Flipper: "Write failed" | T5577 slipped | re-center on the back, retry; confirm it's the blank |
| Clone reads a different number | wrong ID typed (Proxmark) | re-check the number from `lf search`, redo the clone |
| Proxmark prompt `[offline]` | not connected | replug USB, other port, run `pm3` again |
| Everyone's card is identical | expected — you all copied one master | that IS the lesson: "you all carry the master key" |

---

## 8. Safety (non-negotiable)

- Copy **only** the provided master puck, onto **your own** blank T5577.
- **Never** read or clone anyone's real building badge, keyfob, or hotel/transit
  card — not even "just to see."
- These skills are illegal against systems you don't own or aren't authorized to
  test. Here, on the provided master and your own blank, you're clear.

---

## Presenters

- **Len Noe (213)** — <https://www.linkedin.com/in/len-noe/>
- **Dr. Gregory Carpenter (JunkBond)** — <https://www.linkedin.com/in/gcarpenter-cw-pensec/>
