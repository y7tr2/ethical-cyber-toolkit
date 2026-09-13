#!/usr/bin/env python3\n# Sanitize a report line — JSON & data\n# تنظيف نص تقرير — JSON والبيانات\n# استخدمه فقط على جهازك أو على نظام لديك إذن كتابي لاختباره. لا تجمع كلمات مرور أو بيانات شخصية.\n\n"""JSON & data: normalize a line before storing it in a report."""
import re

RAW_LINE = "  finding-92:   review   required  "
clean = re.sub(r"\s+", " ", RAW_LINE).strip()
print({"category": "json-data", "normalized": clean})
