#!/usr/bin/env python3\n# Hash a text value — TLS & certificates\n# حساب SHA-256 لنص — TLS والشهادات\n# استخدمه فقط على جهازك أو على نظام لديك إذن كتابي لاختباره. لا تجمع كلمات مرور أو بيانات شخصية.\n\n"""TLS & certificates: create a reproducible SHA-256 fingerprint."""
import hashlib

payload = "authorized-tls-63".encode("utf-8")
digest = hashlib.sha256(payload).hexdigest()
print({"sha256": digest, "bytes": len(payload)})
