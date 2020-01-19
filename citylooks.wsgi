#! /usr/bin/python3.5
import logging
import sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/var/www/html/citylooks')

from __init__ import app as application
