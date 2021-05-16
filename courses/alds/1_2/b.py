def selectionSort(a, n):
    cnt = 0

    for i in range(n):
        minj = i
        for j in range(i, n):
            if a[j] < a[minj]:
                minj = j
        if a[i] != a[minj]:
            a[i], a[minj] = a[minj], a[i]
            cnt += 1

    print(*a)
    print(cnt)
    return

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))

    selectionSort(arr, n)