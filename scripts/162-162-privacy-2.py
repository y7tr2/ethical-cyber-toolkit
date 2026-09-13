#!/usr/bin/env python3\n# Sanitize a report line — Privacy\n# تنظيف نص تقرير — الخصوصية\n# استخدمه فقط على جهازك أو على نظام لديك إذن كتابي لاختباره. لا تجمع كلمات مرور أو بيانات شخصية.\n\n"""Privacy: normalize a line before storing it in a report."""
import re

RAW_LINE = "  finding-162:   review   required  "
clean = re.sub(r"\s+", " ", RAW_LINE).strip()
print({"category": "privacy", "normalized": clean})
