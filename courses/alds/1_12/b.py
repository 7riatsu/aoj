n = int(input())

adj = [[100001 for j in range(n)] for i in range(n)]

for u in range(n):
    x = list(map(int, input().split()))
    for v, c in zip(x[2::2], x[3::2]):
        adj[u][v] = c

INF_NUM = 9900001
unvisited = [v for v in range((n))]
distance = [INF_NUM] * n


def dijkstra(s):
    distance[s] = 0

    while True:
        mincost = INF_NUM
        for i in unvisited:
            if distance[i] < mincost:
                mincost = distance[i]
                u = i
        if mincost == INF_NUM:
            break

        unvisited.remove(u)

        for v in unvisited:
            weight_uv = adj[u][v]
            if weight_uv != 100001:
                t_d = distance[u] + weight_uv
                if t_d < distance[v]:
                    distance[v] = t_d

dijkstra(0)

for v, d in enumerate(distance):
    print(v, d)
