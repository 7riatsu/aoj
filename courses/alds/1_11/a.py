n = int(input())

matrix = [[0 for i in range(n)] for i in range(n)]

for i in range(n):
    line = list(map(int, input().split()))
    u, k, vs = line[0], line[1], line[2:]
    for v in vs:
        matrix[i][v - 1] = 1

for line in matrix:
    print(*line)