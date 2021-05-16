# 参照: https://onlinejudge.u-aizu.ac.jp/solutions/problem/ALDS1_7_A/review/1665402/bs5lNkJ/Python3

class Node:
    def __init__(self, num, parent, children):
        self.id = num
        self.parent = -1
        self.depth = 0
        self.type = None
        self.children = children

    def show_info(self):
        print("node {0}: parent = {1}, depth = {2}, {3}, {4}".format(
            self.id,
            self.parent,
            self.depth,
            self.type,
            self.children
        ))

def set_node(num, children):
    node = Node(num, -1, children)
    T[num] = node
    for child in children:
        T[-1] -= child

def set_pdt(num, parent, depth):
    node = T[num]
    node.parent = parent
    node.depth = depth
    if node.children:
        node.type = "internal node"
        for n in node.children:
            set_pdt(n, num, depth + 1)
    else:
        node.type = "leaf"

N = int(input())
T = [None] * N

T.append(int(N * (N - 1) / 2))

for _ in range(N):
    line = list(map(int, input().split()))
    num, k, children = line[0], line[1], line[2:]
    set_node(num, children)

set_pdt(T[-1], -1, 0)

T[T[-1]].type = "root"

for n in T[:-1]:
    n.show_info()
