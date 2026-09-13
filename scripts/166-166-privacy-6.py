#!/usr/bin/env python3\n# Log a redacted result — Privacy\n# تسجيل نتيجة بدون بيانات حساسة — الخصوصية\n# استخدمه فقط على جهازك أو على نظام لديك إذن كتابي لاختباره. لا تجمع كلمات مرور أو بيانات شخصية.\n\n"""Privacy: log a result after removing sensitive fields."""
import json
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
result = {"check": "privacy-166", "status": "ok", "token": "REDACTED"}
logging.info("check_result=%s", json.dumps(result, sort_keys=True))
