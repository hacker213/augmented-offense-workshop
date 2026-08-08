# TOOLS — reproduce this at home

Everything here is open-source or freely available. All techniques are standard, published, and used here against **controlled targets only**.

## Phone apps
- **NFC Tools** (iOS / Android) — read/write NDEF records. Module 1.
- **MIFARE Classic Tool (MCT)** (Android, NXP chipset) — read/dictionary/clone MIFARE Classic. Module 2.
- **VivoKey / Fidesmo** (iOS / Android) — interact with VivoKey secure elements. Module 4.

## Readers / writers
- **Flipper Zero** — LF (T5577) and HF (MIFARE Classic) read/save/write/emulate.
- **Proxmark3** (Easy or RDV4) + Iceman firmware — the reference LF/HF platform.
  - LF: `lf search`, `lf em 410x clone`, `lf hid clone`
  - HF: `hf mf autopwn`, `hf mf chk`, `hf mf nested`, `hf mf restore`, `hf 14a reader`

## Cards used
- **NTAG216** — NFC Type 2, NDEF. ~888 bytes user memory.
- **MIFARE Classic 1k gen2 ("magic")** — writable block 0 → forgeable UID.
- **T5577** — 125 kHz programmable, emulates EM4100 / HID Prox / Indala / AWID.
- **VivoKey test card** — cryptographic secure element (challenge-response).

## Implant analogs (Len's kit)
| Card | Implant |
|------|---------|
| NTAG216 | xNT |
| MIFARE Classic gen2 | xMagic |
| T5577 | xEM / flexEM |
| VivoKey | Apex / Spark |

## Reference reading
- Proxmark3 / Iceman firmware documentation
- NFC Forum NDEF specification (URI record type)
- NXP MIFARE Classic public documentation
- VivoKey developer docs (secure element / challenge-response)

## Defensive follow-through
- Inventory LF prox and bare MIFARE Classic in your environment — treat both as clonable.
- Pilot challenge-response / identity-bound credentials.
- Add tap-to-URL to user-awareness training; consider MDM controls on background NDEF handling.
