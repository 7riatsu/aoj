l = input().split(' ')
l = list(map(int, l))
W = l[0]
H = l[1]
x = l[2]
y = l[3]
r = l[4]

if x+r <= W and x-r >= 0 and y+r <= H and y-r >= 0:
    print("Yes")
else:
    print("No")