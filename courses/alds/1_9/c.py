from heapq import *

s = []

while True:
    line = input().split()
    if line[0] == "end":
        break
    elif line[0] == "insert":
        heappush(s, -int(line[1]))
    else:
        print(-heappop(s))
