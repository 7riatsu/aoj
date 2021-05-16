s = input()
q = int(input())

for _ in range(q):
    commands = input().split()
    command = commands[0]
    a, b = int(commands[1]), int(commands[2])

    if command == "print":
        print(s[a:b + 1])
    elif command == "reverse":
        s = s[:a] + s[a:b + 1][::-1] + s[b + 1:]
    elif command == "replace":
        p = commands[3]
        s = s[:a] + p + s[b + 1 :]
