n, k = map(int, input().split())

arr = [int(input()) for _ in range(n)]

def check(load_list, P):
    i = 0
    for j in range(k):
        weight = 0
        while weight + load_list[i] <= P:
            weight += load_list[i]
            i += 1
            if i == n:
                return True
    return False

left = 0
right = 100_000 * 100_00

while left + 1 < right:
    mid = (left + right) // 2
    if check(arr, mid):
        right = mid
    else:
        left = mid
print(right)