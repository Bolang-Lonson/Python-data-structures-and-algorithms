# A queue is a linear data structure that follows the First-In-First-Out (FIFO) principle.

'''Think of a queue as people standing in line in a supermarket.

The first person to stand in line is also the first who can pay and leave the supermarket.

Basic operations we can do on a queue are:

-> Enqueue: Adds a new element to the queue.
-> Dequeue: Removes and returns the first (front) element from the queue.
-> Peek: Returns the first element in the queue.
-> isEmpty: Checks if the queue is empty.
-> Size: Finds the number of elements in the queue.

Queues can be implemented by using arrays or linked lists.
Queues can be used to implement job scheduling for an office printer, order processing for e-tickets, or to create algorithms for breadth-first search in graphs.

'''

# Using a Python list as a queue:
queue = []

# Enqueue
queue.append('A')
queue.append('B')
queue.append('C')
print("Queue: ", queue)

# Peek
frontElement = queue[0]
print("Peek: ", frontElement)

# Dequeue
poppedElement = queue.pop(0)
print("Dequeue: ", poppedElement)

print("Queue after Dequeue: ", queue)

# isEmpty
isEmpty = not bool(queue)
print("isEmpty: ", isEmpty)

# Size
print("Size: ", len(queue))

# ************************* Here's a complete implementation of a Queue class: ****************************

class Queue:
	'''Creates queue object that follows the First-In-First-Out (FIFO) principle
	
		Author:
			Bolang-Lonson
	'''
	def __init__(self):
		self.queue = []

	@property
	def size(self) -> int:
		'''number of elements in the queue'''
		return len(self.queue)
	
	@property
	def isEmpty(self) -> bool:
		'''True if queue has no elements,\n
		False if queue has atleast one element
		'''
		return bool(self.size)

	def enqueue(self, element):
		'''Adds element to end of the queue'''
		self.queue.append(element)

	def dequeue(self):
		'''Removes first element in queue'''
		if self.isEmpty:
			return 'Queue is empty'
		return self.queue.pop()
	
	def peek(self):
		'''Peek at the first element in the queue'''
		if self.isEmpty:
			return 'Queue is empty'
		return self.queue[0]
	

if __name__ == '__main__':
	# Create a queue
	myQueue = Queue()

	myQueue.enqueue('A')
	myQueue.enqueue('B')
	myQueue.enqueue('C')

	print("Queue: ", myQueue.queue)
	print("Peek: ", myQueue.peek())
	print("Dequeue: ", myQueue.dequeue())
	print("Queue after Dequeue: ", myQueue.queue)
	print("isEmpty: ", myQueue.isEmpty)
	print("Size: ", myQueue.size)


'''Queues are used in many real-world scenarios:

Task scheduling in operating systems
Breadth-first search in graphs
Message queues in distributed systems'''