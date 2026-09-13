#!/usr/bin/env python3\n# Sanitize a report line — Secure coding\n# تنظيف نص تقرير — البرمجة الآمنة\n# استخدمه فقط على جهازك أو على نظام لديك إذن كتابي لاختباره. لا تجمع كلمات مرور أو بيانات شخصية.\n\n"""Secure coding: normalize a line before storing it in a report."""
import re

RAW_LINE = "  finding-182:   review   required  "
clean = re.sub(r"\s+", " ", RAW_LINE).strip()
print({"category": "secure-coding", "normalized": clean})
