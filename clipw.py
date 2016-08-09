#! /usr/bin/python3.4

from os import urandom
from base64 import b64encode
import argparse

def default():
	gen = urandom(12)
	genout = b64encode(gen).decode('utf-8')
	print(genout)
def length(len):
	gen = urandom(len)
	genout = b64encode(gen).decode('utf-8')
	print(genout)

#adding ability to use arguments
parser = argparse.ArgumentParser()

parser.add_argument('-d', action='store_true', help='default behavior - prints 12-character password') #try default=True again
parser.add_argument('-a', action='store_true', help='secondary test switch')
#parser.add_argument('-l', action='store', dest='len', type=int, help='set the length of password provided')
parser.add_argument('--len', '-l', action='store', dest='len', type=int, help='set the length of password provided')

args = parser.parse_args()

if args.d:
	default()
elif args.a:
	print('a switch worked')
#elif args.l:
#	print(args.len)
#	length(args.len)
elif args.len:
#	print(args.len)
	length(args.len)

#default random output behavior
#test = urandom(12)
#testout = b64encode(test).decode('utf-8')
#print(testout)
