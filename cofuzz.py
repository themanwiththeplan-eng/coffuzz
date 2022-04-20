#!/usr/bin/env python3


import requests
import os
import sys
import argparse

wl = sys.argv[2]

url = sys.argv[1]
urlsubstr = 'http://'

if not url:
  print('Please provide a url')
elif not wl:
  print('Please provide a wordlist')
elif wl:
  line = wl.readline()
  print(line.strip())
  if line == "":
    return




if urlsubstr in url:
  print(url + fileread)
else:
  httpurl = urlsubstr + url + fileread
  print(httpurl)


