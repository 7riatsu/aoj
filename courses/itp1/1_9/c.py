n = int(input())

t_point = h_point = 0

for _ in range(n):
    t, h = input().split()
    if t > h:
        t_point += 3
    elif h > t:
        h_point += 3
    else:
        t_point += 1
        h_point += 1

print(t_point, h_point)
