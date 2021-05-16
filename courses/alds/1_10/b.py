def matrix_chain_multiplication(n, r, c) -> int:
    for i in range(1, n):
        m[i][i] = 0
    for l in range(2, n):
        for i in range(1, n - l + 1):
            j = i + l - 1
            m[i][j] = float("inf")
            for k in range(i, j - 1):
                pass
    return 0

n = int(input())
for _ in range(n):
    r, c = map(int, input().split())
