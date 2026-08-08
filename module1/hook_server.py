#!/usr/bin/env python3
# =============================================================================
# MODULE 1 · TIER 1 (OPTIONAL) · hook_server.py · runs on YOUR laptop
# =============================================================================
#
# READ THIS BEFORE YOU RUN IT. At a hacker con you read code before executing
# it — so here is the whole truth about this ~90 lines:
#
# WHAT IT DOES
#   • Serves the Module 1 page (index.html + beacon.js) from THIS folder over
#     plain HTTP so your phone on the same Wi-Fi can load it from your laptop.
#   • Logs each request to your terminal: time, client IP, path, user-agent.
#     That log is the "callback" — you watch your own phone check in.
#
# WHAT IT DOES NOT DO
#   • It does NOT execute commands, run shell, control any browser, or push any
#     payload. It only serves static files and prints a log line. That's it.
#   • It stores nothing to disk. It contacts no third party. It opens no
#     outbound connections at all — it only listens.
#   • It has no auth, no TLS, no persistence. It is a teaching beacon, not a
#     tool you should leave running or expose to a network you don't control.
#
# DEPENDENCIES: none. Pure Python 3 standard library. No pip install. You can
# audit every import below — they ship with Python.
#
# RUN IT:
#     cd module1
#     python3 hook_server.py
# Then it prints the URL to write into your NDEF tag. Only use it on a network
# you own (your own hotspot is ideal at a conference). Ctrl-C to stop.
# =============================================================================

import http.server        # stdlib: simple HTTP server + static file handler
import socketserver       # stdlib: TCP server plumbing
import socket             # stdlib: used once, only to discover your LAN IP
import datetime           # stdlib: timestamps for the log
import os                 # stdlib: serve files from this script's folder

PORT = 8000               # change if 8000 is busy; it's only a local port.

# Serve files from the folder this script lives in (so it finds index.html
# and beacon.js), regardless of where you launched it from.
WEB_ROOT = os.path.dirname(os.path.abspath(__file__))


class CheckinHandler(http.server.SimpleHTTPRequestHandler):
    """A static-file server that also prints one honest log line per request.

    We subclass the stdlib SimpleHTTPRequestHandler, which already knows how to
    safely serve files from a directory. We add nothing dangerous — we only add
    a print statement and a tiny plain-text reply for the beacon's /checkin.
    """

    def __init__(self, *args, **kwargs):
        # Pin the served directory to WEB_ROOT. This is the same mechanism
        # `python -m http.server` uses; it does not allow escaping the folder.
        super().__init__(*args, directory=WEB_ROOT, **kwargs)

    def _log_hit(self):
        """Print who just connected. This is the whole 'attack callback' demo."""
        stamp = datetime.datetime.now().strftime("%H:%M:%S")
        client_ip = self.client_address[0]                 # the phone's LAN IP
        ua = self.headers.get("User-Agent", "(none)")      # already sent by any browser
        print(f"[{stamp}]  CHECK-IN from {client_ip}  {self.path}")
        print(f"            device: {ua}")

    def do_GET(self):
        # The beacon hits /checkin. We log it and reply with a tiny plain 200.
        # We do NOT read cookies, bodies, or credentials — there are none to read.
        if self.path.startswith("/checkin"):
            self._log_hit()
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"ok")   # the browser ignores this; it's just closure.
            return
        # Any other path = a normal page/file load. Log it, then let the stdlib
        # handler serve the static file exactly as `python -m http.server` would.
        self._log_hit()
        return super().do_GET()

    # Silence the default noisy access log; our _log_hit is the readable version.
    def log_message(self, *args):
        pass


def my_lan_ip():
    """Best-effort discovery of this laptop's LAN IP, so we can print the URL
    you write into the NFC tag. This opens a UDP socket to a non-routable
    address purely to ask the OS 'which local interface would you use?' — it
    sends no packets to anyone and needs no internet."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("10.255.255.255", 1))   # never actually sends; just picks an iface
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"                    # fall back to localhost if offline
    finally:
        s.close()
    return ip


if __name__ == "__main__":
    ip = my_lan_ip()
    print("=" * 64)
    print(" Module 1 · Tier 1 beacon server (serves files + logs check-ins)")
    print(" Only run this on a network you control. Ctrl-C to stop.")
    print("-" * 64)
    print(f" Write THIS url into your NDEF tag (NFC Tools):  http://{ip}:{PORT}/")
    print(f" Then tap it with YOUR phone and watch the log below.")
    print("=" * 64)
    # ThreadingTCPServer so multiple quick loads don't block each other.
    with socketserver.ThreadingTCPServer(("0.0.0.0", PORT), CheckinHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nStopped. Nothing was saved; the server held no state.")
