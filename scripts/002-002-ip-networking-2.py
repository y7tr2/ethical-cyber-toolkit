#!/usr/bin/env python3\n# Sanitize a report line — IP & networking\n# تنظيف نص تقرير — الشبكات و IP\n# استخدمه فقط على جهازك أو على نظام لديك إذن كتابي لاختباره. لا تجمع كلمات مرور أو بيانات شخصية.\n\n"""IP & networking: normalize a line before storing it in a report."""
import re

RAW_LINE = "  finding-2:   review   required  "
clean = re.sub(r"\s+", " ", RAW_LINE).strip()
print({"category": "ip-networking", "normalized": clean})
