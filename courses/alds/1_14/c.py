"""
# TLE
h, w = map(int, input().split())
mt = [list(input()) for _ in range(h)]
r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]

def is_correct(i, j) -> bool:
    for y, line in enumerate(arr):
        if line != mt[i + y][j: j + c]:
            return False
    return True

for i in range(h - r + 1):
    for j in range(w - c + 1):
        if is_correct(i, j):
            print(i, j)
"""