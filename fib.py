#!/usr/bin/python

import sys
import platform



def fib(n):
	if n ==1:
		return 1
	elif n == 0:
		return 0
	else:
		return fib(n-1)+fib(n-2)

x= int(sys.argv[1])
z= fib(x)
print(z)
print(platform.node())
print("abc")

