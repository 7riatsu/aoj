N = int(input())
A = []
D = {}

for i in range(N):
    v, d = input().split()
    A.append((v, int(d)))
    D.setdefault(int(d), []).append(v)

def partition(A, p, r):
    x = A[r]
    i = p
    for j in range(p, r):
        if A[j][1] <= x[1]:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[r] = A[r], A[i]
    return i

def quickSort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q - 1)
        quickSort(A, q + 1, r)

def isStable(A, D):
    D_comp = {}
    for i in range(N):
        v, d = A[i][0], A[i][1]
        D_comp.setdefault(int(d), []).append(v)
    for k, v in D.items():
        if D_comp[k] != D[k]:
            return False
    return True

quickSort(A, 0, N-1)
print("Stable" if isStable(A, D) else "Not stable")
for i in range(len(A)):
    print(*A[i])