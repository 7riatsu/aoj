n = int(input())
s = list(map(int, input().split()))
q = int(input())
t = list(map(int, input().split()))

def binarySearch(tar):
    left = 0
    right = len(s)

    while left < right:
        mid = (right + left) // 2
        if s[mid] == tar:
            return mid
        elif tar < s[mid]:
            right = mid
        else:
            left = mid + 1
    return False

cnt = 0
for num in t:
    if type(binarySearch(num)) == int:
        cnt += 1
    else:
        pass
print(cnt)
