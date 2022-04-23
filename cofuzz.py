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
  reason = r.reason
  data = r.status_code
  if r.ok and r.status_code <= 300:
    print(httpurl + " --> " + " " + str(data) + " " + reason)
  elif r.status_code > 300 and r.status_code < 400:
    print(httpurl + " --> " + reason + " " + " " + str(data) + " " + r.url)
  elif r.status_code > 400:
    print(httpurl + " --> " + str(r.status_code))
  elif url == " " or params == " ":
    print('You have not suppplied any input. Please supply arguments for url using http://, and supply a filepath to use as a parameter from a wordlist')
requestfromfile()
