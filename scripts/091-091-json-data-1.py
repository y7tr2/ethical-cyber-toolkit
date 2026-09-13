#!/usr/bin/env python3\n# Validate a value — JSON & data\n# التحقق من صحة قيمة — JSON والبيانات\n# استخدمه فقط على جهازك أو على نظام لديك إذن كتابي لاختباره. لا تجمع كلمات مرور أو بيانات شخصية.\n\n"""JSON & data: validate an input without contacting a remote system."""
import re

VALUE = "example-91"
ALLOWED = re.compile(r"^[A-Za-z0-9._:/-]{1,120}$")

is_valid = bool(ALLOWED.fullmatch(VALUE))
print({"category": "json-data", "value": VALUE, "valid": is_valid})
