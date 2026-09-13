#!/usr/bin/env python3\n# Summarize check results — Cryptography\n# حساب نسبة النتائج — التشفير والتجزئة\n# استخدمه فقط على جهازك أو على نظام لديك إذن كتابي لاختباره. لا تجمع كلمات مرور أو بيانات شخصية.\n\n"""Cryptography: summarize local check outcomes."""
from collections import Counter

statuses = ["ok", "ok", "review", "ok", "review"]
summary = Counter(statuses)
total = len(statuses)
print({"category": "crypto", "total": total, "ok_percent": round(summary["ok"] / total * 100, 1)})
