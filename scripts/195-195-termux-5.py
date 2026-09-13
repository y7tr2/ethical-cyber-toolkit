#!/usr/bin/env python3\n# Write a CSV report — Termux automation\n# إنشاء تقرير CSV — أتمتة Termux\n# استخدمه فقط على جهازك أو على نظام لديك إذن كتابي لاختباره. لا تجمع كلمات مرور أو بيانات شخصية.\n\n"""Termux automation: write a small local CSV report."""
import csv
from pathlib import Path

output = Path("security-report-195.csv")
rows = [{"category": "termux", "status": "review", "authorized": "yes"}]
with output.open("w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=rows[0])
    writer.writeheader()
    writer.writerows(rows)
print(f"created {output} with {len(rows)} finding(s)")
