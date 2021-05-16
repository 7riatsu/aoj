n = int(input())

adj = [None]
for i in range(n):
    adj_i = list(map(int, input().split()[2:]))
    adj.append(adj_i)

sndf = [None]
for i in range(1, n + 1):
    sndf.append([False, i])

time = 0

def dfs(u):
    global time
    sndf[u][0] = True
    time += 1

    # Save d
    sndf[u].append(time)

    for v in adj[u]:
        if not sndf[v][0]:
            dfs(v)

    # Save f
    time += 1
    sndf[u].append(time)


for i in range(1, n + 1):
    if not sndf[i][0]:
        dfs(i)

for x in sndf[1:]:
    print(*x[1:])
