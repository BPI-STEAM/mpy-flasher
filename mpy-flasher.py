#!/usr/bin/env python

import sys

from esp.main import run

try:
    run()
except Exception as e:
    sys.stderr.write(str(e) + "\n")
    exit(1)

