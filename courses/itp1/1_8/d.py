s = input()
p = input()

for i in range(len(s)):
    if p in s[i:] + s[:i]:
        print("Yes")
        exit()
else:
    print("No")
