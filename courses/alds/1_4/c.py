d = set()
results = []

n = int(input())
for i in range(n):
    command, s = map(str, input().split())
    if command == 'insert':
        d.add(s)
    else:
        if s in d:
            results.append('yes')
        else:
            results.append('no')

for result in results:
    print(result)