l = input().split(' ')
l = sorted(l)

ans = ""
for i in range(len(l)):
    ans += " " + str(l[i])
ans = ans.lstrip()
print(ans)