import math

a, b, c = map(int, input().split())

def d(a, b, c) -> float:
    return

def area(a, b, c) -> float:
    return 0.5 * a * b * math.sin(math.radians(c))

def length(a, b, c) -> float:
    tmp = (a ** 2 + b ** 2 - 2 * a * b * math.cos(math.radians(c))) ** 0.5
    return a + b + tmp

def height(a, b, c) -> float:
    return 2 * area(a, b, c) / a

print(area(a, b, c))
print(length(a, b, c))
print(height(a, b, c))
