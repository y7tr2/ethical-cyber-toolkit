#!/usr/bin/env python3\n# Sanitize a report line — Log analysis\n# تنظيف نص تقرير — تحليل السجلات\n# استخدمه فقط على جهازك أو على نظام لديك إذن كتابي لاختباره. لا تجمع كلمات مرور أو بيانات شخصية.\n\n"""Log analysis: normalize a line before storing it in a report."""
import re

RAW_LINE = "  finding-22:   review   required  "
clean = re.sub(r"\s+", " ", RAW_LINE).strip()
print({"category": "logs", "normalized": clean})
