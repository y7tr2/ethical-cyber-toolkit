#!/usr/bin/env python3\n# Sanitize a report line — Environment audit\n# تنظيف نص تقرير — بيئة التشغيل\n# استخدمه فقط على جهازك أو على نظام لديك إذن كتابي لاختباره. لا تجمع كلمات مرور أو بيانات شخصية.\n\n"""Environment audit: normalize a line before storing it in a report."""
import re

RAW_LINE = "  finding-122:   review   required  "
clean = re.sub(r"\s+", " ", RAW_LINE).strip()
print({"category": "environment", "normalized": clean})
