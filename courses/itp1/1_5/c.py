while True:
    H,W = map(int, input().split())
    if H == 0 or W == 0:
        break
    for i in range(H):
        if i == 0:
            line = "#"
            for j in range(W-1):
                if j % 2 == 0:
                    line += "."
                else:
                    line += "#"
            print(line)
        elif i % 2 == 1:
            line = "."
            for j in range(W-1):
                if j % 2 == 0:
                    line += "#"
                else:
                    line += "."
            print(line)
        elif i % 2 == 0:
            line = "#"
            for j in range(W-1):
                if j % 2 == 0:
                    line += "."
                else:
                    line += "#"
            print(line)
    print()