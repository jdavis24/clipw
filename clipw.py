#! /usr/bin/python3.4

from os import urandom
from base64 import b64encode

test = urandom(12)
testout = b64encode(test).decode('utf-8')
print(testout)
