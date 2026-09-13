#!/usr/bin/env python3\n# Validate a value — Environment audit\n# التحقق من صحة قيمة — بيئة التشغيل\n# استخدمه فقط على جهازك أو على نظام لديك إذن كتابي لاختباره. لا تجمع كلمات مرور أو بيانات شخصية.\n\n"""Environment audit: validate an input without contacting a remote system."""
import re

VALUE = "example-121"
ALLOWED = re.compile(r"^[A-Za-z0-9._:/-]{1,120}$")

is_valid = bool(ALLOWED.fullmatch(VALUE))
print({"category": "environment", "value": VALUE, "valid": is_valid})
