n = int(input())
s = list(map(int, input().split()))
q = int(input())
t = list(map(int, input().split()))

cnt = 0
for num in t:
    if num in s:
        cnt += 1

print(cnt)