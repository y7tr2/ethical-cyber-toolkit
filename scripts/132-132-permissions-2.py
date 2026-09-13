#!/usr/bin/env python3\n# Sanitize a report line — Permissions\n# تنظيف نص تقرير — الصلاحيات\n# استخدمه فقط على جهازك أو على نظام لديك إذن كتابي لاختباره. لا تجمع كلمات مرور أو بيانات شخصية.\n\n"""Permissions: normalize a line before storing it in a report."""
import re

RAW_LINE = "  finding-132:   review   required  "
clean = re.sub(r"\s+", " ", RAW_LINE).strip()
print({"category": "permissions", "normalized": clean})
