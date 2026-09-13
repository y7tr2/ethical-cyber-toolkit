#!/usr/bin/env python3\n# Validate a value — Cryptography\n# التحقق من صحة قيمة — التشفير والتجزئة\n# استخدمه فقط على جهازك أو على نظام لديك إذن كتابي لاختباره. لا تجمع كلمات مرور أو بيانات شخصية.\n\n"""Cryptography: validate an input without contacting a remote system."""
import re

VALUE = "example-81"
ALLOWED = re.compile(r"^[A-Za-z0-9._:/-]{1,120}$")

is_valid = bool(ALLOWED.fullmatch(VALUE))
print({"category": "crypto", "value": VALUE, "valid": is_valid})
