#!/usr/bin/env python3


import requests
import os
import sys
import argparse

url = sys.argv[1]
params = open(sys.argv[2], "r")
requesttype = sys.argv[3]

for p in params:
    stripped_line = p.strip()
    httpurl = url + '/' + stripped_line 
    if requesttype == "GET":
      r = requests.get(httpurl, allow_redirects=True)
      status = r.status_code
      reason = r.reason
      if status >= 200 and status <= 299:
        print(r.url + " --> " + str(status) + " " + reason)
      elif status >= 300 and status <= 399:
        print(r.history + " --> " + r.url + str(status) + " " + reason)
      elif status >= 400 and status <= 499:
        print(r.url + " --> " + str(status) + " " + reason)
    elif requesttype == "POST":
      r = requests.post(httpurl, allow_redirects=True)
      status = r.status_code
      reason = r.reason
      if status >= 200 and status <= 299:
        print(r.url + " --> " + str(status) + " " + reason)
      elif status >= 300 and status <= 399:
        print(r.history + " --> " + r.url + str(status) + " " + reason)
      elif status >= 400 and status <= 499:
        print(r.url + " --> " + str(status) + " " + reason)
