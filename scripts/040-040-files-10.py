#!/usr/bin/env python3\n# Enforce an authorized scope — File integrity\n# تنبيه للمجال المصرّح — سلامة الملفات\n# استخدمه فقط على جهازك أو على نظام لديك إذن كتابي لاختباره. لا تجمع كلمات مرور أو بيانات شخصية.\n\n"""File integrity: refuse to continue until an explicit local scope is set."""
import os

scope = os.getenv("AUTHORIZED_SCOPE", "").strip().lower()
allowed = {"localhost", "127.0.0.1", "owned-lab"}
if scope not in allowed:
    raise SystemExit("Set AUTHORIZED_SCOPE to localhost, 127.0.0.1, or owned-lab before running.")
print({"scope": scope, "authorized": True, "check": "files-40"})
