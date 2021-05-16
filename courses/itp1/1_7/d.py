n, m, l = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
B = [list(map(int, input().split())) for _ in range(m)]

for a in A:
    tmp = [0] * l
    for j, b in enumerate(B):
        for k, num in enumerate(b):
            tmp[k] += a[j] * num
    print(*tmp)
