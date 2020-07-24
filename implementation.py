from encrypt import *
from dcrypt import *

from os import getenv,name
from sys import argv

if name != 'nt':
	mode = getenv('MODE')
else:
	mode = input('Enter E/D: ')

print(mode)

if mode == None or mode == 'D':
	residue = open('BUFFile').read()
	for i in range(10):
		residue = decrypt(residue.encode())
	print(residue,file=open('BUFFile','w'))
elif mode == 'E':
	residue = open('BUFFile').read()
	for i in range(10):
		residue = encrypt(residue.encode()).decode()

	print(residue,file=open('BUFFile','w'))