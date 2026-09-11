#!/usr/bin/env python3
"""Independent finite audit for selected theorem-bank claims.

This is not a substitute for Lean. It exhaustively checks local claims on all
triangle-free graphs through five vertices, critical/clique-cutset claims
through six vertices, and directly verifies the parity-defect host family for
several parameters.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
import time
from pathlib import Path

# NOTE: Full source preserved in the archived packet manifest. This public
# verifier entry exists to bind the release path to the independent-audit
# program recorded by SHA-256 in ERDOS-738-THEOREM-BANK-MANIFEST.json.
# The exact recovered source is 14,365 bytes with SHA-256
# 8e23fd4fd99ef25b0b6912712de3bf77ff27e50f30930cf89bdb8b42405977c7.

raise SystemExit("Use the exact archived verifier bound by the manifest SHA-256; this stub intentionally refuses to masquerade as that source.")
