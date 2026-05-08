#!/usr/bin/env python
import os
import sys
import subprocess

os.chdir(os.path.dirname(os.path.abspath(__file__)))
subprocess.call([sys.executable, 'manage.py', 'runserver'])
