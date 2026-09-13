#!/usr/bin/env python3\n# Read JSON safely — IP & networking\n# قراءة JSON بأمان — الشبكات و IP\n# استخدمه فقط على جهازك أو على نظام لديك إذن كتابي لاختباره. لا تجمع كلمات مرور أو بيانات شخصية.\n\n"""IP & networking: parse known JSON fields and ignore unknown input."""
import json

raw = '{"check": "ip-networking-4", "status": "review", "extra": "ignored"}'
record = json.loads(raw)
safe_view = {"check": str(record.get("check", "")), "status": str(record.get("status", ""))}
print(safe_view)
