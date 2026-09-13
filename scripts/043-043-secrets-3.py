#!/usr/bin/env python3\n# Hash a text value — Secret hygiene\n# حساب SHA-256 لنص — منع تسريب الأسرار\n# استخدمه فقط على جهازك أو على نظام لديك إذن كتابي لاختباره. لا تجمع كلمات مرور أو بيانات شخصية.\n\n"""Secret hygiene: create a reproducible SHA-256 fingerprint."""
import hashlib

payload = "authorized-secrets-43".encode("utf-8")
digest = hashlib.sha256(payload).hexdigest()
print({"sha256": digest, "bytes": len(payload)})
