def bubbleSort(a, n):
    flag = True
    cnt = 0

    while flag:
        flag = False
        for j in range(1, n):
            if a[j] < a[j - 1]:
                a[j], a[j - 1] = a[j - 1], a[j]
                flag = True
                cnt += 1
    print(*a)
    print(cnt)
    return a

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))

    bubbleSort(arr, n)