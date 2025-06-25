# Empty list
x = []

# List with initial values
y = [1, 2, 3, 4, 5]

# List with mixed types
z = [1, "hello", 3.14, True]

'''List Methods'''
x = [9, 12, 7, 4, 11]

# Add element:
x.append(8)

# Sort list ascending:
x.sort()

'''Create Algorithms
Sometimes we want to perform actions that are not built into Python.

Then we can create our own algorithms.

For example, an algorithm can be used to find the lowest value in a list, like in the example below:
'''
my_array = [7, 12, 9, 4, 11, 8]
minVal = my_array[0]

for i in my_array:
  if i < minVal:
    minVal = i

print('Lowest value:', minVal)

'''The algorithm above is very simple, and fast enough for small data sets, but if the data is big enough, any algorithm will take time to run.

This is where optimization comes in.

Optimization is an important part of algorithm development, and of course, an important part of DSA programming.

'''