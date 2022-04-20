#!/usr/bin/env python3


import requests
import os
import sys
import argparse

url = sys.argv[1]
params = sys.argv[2]
httpurl = url + '/' + params


def requestfromfile():
  r = requests.get(httpurl, allow_redirects=True)

  data = r.status_code
  if r.ok and r.status_code <= 300:
    print(httpurl + " --> " + " " + str(r.status_code) + " " + r.reason)
  elif r.status_code > 300 and r.status_code < 400:
    print(httpurl + " --> " + r.reason + " " + " " + str(r.status_code) + " " + r.url)
  elif r.status_code > 400:
    print(httpurl + " --> " + str(r.status_code))

requestfromfile()
