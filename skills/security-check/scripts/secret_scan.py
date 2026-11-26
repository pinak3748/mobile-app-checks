#!/usr/bin/env python3
"""Searches a repo for things that look like secrets. Stdlib only. Read-only.

Usage:
  secret_scan.py [PATH ...]            default: the current folder
  secret_scan.py --json PATH

Prints file, line and the kind of match, never the secret itself. Exit code 1 if anything is found.
A match is a lead, not proof: a Firebase or Maps API key may ship in an app if it is restricted to
this app's identifiers. Decide each one, and write the decision in security.md.
"""
import json
import os
import re
import sys

PATTERNS = [
    ("private key block", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----")),
    ("service account file", re.compile(r'"type"\s*:\s*"service_account"')),
    ("Google API key", re.compile(r"AIza[0-9A-Za-z_\-]{35}")),
    ("AWS access key id", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("OpenAI-style key", re.compile(r"\bsk-[A-Za-z0-9_\-]{20,}")),
    ("GitHub token", re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b")),
    ("Slack token", re.compile(r"\bxox[abprs]-[A-Za-z0-9\-]{10,}")),
    ("Stripe live key", re.compile(r"\b[sr]k_live_[A-Za-z0-9]{16,}")),
    ("hard-coded password or secret", re.compile(r"(?i)\b(?:password|passwd|secret|api[_-]?key|token)\b\s*[:=]\s*['\"][^'\"\s]{8,}['\"]")),
    ("signing store password", re.compile(r"(?i)\b(?:storePassword|keyPassword)\s*[=:]\s*\S{4,}")),
]
SKIP_DIRS = {".git", "node_modules", "build", ".dart_tool", "Pods", ".gradle", ".idea", "DerivedData", ".venv", "__pycache__"}
SKIP_EXT = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".ico", ".ttf", ".otf", ".woff", ".woff2", ".mp3", ".mp4", ".mov", ".zip", ".jar", ".class", ".so", ".a", ".pdf", ".keystore", ".jks"}
MAX_BYTES = 2_000_000


def scan(root):
    hits = []
    for base, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for name in files:
            if os.path.splitext(name)[1].lower() in SKIP_EXT:
                continue
            path = os.path.join(base, name)
            try:
                if os.path.getsize(path) > MAX_BYTES:
                    continue
                text = open(path, encoding="utf-8", errors="ignore").read()
            except OSError:
                continue
            if name.endswith((".keystore", ".jks", ".p8", ".p12")) or name in ("google-services.json.example",):
                pass
            for lineno, line in enumerate(text.splitlines(), 1):
                for kind, rx in PATTERNS:
                    if rx.search(line):
                        hits.append({"file": path, "line": lineno, "kind": kind})
            if re.search(r"\.(p8|p12|pem|keystore|jks)$", name):
                hits.append({"file": path, "line": 0, "kind": "key or certificate file in the repo"})
    return hits


def main():
    args = [a for a in sys.argv[1:] if a != "--json"]
    paths = args or ["."]
    hits = [h for p in paths for h in scan(p)]
    if "--json" in sys.argv:
        print(json.dumps(hits, indent=1))
    else:
        for h in hits:
            print(f"{h['file']}:{h['line']}  {h['kind']}")
        print(f"\n{len(hits)} possible secret(s) found." if hits else "No possible secrets found.")
    sys.exit(1 if hits else 0)


if __name__ == "__main__":
    main()
