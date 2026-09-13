#!/usr/bin/env python3\n# Log a redacted result — JSON & data\n# تسجيل نتيجة بدون بيانات حساسة — JSON والبيانات\n# استخدمه فقط على جهازك أو على نظام لديك إذن كتابي لاختباره. لا تجمع كلمات مرور أو بيانات شخصية.\n\n"""JSON & data: log a result after removing sensitive fields."""
import json
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
result = {"check": "json-data-96", "status": "ok", "token": "REDACTED"}
logging.info("check_result=%s", json.dumps(result, sort_keys=True))
