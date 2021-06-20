class Node:
    def __init__(self, prev, next, val):
        self.prev = prev
        self.next = next
        self.val = val

def insert(cur, pos):
    cur.prev.next = cur.prev = cur = Node(cur.prev, cur, pos)
    return cur

def move(cur, d):
    if d > 0:
        for _ in range(d):
            cur = cur.next
    else:
        for _ in range(-d):
            cur = cur.prev
    return cur

def erase(cur):
    cur.next.prev = cur.prev
    cur.prev.next = cur = cur.next
    return cur


if __name__ == '__main__':
    n = int(input())
    queries = [list(map(int, input().split())) for _ in range(n)]

    root = Node(None, None, None)
    cur = root.next = Node(root, None, None)

    ans = []
    C = {0: insert, 1: move, 2: erase}

    for q in queries:
        if q[0] == 2:
            cur = C[q[0]](cur)
        else:
            cur = C[q[0]](cur, q[1])
    it = root.next
    while it.next:
        ans.append(it.val)
        it = it.next

    [print(ele) for ele in ans]