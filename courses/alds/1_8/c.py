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

    def find(self, key):
        if find_from(self.root, key):
            print('yes')
        else:
            print('no')

    def insert(self, key):
        node = Node(key)
        insert(self, node)

    def delete(self, key):
        node = find_from(self.root, key)
        delete(self, node)

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

def delete(BT, node):
    if node.left and node.right:  # nodeが子を2つ以上持つ
        x = node.right
        while x.left:
            x = x.left
        node.key = x.key
        delete(BT, x)
    elif node.left or node.right:  # nodeが子を1つもつ
        child = node.left or node.right
        if node is BT.root:
            BT.root = child
            child.parent = None
        else:
            if node.parent.left is node:
                node.parent.left = child
                child.parent = node.parent
            else:
                node.parent.right = child
                child.parent = node.parent
    else:                         # nodeが子を持たない
        if node.parent.left is node:
            node.parent.left = None
        else:
            node.parent.right = None

def find_from(node, key):
    while node:
        if node.key == key:
            return node
        if key < node.key:
            node = node.left
        else:
            node = node.right
    return None

BT = BinarySearchTree()

N = int(input())

for i in range(N):
    line = input()
    if line[0] == 'i':
        _, key = map(str, line.split())
        BT.insert(int(key))
    elif line[0] == 'p':
        BT.print_inorder()
        BT.print_preorder()
    elif line[0] == 'd':
        _, key = map(str, line.split())
        BT.delete(int(key))
    else:
        _, key = map(str, line.split())
        BT.find(int(key))
