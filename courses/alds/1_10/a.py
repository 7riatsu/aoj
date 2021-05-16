# Use recursion
# def fibonacci(n: int) -> int:
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# Use Dynamic Programming
# def fibonacci(n: int) -> int:
#     f = [1, 1]

#     for i in range(2, n + 1):
#         f.append(f[i - 1] + f[i - 2])
#     return f[n]

# Use one variable
def fibonacci(n: int) -> int:
    a = b = 1

    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n + 1):
            c = a + b
            a = b
            b = c
        return b

n = int(input())
print(fibonacci(n))