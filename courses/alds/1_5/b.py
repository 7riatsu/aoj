def merge(A, left, mid, right):
    inf = 10 ** 9
    L = A[left:mid] + [inf]
    R = A[mid:right] + [inf]

    global cnt
    i, j = 0, 0

    for k in range(left, right):
        cnt += 1
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
    return A

def mergeSort(A, left, right):
    if left + 1 < right:
        mid = (left + right) // 2
        mergeSort(A, left, mid)
        mergeSort(A, mid, right)
        merge(A, left, mid, right)
    return A

n = int(input())
A = list(map(int, input().split()))
cnt = 0

mergeSort(A, 0, n)
print(*A)
print(cnt)