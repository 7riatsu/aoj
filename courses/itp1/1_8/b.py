while True:
    i = input()
    if i == "0":
        break

    ans = 0

    for num in i:
        ans += int(num)
    print(ans)
