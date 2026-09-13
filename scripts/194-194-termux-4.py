#!/usr/bin/env python3\n# Read JSON safely — Termux automation\n# قراءة JSON بأمان — أتمتة Termux\n# استخدمه فقط على جهازك أو على نظام لديك إذن كتابي لاختباره. لا تجمع كلمات مرور أو بيانات شخصية.\n\n"""Termux automation: parse known JSON fields and ignore unknown input."""
import json

raw = '{"check": "termux-194", "status": "review", "extra": "ignored"}'
record = json.loads(raw)
safe_view = {"check": str(record.get("check", "")), "status": str(record.get("status", ""))}
print(safe_view)
