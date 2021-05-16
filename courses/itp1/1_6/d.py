n, m = map(int, input().split())

a_arr = [list(map(int, input().split())) for _ in range(n)]
b_arr = [int(input()) for _ in range(m)]

for line in a_arr:
    ans = sum([line[i] * b_arr[i] for i in range(m)])
    print(ans)
