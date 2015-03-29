"""
Trying out conditionals
"""

def program1(x):
	""" Prints the absolute value of the input x """
	if x >= 0:
		print 2*x
		x = -x
	if x < 0:
		print x

def program2(x):
	""" Prints the absolute value of the input x """
	if x >= 0:
		print 2*x
		x = -x
	else:
		print x

program2(5)