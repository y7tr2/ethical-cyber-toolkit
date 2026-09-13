#!/usr/bin/env python3\n# Sanitize a report line — File integrity\n# تنظيف نص تقرير — سلامة الملفات\n# استخدمه فقط على جهازك أو على نظام لديك إذن كتابي لاختباره. لا تجمع كلمات مرور أو بيانات شخصية.\n\n"""File integrity: normalize a line before storing it in a report."""
import re

RAW_LINE = "  finding-32:   review   required  "
clean = re.sub(r"\s+", " ", RAW_LINE).strip()
print({"category": "files", "normalized": clean})
