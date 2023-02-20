#!/usr/bin/env python3
'''''''''''''''''''''''''''''
COPYRIGHT LESTERRRY,
2021

'''''''''''''''''''''''''''''
import sys
from random import shuffle

RED = "\033[31m"
GRN = "\033[32m"
BLD = "\033[1m"
RES = "\033[0m"

def my_except_hook(exctype, value, traceback):
	print(f'{RED + BLD}ERROR:{RES} {value}')
	exit(1)
sys.excepthook = my_except_hook

def rreplace(s, old, new, occurrence):
	li = s.rsplit(old, occurrence)
	return new.join(li)

argv = sys.argv
if len(argv) < 2:
	raise ValueError("no path to file provided")
path = argv[1]
ifile = open(path,'rb')
ofile = open(rreplace(path, '.', "_DOZED.", 1), 'wb')
data = ifile.read(1024*1024)
while data:
	shuffled_data = list(data)
	shuffle(shuffled_data)
	ofile.write(bytes(shuffled_data))
	data = ifile.read(1024*1024)
ofile.close()
ifile.close()
print(f"{GRN + BLD}DOZED{RES} successfully")
