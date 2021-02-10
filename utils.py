# utils.py
# Math library
# Author: Sébastien Combéfis
# Version: February 8, 2018
from math import sqrt
from numpy import np
def fact(n):
	try:
		if n <= 1:
			raise ValueError
		if n == 0:
			return 1
		else:
			O = 1
			for i in range(2,n+1):
				O = O * i
		return O
	except ValueError:
		print("Oops! That was no valid number. Try again with a positive number")

def roots(a, b, c):

	delta = ((b**2)-(4*a*c))
	try:
		if (delta>0):
			a = -((b+(sqrt(delta)))/2*a)
			b = -((b-(sqrt(delta)))/2*a)
			return a,b
		if (delta == 0 ):
			return (-b/(2*a)),
		else:
			return ()
	except ValueError:
		print("Oops! That was no valid numbers. Try again with a positive combination for delta")

def integrate(function, lower, upper):
	"""Approximates the integral of a fonction between two bounds
	
	Pre: 'function' is a valid Python expression with x as a variable,
		'lower' <= 'upper',
		'function' continuous and integrable between 'lower‘ and 'upper'.
	Post: Returns an approximation of the integral from 'lower' to 'upper'
		of the specified 'function'.

	Hint: You can use the 'integrate' function of the module 'scipy' and
		you'll probably need the 'eval' function to evaluate the function
		to integrate given as a string.
	"""
	try: 
		if (lower<= upper):
			raise Exception
		if ():
			raise Exception
	except Exception: 
		print("")

if __name__ == '__main__':
	print(fact(5))
	print(roots(1, 0, 1))
	print(integrate('x ** 2 - 1', -1, 1))
