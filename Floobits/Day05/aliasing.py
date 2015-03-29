""" Exploring the concept of aliasing """

x = 5
y = 4
print x
x = y
y = y + 1
print x

x_list = [5]
y_list = [4]
print x_list
x_list = y_list
y_list[0] = y_list[0] + 1
print x_list