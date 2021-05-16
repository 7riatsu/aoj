# def isPrime(num):
#     if num <= 1:
#         return False

#     for i in range(2, num - 1):
#         if num % i == 0:
#             return False
#     return True

def isPrime(num):
    if num == 2:
        return True
    elif num <= 1 or num % 2 == 0:
        return False
    else:
        next

    for i in range(3, int(num ** 0.5 + 1)):
        if num % i == 0:
            return False

    return True


n = int(input())
ans = 0

for _ in range(n):
    num = int(input())
    if isPrime(num):
        ans += 1
print(ans)