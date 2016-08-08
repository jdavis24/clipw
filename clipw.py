#! /usr/bin/python3.4

from os import urandom
from base64 import b64encode
import argparse

#adding ability to use arguments
parser = argparse.ArgumentParser()
parser.add_argument('-d', action='store_true', help='default behavior - prints 12-character password')
parser.add_argument('-a', action='store_true', help='secondary test switch')

args = parser.parse_args()

if args.d:
	print('default switch worked')
elif args.a:
	print('a switch worked')
else:
	print('didn\'t work')

#default random output behavior
#test = urandom(12)
#testout = b64encode(test).decode('utf-8')
#print(testout)
