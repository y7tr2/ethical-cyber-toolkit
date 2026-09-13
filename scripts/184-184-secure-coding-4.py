#!/usr/bin/env python3\n# Read JSON safely — Secure coding\n# قراءة JSON بأمان — البرمجة الآمنة\n# استخدمه فقط على جهازك أو على نظام لديك إذن كتابي لاختباره. لا تجمع كلمات مرور أو بيانات شخصية.\n\n"""Secure coding: parse known JSON fields and ignore unknown input."""
import json

raw = '{"check": "secure-coding-184", "status": "review", "extra": "ignored"}'
record = json.loads(raw)
safe_view = {"check": str(record.get("check", "")), "status": str(record.get("status", ""))}
print(safe_view)
