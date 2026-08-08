/* ============================================================================
   MODULE 1 · TIER 1 (OPTIONAL) · beacon.js · "check in to your own laptop"
   ============================================================================

   READ THIS BEFORE YOU LOAD IT.

   WHAT IT DOES
     • Sends ONE tiny HTTP GET to the SAME address this page was served from —
       i.e. your own laptop running hook_server.py. That check-in is what lets
       you watch your phone appear in your laptop's log: the "callback" beat.

   WHAT IT DOES NOT DO
     • It does NOT contact any third party. It talks only to window.location's
       own origin (your laptop). If you opened this page from GitHub Pages /
       a file, there is no server to talk to and the beacon simply no-ops.
     • It does NOT send your inputs, your password, your contacts, your
       location, or any personal data. See exactly what it sends below.
     • It is NOT a remote-control channel. It pings once and stops. There is no
       command loop, no code execution, no "control" of your browser. (If you
       want the full browser-control experience, that's the optional BeEF path
       described in README.md — a separate, well-known tool, not this file.)

   This exists so the demo stays entirely on YOUR two devices: your phone
   (victim) checking in to your laptop (attacker). Nothing else is involved.
   ============================================================================ */

(function () {
  "use strict";

  // Talk only to the origin that served this page. On your laptop that's your
  // laptop. Anywhere else (GitHub Pages, file://) this resolves to something
  // with no hook_server listening, so the request harmlessly fails and stops.
  var origin = window.location.origin;

  // The ONLY thing we send: a timestamp and the fact that a browser checked in.
  // We deliberately do not attach the user-agent or any identifiers here — the
  // server already sees the UA on any request, and we're demonstrating the
  // callback, not harvesting. Keep it boring and honest.
  var url = origin + "/checkin?t=" + Date.now();

  // Fire exactly one request. `keepalive` lets it complete even if you navigate
  // away. `mode:'no-cors'` because we don't need to read a response — we only
  // want the server to log that the hit happened. There is no retry, no loop.
  try {
    fetch(url, { method: "GET", mode: "no-cors", keepalive: true });
    console.log("[beacon] one-time check-in sent to your own server:", url);
  } catch (err) {
    // If anything goes wrong (e.g. no server), we do nothing. No fallback,
    // no alternate channel. Failing silently here is the correct behavior.
    console.log("[beacon] no local server reachable — nothing sent.");
  }
})();
