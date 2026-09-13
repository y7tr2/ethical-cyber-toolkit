#!/usr/bin/env python3\n# Enforce an authorized scope — Cryptography\n# تنبيه للمجال المصرّح — التشفير والتجزئة\n# استخدمه فقط على جهازك أو على نظام لديك إذن كتابي لاختباره. لا تجمع كلمات مرور أو بيانات شخصية.\n\n"""Cryptography: refuse to continue until an explicit local scope is set."""
import os

scope = os.getenv("AUTHORIZED_SCOPE", "").strip().lower()
allowed = {"localhost", "127.0.0.1", "owned-lab"}
if scope not in allowed:
    raise SystemExit("Set AUTHORIZED_SCOPE to localhost, 127.0.0.1, or owned-lab before running.")
print({"scope": scope, "authorized": True, "check": "crypto-90"})
