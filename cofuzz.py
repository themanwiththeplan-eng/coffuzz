#!/usr/bin/env python3


import requests
import os
import sys
import argparse

url = sys.argv[1]
params = open(sys.argv[2], "r")

for p in params:
    stripped_line = p.strip()
    httpurl = url + '/' + stripped_line
    r = requests.get(httpurl, allow_redirects=True)
    status = r.status_code
    reason = r.reason
    if status >= 200 and status <= 299:
      print(r.url + ' --> ' + str(status))
    elif status >= 300 and status <= 399:
      print(r.url + ' --> ' + str(status))
    elif status >= 400 and status <= 499:
      print(r.url + ' --> ' + str(status))
    
requestfromfile()
