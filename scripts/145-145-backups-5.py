#!/usr/bin/env python3\n# Write a CSV report — Backups\n# إنشاء تقرير CSV — النسخ الاحتياطية\n# استخدمه فقط على جهازك أو على نظام لديك إذن كتابي لاختباره. لا تجمع كلمات مرور أو بيانات شخصية.\n\n"""Backups: write a small local CSV report."""
import csv
from pathlib import Path

output = Path("security-report-145.csv")
rows = [{"category": "backups", "status": "review", "authorized": "yes"}]
with output.open("w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=rows[0])
    writer.writeheader()
    writer.writerows(rows)
print(f"created {output} with {len(rows)} finding(s)")
