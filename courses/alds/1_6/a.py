from itertools import repeat

n = int(input())
arr = list(map(int, input().split()))

max_l = 10001
c = [0] * max_l

for num in arr:
    c[num] += 1

ans = []
for i, num in enumerate(c):
    if num != 0:
        ans.extend(repeat(str(i), num))
print(' '.join(ans))
