#!/usr/bin/env python3\n# Inspect a local file — Backups\n# فحص ملف محلي — النسخ الاحتياطية\n# استخدمه فقط على جهازك أو على نظام لديك إذن كتابي لاختباره. لا تجمع كلمات مرور أو بيانات شخصية.\n\n"""Backups: inspect metadata for a file you own."""
from pathlib import Path

path = Path("README.md")
if path.exists() and path.is_file():
    stat = path.stat()
    print({"file": str(path), "bytes": stat.st_size, "readable": True})
else:
    print({"file": str(path), "status": "not-found"})
