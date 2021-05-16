# 参照: https://onlinejudge.u-aizu.ac.jp/solutions/problem/ALDS1_7_C/review/1680736/bs5lNkJ/Python3

class BinaryTree:
    class Node:
        def __init__(self, num, left_child, right_child):
                self.num = num
                self.left_child = left_child
                self.right_child = right_child

    def __init__(self, num):
        self.nodes = [None] * num
        self.root_id = int(num * (num - 1) / 2)

    def add_node(self, num, left_child, right_child):
        self.nodes[num] = BinaryTree.Node(num, left_child, right_child)
        if left_child != -1:
            self.root_id -= left_child
        if right_child != -1:
            self.root_id -= right_child

    def preorder_walk(self):
        print("Preorder")
        def _pre_order(node_id):
            if node_id != -1:
                print(" {0}".format(node_id), end = "")
                _pre_order(self.nodes[node_id].left_child)
                _pre_order(self.nodes[node_id].right_child)
        _pre_order(self.root_id)
        print("")

    def inorder_walk(self):
        print("Inorder")
        def _in_order(node_id):
            if node_id != -1:
                _in_order(self.nodes[node_id].left_child)
                print(" {0}".format(node_id), end = "")
                _in_order(self.nodes[node_id].right_child)
        _in_order(self.root_id)
        print("")

    def postorder_walk(self):
        print("Postorder")
        def _post_order(node_id):
            if node_id != -1:
                _post_order(self.nodes[node_id].left_child)
                _post_order(self.nodes[node_id].right_child)
                print(" {0}".format(node_id), end="")
        _post_order(self.root_id)
        print("")

N = int(input())

BT = BinaryTree(N)
for i in range(N):
    num, left_child, right_child = map(int, input().split())
    BT.add_node(num, left_child, right_child)

BT.preorder_walk()
BT.inorder_walk()
BT.postorder_walk()

for node in BT.nodes:''
    print(node.num, left_child, right_child)
