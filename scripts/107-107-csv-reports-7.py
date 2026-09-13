#!/usr/bin/env python3\n# Summarize check results — CSV & reports\n# حساب نسبة النتائج — CSV والتقارير\n# استخدمه فقط على جهازك أو على نظام لديك إذن كتابي لاختباره. لا تجمع كلمات مرور أو بيانات شخصية.\n\n"""CSV & reports: summarize local check outcomes."""
from collections import Counter

statuses = ["ok", "ok", "review", "ok", "review"]
summary = Counter(statuses)
total = len(statuses)
print({"category": "csv-reports", "total": total, "ok_percent": round(summary["ok"] / total * 100, 1)})
