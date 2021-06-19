from collections import deque

n = int(input())
lines = [list(input().split()) for _ in range(n)]
q = deque()

for line in lines:
    if line[0] == '0':
        if line[1] == '0':
            q.appendleft(line[2])
        else:
            q.append(line[2])
    elif line[0] == '1':
        if len(q) == '0':
            pass
        else:
            print(q[int(line[1])])
    else:
        if len(q) == '0':
            pass
        else:
            if line[1] == '0':
                q.popleft()
            else:
                q.pop()
