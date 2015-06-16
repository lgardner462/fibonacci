#!/usr/bin/python

# test
import sys

def fib(n):
	if n ==1:
		return 1
	elif n == 0:
		return 0
	else:
		return fib(n-1)+fib(n-2)

x= int(sys.argv[1])fib
z= fib(x)
print
print(z)


