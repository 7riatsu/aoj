l = input()
s1 = []
s2 = []
ans = 0

for k, v in enumerate(l):
    if v == "\\":
        s1.append(k)
    elif v == "/" and s1:
        j = s1.pop()
        a = k - j
        ans += a

        while s2 and s2[-1][0] > j:
            a += s2.pop()[1]
        s2.append((j, a))

print(ans)
print(len(s2), *(a for j, a in s2))
