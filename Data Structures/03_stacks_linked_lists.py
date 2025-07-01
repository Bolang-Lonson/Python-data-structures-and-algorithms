'''A linked list consists of nodes with some sort of data, and a pointer to the next node.
A big benefit with using linked lists is that nodes are stored wherever there is free space in memory, the nodes do not have to be stored contiguously right after each other like elements are stored in arrays
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        popped_node = self.head
        self.head = self.head.next
        self.size -= 1
        return popped_node.value

    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.head.value

    def isEmpty(self):
        return self.size == 0

    @property
    def stackSize(self) -> int:
        return self.size

    def traverseAndPrint(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.value, end=" -> ")
            currentNode = currentNode.next
        print()


if __name__ == '__main__':
    # Create a stack
    myStack = Stack()
    myStack.push('A')
    myStack.push('B')
    myStack.push('C')

    print("LinkedList: ", end="")
    myStack.traverseAndPrint()
    print("Peek: ", myStack.peek())
    print("Pop: ", myStack.pop())
    print("LinkedList after Pop: ", end="")
    myStack.traverseAndPrint()
    print("isEmpty: ", myStack.isEmpty())
    print("Size: ", myStack.stackSize)

'''Stacks are used in many real-world scenarios:

Undo/Redo operations in text editors
Browser history (back/forward)
Function call stack in programming
Expression evaluation
'''