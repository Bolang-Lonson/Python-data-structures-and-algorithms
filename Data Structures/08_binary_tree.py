'''A tree is a hierarchical data structure consisting of nodes connected by edges.

Each node contains a value and references to its child nodes.
The Tree data structure can be useful in many cases:

Hierarchical Data: File systems, organizational models, etc.
Databases: Used for quick data retrieval.
Routing Tables: Used for routing data in network algorithms.
Sorting/Searching: Used for sorting data and searching for data.
Priority Queues: Priority queue data structures are commonly implemented using trees, such as binary heaps.

'''
'''Binary Trees: Each node has up to two children, the left child node and the right child node. 
This structure is the foundation for more complex tree types like Binay Search Trees and AVL Trees.

This restriction, that a node can have a maximum of two child nodes, gives us many benefits:

Algorithms like traversing, searching, insertion and deletion become easier to understand, to implement, and run faster.
Keeping data sorted in a Binary Search Tree (BST) makes searching very efficient.
Balancing trees is easier to do with a limited number of child nodes, using an AVL Binary Tree for example.
Binary Trees can be represented as arrays, making the tree more memory efficient.
'''

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left: TreeNode = None
        self.right: TreeNode = None


root = TreeNode('R')
nodeA = TreeNode('A')
nodeB = TreeNode('B')
nodeC = TreeNode('C')
nodeD = TreeNode('D')
nodeE = TreeNode('E')
nodeF = TreeNode('F')
nodeG = TreeNode('G')

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG

# Test
print("root.right.left.data:", root.right.left.data)

'''Types of Binary Trees

-> A balanced Binary Tree has at most 1 in difference between its left and right subtree heights, for each node in the tree.

-> A complete Binary Tree has all levels full of nodes, except the last level, which is can also be full, or filled from left to right. The properties of a complete Binary Tree means it is also balanced.

-> A full Binary Tree is a kind of tree where each node has either 0 or 2 child nodes.

-> A perfect Binary Tree has all leaf nodes on the same level, which means that all levels are full of nodes, and all internal nodes have two child nodes.The properties of a perfect Binary Tree means it is also full, balanced, and complete.

Binary Tree Traversal: 
Going through a Tree by visiting every node, one node at a time, is called traversal.

There are two main categories of Tree traversal methods:

Breadth First Search (BFS) is when the nodes on the same level are visited before going to the next level in the tree. This means that the tree is explored in a more sideways direction.

Depth First Search (DFS) is when the traversal moves down the tree all the way to the leaf nodes, exploring the tree branch by branch in a downwards direction.

There are three different types of DFS traversals:

pre-order
in-order
post-order'''

'''Pre-order Traversal is a type of Depth First Search, where each node is visited in a certain order..

Pre-order Traversal is done by visiting the root node first, then recursively do a pre-order traversal of the left subtree, followed by a recursive pre-order traversal of the right subtree. It's used for creating a copy of the tree, prefix notation of an expression tree, etc.'''

def preOrderTransversal(node):
    if node is None:
        return
    print(node.data, end=', ')
    preOrderTransversal(node.left)
    preOrderTransversal(node.right)

# Test
preOrderTransversal(root)