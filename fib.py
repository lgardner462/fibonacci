#!/usr/bin/python

def fib(n):
	if n ==1:
		return 1
	elif n == 0:
		return 0
	else:
		return fib(n-1)+fib(n-2)

x=int(input("Fib(n) n=?\n"))
z=fib(x)
print
print(z)


