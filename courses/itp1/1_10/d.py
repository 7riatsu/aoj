def minkowski_dist(p, x, y):
    ret = 0

    if p == float('inf'):
        for i in range(len(x)):
            ret = max(ret, abs(x[i] - y[i]))
        return ret

    for i in range(len(x)):
        ret += (abs(x[i] - y[i])) ** p
    return ret ** (1 / p)

n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

p = [1, 2, 3, float("inf")]
for ele in p:
    print(minkowski_dist(ele, x, y))
