#!/usr/bin/env python3\n# Inspect a local file — Monitoring\n# فحص ملف محلي — المراقبة والتنبيه\n# استخدمه فقط على جهازك أو على نظام لديك إذن كتابي لاختباره. لا تجمع كلمات مرور أو بيانات شخصية.\n\n"""Monitoring: inspect metadata for a file you own."""
from pathlib import Path

path = Path("README.md")
if path.exists() and path.is_file():
    stat = path.stat()
    print({"file": str(path), "bytes": stat.st_size, "readable": True})
else:
    print({"file": str(path), "status": "not-found"})
