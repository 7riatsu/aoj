l = input().split(' ')
l = list(map(int, l))
a = l[0]
b = l[1]
c = l[2]

if a < b and b < c:
    print("Yes")
else:
    print("No")