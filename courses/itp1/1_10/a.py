x1, y1, x2, y2 = map(float, input().split())
ans = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
print("{0:.5f}".format(ans))