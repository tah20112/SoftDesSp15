""" Introducing some simple concepts with tuples """

def get_positive_and_negative(n):
	""" returns both positive and negative n """
	return (n, -n)

return_value = get_positive_and_negative(5)
print "positive value is", return_value[0]
print "negative value is", return_value[1]

positive_value, negative_value = get_positive_and_negative(7)
print negative_value
print positive_value

L = ['a',2,7]

for i in range(len(L)):
	print L[i]

for elem in L:
	print elem

for i, elem in enumerate(L):
	print i
	print elem