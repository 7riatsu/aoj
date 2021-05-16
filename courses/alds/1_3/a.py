s = []

for ele in list(input().split()):
    try:
        ele = int(ele)
    except:
        pass

    if type(ele) == int:
        s.append(ele)
    else:
        n2, n1 = s.pop(), s.pop()
        s.append(eval(str(n1) + ele + str(n2)))
print(s[0])