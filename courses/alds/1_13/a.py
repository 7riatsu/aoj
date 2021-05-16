n = int(input())

ELE_NUM = 8

row = col = [False] * ELE_NUM
dpos = dneg = [False] * (2 * ELE_NUM - 1)

matrix = [["." for i in range(ELE_NUM)] for j in range(ELE_NUM)]

for _ in range(n):
    r, c = map(int, input().split())
    row[r] = True
    col[c] = True
    dpos[r + c] = True
    dneg[r - c + 7] = True
    matrix[r][c] = 'Q'

def dfs(i):
    if i == ELE_NUM - 1:
        for line in matrix:
            print(*line)
    elif row[i]:
        dfs(i + 1)
    else:
        for j in range(ELE_NUM):
            if col[j] or dpos[i + j] or dneg[i - j + 7]:
                continue
            row[i] = True
            col[j] = True
            dpos[i + j] = True
            dneg[i - j + 7] = True
            matrix[i][j] = 'Q'
            dfs(i + 1)
            row[i] = False
            col[j] = False
            dpos[i + j] = False
            dneg[i - j + 7] = False
            matrix[i][j] = '.'


dfs(0)
