#!/usr/bin/env python3\n# Validate a value — File integrity\n# التحقق من صحة قيمة — سلامة الملفات\n# استخدمه فقط على جهازك أو على نظام لديك إذن كتابي لاختباره. لا تجمع كلمات مرور أو بيانات شخصية.\n\n"""File integrity: validate an input without contacting a remote system."""
import re

VALUE = "example-31"
ALLOWED = re.compile(r"^[A-Za-z0-9._:/-]{1,120}$")

is_valid = bool(ALLOWED.fullmatch(VALUE))
print({"category": "files", "value": VALUE, "valid": is_valid})
