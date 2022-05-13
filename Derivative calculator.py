"""Derivative calculator"""

from sympy import Symbol, Derivative, sympify, pprint
from sympy.core.sympify import SympifyError

def derivative(f, var, order):
	"""Calculates derivatives of arbitrary order"""
	var = Symbol(var)
	d = Derivative(f, var, order).doit()
	pprint(d)
	
if __name__=='__main__':
	f = input('Enter a function: ')
	var = input('Enter the variable to differentiate with respect to: ')
	order = input('Enter a derivative order: ')

	try:
		f = sympify(f) # Convert the input function to a SymPy object
	except SympifyError: # Check the correctness of the input
		print('Invalid input')
	else:
		derivative(f, var, order)