def partition(a, p, r):
    x = a[r]
    i = p - 1
    for j in range(p, r):
        if a[j] <= x:
            i += 1
            a[i], a[j] = a[j], a[i]

    a[i + 1], a[r] = a[r], a[i + 1]
    return i + 1

n = int(input())
arr = list(map(int, input().split()))

j = partition(arr, 0, n - 1)
print(*(str(x) if i != j else "[%d]" % x for i, x in enumerate(arr)))