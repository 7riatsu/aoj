from itertools import combinations as c

while True:
    ans = 0
    n, x = map(int, input().split())
    if n == 0 and x == 0:
        break

    for comb in list(c(list(range(1, n + 1)), 3)):
        if sum(comb) == x:
            ans += 1
    else:
        print(ans)
