#!/usr/bin/env python3\n# Sanitize a report line — CSV & reports\n# تنظيف نص تقرير — CSV والتقارير\n# استخدمه فقط على جهازك أو على نظام لديك إذن كتابي لاختباره. لا تجمع كلمات مرور أو بيانات شخصية.\n\n"""CSV & reports: normalize a line before storing it in a report."""
import re

RAW_LINE = "  finding-102:   review   required  "
clean = re.sub(r"\s+", " ", RAW_LINE).strip()
print({"category": "csv-reports", "normalized": clean})
