'''A Linked List is, as the word implies, a list where the nodes are linked together. Each node contains data and a pointer. The way they are linked together is that each node points to where in the memory the next node is placed.

*Linked List Operations*
Basic things we can do with linked lists are:

-> Traversal
-> Remove a node
-> Insert a node
-> Sort
'''

# Traversing a linked list means to go through the linked list by following the links from one node to the next. We start with the first node in the list, the head node

class Node:
    def __init__(self, data):
        self.data = data
        self.next: Node = None


def traverseAndPrint(head: Node) -> None:
    currNode = head
    while currNode:
        print(currNode.data, end=' -> ')
        currNode = currNode.next
    print("null")

node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

traverseAndPrint(node1)
# Find The Lowest Value in a Linked List. Let's find the lowest value in a singly linked list by traversing it and checking each value.
def findLowestValue(head: Node):
    minVal = head.data
    currNode = head.next
    while currNode:
        if currNode.data < minVal:
            minVal = currNode.data
        currNode = currNode.next

    return minVal

print("The lowest value in the linked list is:", findLowestValue(node1))

'''Delete a Node in a Linked List
If you want to delete a node in a linked list, it is important to connect the nodes on each side of the node before deleting it, so that the linked list is not broken.

So before deleting the node, we need to get the next pointer from the previous node, and connect the previous node to the new next node before deleting the node in between.

Also, it is a good idea to first connect next pointer to the node after the node we want to delete, before we delete it. This is to avoid a 'dangling' pointer, a pointer that points to nothing, even if it is just for a brief moment.

'''
def deleteSpecificNode(head: Node, nodeToDelete: Node) -> Node:
    if head == nodeToDelete:
        return head.next
    
    currNode = head
    while currNode.next and currNode.next != nodeToDelete:
        currNode = currNode.next

    if currNode.next == None:
        return head
    
    currNode.next = currNode.next.next

    return head


print("Before deletion:")
traverseAndPrint(node1)

# Delete node4
node1 = deleteSpecificNode(node1, node4)

print("\nAfter deletion:")
traverseAndPrint(node1)

'''Insert a Node in a Linked List

To insert a node in a linked list we first need to create the node, and then at the position where we insert it, we need to adjust the pointers so that the previous node points to the new node, and the new node points to the correct next node.
'''
def insertNodeAtPosition(head: Node, newNode: Node, position: int) -> Node:
    '''
        Inserts node in linked list at specified position

        params:
            head: head of linked list
            newNode: new node to be inserted
            position: position in linked list to insert
    '''
    if position == 1:
        newNode.next = head
        return newNode
    
    currNode: Node = head
    for _ in range(position - 2):
        if currNode is None:
            break
        currNode = currNode.next

    newNode.next = currNode.next
    currNode.next = newNode
    return head

print("Original list:")
traverseAndPrint(node1)

# Insert a new node with value 97 at position 2
newNode = Node(97)
node1 = insertNodeAtPosition(node1, newNode, 2)

print("\nAfter insertion:")
traverseAndPrint(node1)