t = input()
p = input()

for i in range(len(t) - len(p) + 1):
    if p == t[i: i + len(p)]:
        print(i)
