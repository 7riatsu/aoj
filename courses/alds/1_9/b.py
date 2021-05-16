def max_heapify(a, i):
    l = i * 2
    r = i * 2 + 1

    if l <= h and a[l] > a[i]:
        largest = l
    else:
        largest = i
    if r <= h and a[r] > a[largest]:
        largest = r

    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        max_heapify(a, largest)

def build_max_heap(a, h):
    for i in range(h // 2, 0, -1):
        max_heapify(a, i)

h = int(input())
a = [None] + list(map(int, input().split()))

build_max_heap(a, h)

print("", *a[1:])

