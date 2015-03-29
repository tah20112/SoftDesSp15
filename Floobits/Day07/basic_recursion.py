""" Introduction to recursion """

def sum_of_numbers(n):
	""" Adds up the integers from 1 to n """
	if n == 0:
		return 0
	return n + sum_of_numbers(n-1)

def factorial(n):
	""" returns factorial of n """
	if n == 1:
		return 1
	return n*factorial(n-1)

print factorial(5)