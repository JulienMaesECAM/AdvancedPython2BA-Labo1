# utils.py
# Math library
# Author: Sébastien Combéfis
# Version: February 8, 2018
from scipy.integrate import quad
from math import sqrt
import numpy as np 

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
	try: 
		if (upper<= lower):
			raise Exception
		res= quad(lambda x: eval(function), lower, upper)
		print (res)
	except Exception: 
		print("Oops! That was no valid input. Try again with a continious function or verify the lower or upper limit")

if __name__ == '__main__':
	print(fact(5))
	print(roots(1, 0, 1))
	print(integrate("x ** 2 - 1", -1, 1))
