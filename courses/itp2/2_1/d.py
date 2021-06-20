def pushBack(t, x):
    t.append(x)

def dump(t):
    ans = ""
    for ele in t:
        ans += str(ele) + " "
    print(ans.strip())

def clear(t):
    t.clear()


n, q = map(int, input().split())
queries = [list(map(int, input().split())) for _ in range(q)]
A = [[] for _ in range(n)]

for q in queries:
    if q[0] == 0:
        pushBack(A[q[1]], q[2])
    elif q[0] == 1:
        dump(A[q[1]])
    else:
        clear(A[q[1]])