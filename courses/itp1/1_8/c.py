d = {}
a_range = range(ord('a'), ord('z') + 1)
for i in a_range:
    d[i] = 0

while True:
    try:
        s = input()
    except EOFError:
        break

    for char in s:
        if char.isupper():
            char = char.lower()
        if not ord(char) in a_range:
            continue

        d[ord(char)] += 1

for k, v in d.items():
    print(str(chr(k)) + " : " + str(v))

