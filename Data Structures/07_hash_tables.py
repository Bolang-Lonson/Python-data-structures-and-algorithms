'''We will build the Hash Table in 5 steps:

-> Create an empty list (it can also be a dictionary or a set).
-> Create a hash function.
-> Inserting an element using a hash function.
-> Looking up an element using a hash function.
-> Handling collisions.
'''

# A hash function can be made in many ways, it is up to the creator of the Hash Table. A common way is to find a way to convert the value into a number that equals one of the Hash Table's index numbers, in this case a number from 0 to 9.
def hash_function(value):
	'''In our example we will use the Unicode number of each character, summarize them and do a modulo 10 operation to get index numbers 0-9.'''
	sum_of_chars = 0
	for char in value:
		sum_of_chars += ord(char)

	# The number returned by the hash function is called the hash code.
	return sum_of_chars % 10

print("'Bob' has hash code:", hash_function('Bob'))

'''Step 3: Inserting an Element
According to our hash function, "Bob" should be stored at index 5.

Lets create a function that add items to our hash table:
'''
mylist = [None for _ in range(10)]

def add(name):
	index = hash_function(name)
	mylist[index] = name


add('Bob')

add('Pete')
add('Jones')
add('Lisa')
add('Siri')
print(mylist)

# Step 4: Looking up a name
def contains(name):
  index = hash_function(name)
  return mylist[index] == name

print("'Pete' is in the Hash Table:", contains('Pete'))

'''Step 5: Handling collisions

To fix the collision, we can make room for more elements in the same bucket. Solving the collision problem in this way is called chaining, and means giving room for more elements in the same bucket.

Start by creating a new list with the same size as the original list, but with empty buckets:
'''
my_list = [
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[]
]

# Rewrite the add() function, and add the same names as before:
def add(name):
	index = hash_function(name)
	my_list[index].append(name)

add('Bob')
add('Pete')
add('Jones')
add('Lisa')
add('Siri')
add('Stuart')
print(my_list)