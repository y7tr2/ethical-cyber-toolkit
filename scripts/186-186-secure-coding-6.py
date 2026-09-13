#!/usr/bin/env python3\n# Log a redacted result — Secure coding\n# تسجيل نتيجة بدون بيانات حساسة — البرمجة الآمنة\n# استخدمه فقط على جهازك أو على نظام لديك إذن كتابي لاختباره. لا تجمع كلمات مرور أو بيانات شخصية.\n\n"""Secure coding: log a result after removing sensitive fields."""
import json
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
result = {"check": "secure-coding-186", "status": "ok", "token": "REDACTED"}
logging.info("check_result=%s", json.dumps(result, sort_keys=True))
