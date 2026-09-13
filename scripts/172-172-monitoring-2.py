#!/usr/bin/env python3\n# Sanitize a report line — Monitoring\n# تنظيف نص تقرير — المراقبة والتنبيه\n# استخدمه فقط على جهازك أو على نظام لديك إذن كتابي لاختباره. لا تجمع كلمات مرور أو بيانات شخصية.\n\n"""Monitoring: normalize a line before storing it in a report."""
import re

RAW_LINE = "  finding-172:   review   required  "
clean = re.sub(r"\s+", " ", RAW_LINE).strip()
print({"category": "monitoring", "normalized": clean})
