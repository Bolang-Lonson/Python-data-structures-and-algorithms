'''A stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle.
Think of it like a stack of pancakes - you can only add or remove pancakes from the top.

Basic operations we can do on a stack are:

-> Push: Adds a new element on the stack.
-> Pop: Removes and returns the top element from the stack.
-> Peek: Returns the top (last) element on the stack.
-> isEmpty: Checks if the stack is empty.
-> Size: Finds the number of elements in the stack.

Stacks can be implemented by using arrays or linked lists.

Stacks can be used to implement undo mechanisms, to revert to previous states, to create algorithms for depth-first search in graphs, or for backtracking.
'''

stack = []

# Push
stack.append('A')
stack.append('B')
stack.append('C')
print("Stack: ", stack)

# Peek
topElement = stack[-1]
print("Peek: ", topElement)

# Pop
poppedElement = stack.pop()
print("Pop: ", poppedElement)

# Stack after Pop
print("Stack after Pop: ", stack)

# isEmpty
isEmpty = not bool(stack) # empty list has a boolean value of false
print("isEmpty: ", isEmpty)

# Size
print("Size: ",len(stack))

# While Python lists can be used as stacks, creating a dedicated Stack class provides better encapsulation and additional functionality:

class Stack:
    def __init__(self):
        self.stack: list = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.isEmpty():
            return 'Stack is empty'
        return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return 'Stack is empty'
        return self.stack[-1]
    
    def isEmpty(self):
        return self.size == 0
    
    @property
    def size(self) -> int:
        '''size of the stack'''
        return len(self.stack)
    

if __name__ == '__main__':
    # Create a stack
    myStack = Stack()

    myStack.push('A')
    myStack.push('B')
    myStack.push('C')

    print("Stack: ", myStack.stack)
    print("Pop: ", myStack.pop())
    print("Stack after Pop: ", myStack.stack)
    print("Peek: ", myStack.peek())
    print("isEmpty: ", myStack.isEmpty())
    print("Size: ", myStack.size)


'''Stacks are used in many real-world scenarios:

Undo/Redo operations in text editors
Browser history (back/forward)
Function call stack in programming
Expression evaluation
'''