n = int(input())

adj = [[100001 for j in range(n)] for i in range(n)]

for u in range(n):
    x = list(map(int, input().split()))
    for v, c in zip(x[2::2], x[3::2]):
        adj[u][v] = c

print(adj)