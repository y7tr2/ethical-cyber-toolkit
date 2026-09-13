#!/usr/bin/env python3\n# Export JSON evidence — Secret hygiene\n# حفظ بصيغة JSON — منع تسريب الأسرار\n# استخدمه فقط على جهازك أو على نظام لديك إذن كتابي لاختباره. لا تجمع كلمات مرور أو بيانات شخصية.\n\n"""Secret hygiene: export minimal evidence for an authorized review."""
import json
from datetime import datetime, timezone
from pathlib import Path

evidence = {
    "check_id": "secrets-48",
    "collected_at": datetime.now(timezone.utc).isoformat(),
    "scope": "local-or-authorized",
    "notes": "No credentials or payloads are collected",
}
Path("evidence-48.json").write_text(json.dumps(evidence, indent=2), encoding="utf-8")
print("evidence exported with sensitive fields excluded")
