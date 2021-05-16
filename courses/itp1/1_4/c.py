import math
while True:
    arr = input().split()
    a,b,c = int(arr[0]),arr[1],int(arr[2])
    if b == "?":
        break
    elif b == "+":
        print(a+c)
    elif b == "-":
        print(a-c)
    elif b == "*":
        print(a*c)
    elif b == "/":
        print(math.floor((a/c)))