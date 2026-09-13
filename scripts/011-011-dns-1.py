#!/usr/bin/env python3\n# Validate a value — DNS & domains\n# التحقق من صحة قيمة — DNS واسم النطاق\n# استخدمه فقط على جهازك أو على نظام لديك إذن كتابي لاختباره. لا تجمع كلمات مرور أو بيانات شخصية.\n\n"""DNS & domains: validate an input without contacting a remote system."""
import re

VALUE = "example-11"
ALLOWED = re.compile(r"^[A-Za-z0-9._:/-]{1,120}$")

is_valid = bool(ALLOWED.fullmatch(VALUE))
print({"category": "dns", "value": VALUE, "valid": is_valid})
