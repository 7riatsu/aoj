cards = []
suits = ['S', 'H', 'C', 'D']

n = int(input())

for i in range(n):
    s, r = input().split()
    r = int(r)
    if s == 'S':
        cards.append(0 + r)
    elif s == 'H':
        cards.append(13 + r)
    elif s == 'C':
        cards.append(26 + r)
    elif s == 'D':
        cards.append(39 + r)

for j in range(1, 53):
    if not j in cards:
        print(suits[(j-1)//13], (j-1)%13+1)