#!/usr/bin/env python3\n# Sanitize a report line — Web headers\n# تنظيف نص تقرير — رؤوس الويب\n# استخدمه فقط على جهازك أو على نظام لديك إذن كتابي لاختباره. لا تجمع كلمات مرور أو بيانات شخصية.\n\n"""Web headers: normalize a line before storing it in a report."""
import re

RAW_LINE = "  finding-52:   review   required  "
clean = re.sub(r"\s+", " ", RAW_LINE).strip()
print({"category": "web-headers", "normalized": clean})
