n = int(input())
a = [None] + list(map(int, input().split()))

for i in range(1, n + 1):
    print("node {}: ".format(i), end="")
    print("key = {}, ".format(a[i]), end="")
    if i != 1:
        print("parent key = {}, ".format(a[i // 2]), end="")
    if i * 2 in range(1, n + 1):
        print("left key = {}, ".format(a[i * 2]), end="")
    if i * 2 + 1 in range(1, n + 1):
        print("right key = {}, ".format(a[i * 2 + 1]), end="")
    print("")