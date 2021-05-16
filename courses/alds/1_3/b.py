from collections import deque

n, q = map(int, input().split())
d = deque()

for _ in range(n):
    name, time = input().split(); time = int(time)
    d.append((name, time))

ans = []
cnt = 0

while d:
    name, time = d.popleft()
    if time <= q:
        cnt += time
        ans.append("%s %d" % (name, cnt))
    else:
        cnt += q
        d.append((name, time - q))

print(*ans, sep="\n")