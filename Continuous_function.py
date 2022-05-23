"""This programe checks whether the input function is continuous at a given point."""

from sympy import Symbol, Limit, sympify, S
from sympy.core.sympify import SympifyError

def is_continuous(f, var, value):
	"""Checks whether a function is continuous at a point."""
	var = Symbol(var)

	right_limit = Limit(f, var, value, dir='+').doit()
	left_limit = Limit(f, var, value, dir='-').doit()

	# If the left-hand limit equals to right-hand limit
	# and they do not equal infinity
	# a function is continuous at the point.
	if right_limit == left_limit and right_limit != S.Infinity and right_limit != -S.Infinity:
		print(f"The function is continuous at the point {var} = {value}.")
	else:
		print(f"The function is not continuous at the point {var} = {value}.")

if __name__=='__main__':

	f = input("Enter a function: ")
	var = input("Enter a function variable: ")
	value = input("Enter a point: ")

	try:
		f = sympify(f) #Convert the input function to a SymPy object
	except SympifyError: #Check the correctness of the input
		print("Invalid input")
	else:
		is_continuous(f, var, value)