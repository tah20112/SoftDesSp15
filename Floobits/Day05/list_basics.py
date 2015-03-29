""" Exploring some basic properties of lists """

def list_sum(L):
	""" Adds up a the numbers in L and returns their sum """
	sum_of_values = 0.0
	for element in L:
		sum_of_values += element
	return sum_of_values

my_list_1 = []                        # an empty list
my_list_2 = [2, 3, 5, 7, 11]          # the first five prime numbers
my_list_3 = [0, 1, -999999, 99999, 'lizard']    # beer orders for a QA engineer
my_list_4 = [0, 1, [2, 5], 3]         # a nested list

print my_list_4[0]
print my_list_4[0:2]

print list_sum(my_list_2)