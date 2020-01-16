#! /usr/bin/python3.5
import logging
import sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/home/paulsuk/workspace/citylooks')

from citylooks import app as application
