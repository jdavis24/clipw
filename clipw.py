#! /usr/bin/python3.4

from os import urandom
from base64 import b64encode
import argparse
import random
import string

#leaving the debug checks on the functions for now, while I work some things out

def default():
	gen = urandom(12)
	genout = b64encode(gen).decode('utf-8')
	pw = genout.translate({ord(x): '' for x in '!@#$%^&*()_+-==[]{}<>,./\?`~'})
	print(pw + '  default')
def length(len):
	gen = urandom(len)
	genout = b64encode(gen).decode('utf-8')
	pw = genout.translate({ord(x): '' for x in '!@#$%^&*()_+-=[]{}<>,./\?`~'})
	print(pw + '  length')
def special():
	gen = urandom(12)
	genout = b64encode(gen).decode('utf-8')
	pw = genout.translate({ord(x): '' for x in '!@#$%^&*()_+-=[]{}<>,./\?`~'})
	randchar = random.choice(string.punctuation)
	print(pw + randchar + '  special')

#adding ability to use arguments
parser = argparse.ArgumentParser(description='generates random passwords')

parser.add_argument('-d', action='store_true', help='default behavior - prints 12-byte password') #try default=True again
parser.add_argument('-a', action='store_true', help='secondary test switch')
parser.add_argument('--spec', '-s', action='store_true', help='adds a special character to the default password')
parser.add_argument('--len', '-l', action='store', dest='len', type=int, help='set the length of password provided in bytes')

args = parser.parse_args()

if args.d:
	default()
elif args.a:
	print('a switch worked')
elif args.len:
	length(args.len)
elif args.spec:
	special()

#default random output behavior
#test = urandom(12)
#testout = b64encode(test).decode('utf-8')
#print(testout)
