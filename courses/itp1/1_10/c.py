while True:
    n = int(input())
    if n == 0:
        break
    s = list(map(int, input().split()))

    avg = sum(s) / len(s)

    om = 0
    for ele in s:
        om += (ele - avg) ** 2

    print((om / n) ** 0.5)