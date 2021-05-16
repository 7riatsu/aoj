for _ in range(51):
    m, f, r = map(int, input().split())
    if m == f and f == r and f == m and m == -1:
        break
    s = m + f

    if m == -1 or f == -1:
        print("F")
        continue

    if s >= 80:
        print("A")
    elif s >= 65 and s < 80:
        print("B")
    elif s >= 50 and s < 65:
        print("C")
    elif s >= 30 and s < 50:
        if r >= 50:
            print("C")
        else:
            print("D")
    elif s < 30:
        print("F")
    else:
        pass
