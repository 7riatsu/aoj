class BinarySearchTree:
    def __init__(self):
        self.root = None

    def print_inorder(self):
        def _print_inorder(node):
            if node:
                _print_inorder(node.left)
                print(' {0}'.format(node.key), end = '')
                _print_inorder(node.right)
        _print_inorder(self.root)
        print('')

    def print_preorder(self):
        def _print_preorder(node):
            if node:
                print(' {0}'.format(node.key), end = '')
                _print_preorder(node.left)
                _print_preorder(node.right)
        _print_preorder(self.root)
        print('')

class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

def insert(BT, node):
    y = None
    x = BT.root

    while x != None:
        y = x
        if node.key < x.key:
            x = x.left
        else:
            x = x.right
    node.parent = y

    if y == None:
        BT.root = node
    elif node.key < y.key:
        y.left = node
    else:
        y.right = node

BT = BinarySearchTree()

N = int(input())

# Insert
for i in range(N):
    line = input()
    if line[0] == 'i':
        command, num = map(str, line.split())
        node = Node(int(num))
        insert(BT, node)
    else:
        BT.print_inorder()
        BT.print_preorder()