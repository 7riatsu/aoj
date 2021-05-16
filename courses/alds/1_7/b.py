# 参照: https://onlinejudge.u-aizu.ac.jp/solutions/problem/ALDS1_7_B/review/1676314/bs5lNkJ/Python3

class Node:
    def __init__(self, num, left_child, right_child):
        self.id = num
        self.parent = -1
        self.sibling = -1
        self.degree = 0
        self.depth = 0
        self.height = 0
        self.type = 'leaf'
        self.left_child = left_child
        self.right_child = right_child

    def show_info(self):
        print(
            'node {}:'.format(self.id),
            'parent = {},'.format(self.parent),
            'sibling = {},'.format(self.sibling),
            'degree = {},'.format(self.degree),
            'depth = {},'.format(self.depth),
            'height = {},'.format(self.height),
            '{}'.format(self.type)
        )

def set_node(num, parent, sibling, depth):
    if num == -1:
        return - 1
    node = T[num]
    lc = node.left_child
    rc = node.right_child
    node.parent = parent
    node.sibling = sibling
    node.depth = depth
    node.degree = (node.left_child != -1) + (node.right_child != -1)
    if lc != -1 or rc != -1:
        node.type = "internal node"
    node.height = max(set_node(lc, num, rc, depth + 1),
                      set_node(rc, num, lc, depth + 1)) + 1
    return node.height

N = int(input())
T = [None] * N

rt_n = int(N * (N - 1) / 2)

for _ in range(N):
    num, left_child, right_child = list(map(int, input().split()))
    node = Node(num, left_child, right_child)
    T[num] = node
    rt_n -= (max(0, left_child) + max(0, right_child))

# num, parent, sibling, depth
set_node(rt_n, -1, -1, 0)
T[rt_n].type = "root"

for n in T:
    n.show_info()
