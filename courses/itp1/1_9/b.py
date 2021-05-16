while True:
    cards = input()
    if cards == "-":
        break

    m = int(input())
    for i in range(m):
        h = int(input())
        cards = cards[h:] + cards[:h]
    print(cards)
