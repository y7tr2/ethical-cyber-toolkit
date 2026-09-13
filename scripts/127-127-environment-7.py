#!/usr/bin/env python3\n# Summarize check results — Environment audit\n# حساب نسبة النتائج — بيئة التشغيل\n# استخدمه فقط على جهازك أو على نظام لديك إذن كتابي لاختباره. لا تجمع كلمات مرور أو بيانات شخصية.\n\n"""Environment audit: summarize local check outcomes."""
from collections import Counter

statuses = ["ok", "ok", "review", "ok", "review"]
summary = Counter(statuses)
total = len(statuses)
print({"category": "environment", "total": total, "ok_percent": round(summary["ok"] / total * 100, 1)})
