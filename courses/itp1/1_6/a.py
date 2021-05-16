N = int(input())
s = list(map(int, input().split()))

ans_str = ""
for i in s[::-1]:
    ans_str += str(i) + " "
print(ans_str.strip())