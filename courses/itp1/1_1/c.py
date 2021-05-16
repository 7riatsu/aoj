l = input().split(' ')
l = list(map(int, l))

h, w = l[0], l[1]

area = h * w
length = 2*h + 2*w

print(str(area)+ " " + str(length))