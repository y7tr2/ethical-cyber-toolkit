#!/usr/bin/env python3\n# Read JSON safely — JSON & data\n# قراءة JSON بأمان — JSON والبيانات\n# استخدمه فقط على جهازك أو على نظام لديك إذن كتابي لاختباره. لا تجمع كلمات مرور أو بيانات شخصية.\n\n"""JSON & data: parse known JSON fields and ignore unknown input."""
import json

raw = '{"check": "json-data-94", "status": "review", "extra": "ignored"}'
record = json.loads(raw)
safe_view = {"check": str(record.get("check", "")), "status": str(record.get("status", ""))}
print(safe_view)
