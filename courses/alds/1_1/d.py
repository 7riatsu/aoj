n = int(input())

mn, ans = 100_000_000_000, -100_000_000_000

for i in range(n):
    num = int(input())
    ans = max(num - mn, ans)
    mn = min(num, mn)
print(ans)