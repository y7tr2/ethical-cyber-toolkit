#!/usr/bin/env python3\n# Log a redacted result — Secret hygiene\n# تسجيل نتيجة بدون بيانات حساسة — منع تسريب الأسرار\n# استخدمه فقط على جهازك أو على نظام لديك إذن كتابي لاختباره. لا تجمع كلمات مرور أو بيانات شخصية.\n\n"""Secret hygiene: log a result after removing sensitive fields."""
import json
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
result = {"check": "secrets-46", "status": "ok", "token": "REDACTED"}
logging.info("check_result=%s", json.dumps(result, sort_keys=True))
