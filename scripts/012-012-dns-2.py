#!/usr/bin/env python3\n# Sanitize a report line — DNS & domains\n# تنظيف نص تقرير — DNS واسم النطاق\n# استخدمه فقط على جهازك أو على نظام لديك إذن كتابي لاختباره. لا تجمع كلمات مرور أو بيانات شخصية.\n\n"""DNS & domains: normalize a line before storing it in a report."""
import re

RAW_LINE = "  finding-12:   review   required  "
clean = re.sub(r"\s+", " ", RAW_LINE).strip()
print({"category": "dns", "normalized": clean})
