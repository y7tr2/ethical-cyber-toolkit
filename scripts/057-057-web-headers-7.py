#!/usr/bin/env python3\n# Summarize check results — Web headers\n# حساب نسبة النتائج — رؤوس الويب\n# استخدمه فقط على جهازك أو على نظام لديك إذن كتابي لاختباره. لا تجمع كلمات مرور أو بيانات شخصية.\n\n"""Web headers: summarize local check outcomes."""
from collections import Counter

statuses = ["ok", "ok", "review", "ok", "review"]
summary = Counter(statuses)
total = len(statuses)
print({"category": "web-headers", "total": total, "ok_percent": round(summary["ok"] / total * 100, 1)})
