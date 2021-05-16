n = int(input())
adj = [None]

for i in range(n):
    adj_i = list(map(int, input().split()[2:]))
    adj.append(adj_i)

is_searched = [None] + [False] * n
distance = [None] + [-1] * n

def bfs(u):
    d = 0
    is_searched[u] = True
    distance[u] = d
    edge = [u]
    while edge:
        q = list(edge)
        edge = []
        d += 1
        for c_e in q:
            for n_e in adj[c_e]:
                if not is_searched[n_e]:
                    is_searched[n_e] = True
                    edge.append(n_e)
                    distance[n_e] = d


bfs(1)

for k, v in enumerate(distance[1:], start=1):
    print(k, v)
