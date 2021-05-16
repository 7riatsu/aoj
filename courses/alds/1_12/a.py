n = int(input())

adj = [list(map(int, input().split())) for i in range(n)]

def prim_mst(n) -> int:
    INF_NUM = 2001
    is_visited = [False] * n
    d = [0] + [INF_NUM] * (n - 1)
    p = [-1] * n

    while True:
        min_cost = INF_NUM
        for i in range(n):
            if (not is_visited[i]) and (d[i] < min_cost):
                min_cost = d[i]
                u = i

        if min_cost == INF_NUM:
            break

        is_visited[u] = True

        for v in range(n):
            if (not is_visited[v]) and (adj[u][v] != -1):
                if adj[u][v] < d[v]:
                    d[v] = adj[u][v]
                    p[v] = u
    return sum(d)


print(prim_mst(n))
