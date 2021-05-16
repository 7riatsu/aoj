arr = []

while True:
    try:
        s = input()
        if s == "END_OF_TEXT":
            break
        arr.append(s.lower())
    except EOFError:
        break

cnt = 0
tar = arr[0]
del arr[0]

arr = [line.split() for line in arr]

for line in arr:
    for ele in line:
        if ele == tar:
            cnt += 1

print(cnt)
