r, c = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(r)]

r_s = []
c_s = [0] * (c + 1)

for line in matrix:
    r_s.append(sum(line))
    for i, n in enumerate(line):
        c_s[i] += n
c_s[-1] = sum(c_s)

for i, line in enumerate(matrix):
    print(*line, r_s[i])
print(*c_s)