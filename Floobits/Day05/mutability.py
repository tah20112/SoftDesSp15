""" Exploring list mutability """

def multiply_by_two(L):
	""" multiplies each of the input elements of L by 2 and overwrites
		their value """
	for i, element in enumerate(L):
		L[i] = element*2

L = [1,5]
multiply_by_two(L)
print L