#!/usr/bin/env python3\n# Export JSON evidence — Backups\n# حفظ بصيغة JSON — النسخ الاحتياطية\n# استخدمه فقط على جهازك أو على نظام لديك إذن كتابي لاختباره. لا تجمع كلمات مرور أو بيانات شخصية.\n\n"""Backups: export minimal evidence for an authorized review."""
import json
from datetime import datetime, timezone
from pathlib import Path

evidence = {
    "check_id": "backups-148",
    "collected_at": datetime.now(timezone.utc).isoformat(),
    "scope": "local-or-authorized",
    "notes": "No credentials or payloads are collected",
}
Path("evidence-148.json").write_text(json.dumps(evidence, indent=2), encoding="utf-8")
print("evidence exported with sensitive fields excluded")
