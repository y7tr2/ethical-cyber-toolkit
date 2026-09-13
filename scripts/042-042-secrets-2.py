#!/usr/bin/env python3\n# Sanitize a report line — Secret hygiene\n# تنظيف نص تقرير — منع تسريب الأسرار\n# استخدمه فقط على جهازك أو على نظام لديك إذن كتابي لاختباره. لا تجمع كلمات مرور أو بيانات شخصية.\n\n"""Secret hygiene: normalize a line before storing it in a report."""
import re

RAW_LINE = "  finding-42:   review   required  "
clean = re.sub(r"\s+", " ", RAW_LINE).strip()
print({"category": "secrets", "normalized": clean})
