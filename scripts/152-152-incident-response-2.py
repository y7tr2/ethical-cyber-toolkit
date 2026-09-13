#!/usr/bin/env python3\n# Sanitize a report line — Incident response\n# تنظيف نص تقرير — الاستجابة للحوادث\n# استخدمه فقط على جهازك أو على نظام لديك إذن كتابي لاختباره. لا تجمع كلمات مرور أو بيانات شخصية.\n\n"""Incident response: normalize a line before storing it in a report."""
import re

RAW_LINE = "  finding-152:   review   required  "
clean = re.sub(r"\s+", " ", RAW_LINE).strip()
print({"category": "incident-response", "normalized": clean})
