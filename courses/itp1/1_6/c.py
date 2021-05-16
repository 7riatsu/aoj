n = int(input())

# この書き方はNG. 同じオブジェクトが共有されているので一つだけ代入することができない.
# ans = [[[0] * 10] * 3] * 4

# リスト内包表記を利用すると解決できる(参照: https://note.nkmk.me/python-list-initialize/)
ans = [[[0] * 10 for i in range(3)] for j in range(4)]

for _ in range(n):
    b, f, r, v = map(int, input().split())
    ans[b - 1][f - 1][r - 1] += v

for (i, building) in enumerate(ans):
    for floor in building:
        print(" " + " ".join(map(str, floor)))
    if i != len(ans) - 1:
        print("#" * 20)