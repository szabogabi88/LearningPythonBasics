# write Fibonacci series up to next
def fib(n):
	""" This is a docstring of function fib()"""
	""" Just type \'from <name of this file without extension .py\' import fib"""
	""" Then call e.g. fib(10) in python interpreter"""
	a=0
	b=1
	while a<n:
		temp=a
		a=b
		b=b+temp
		print(a, end=' ')
	print()

