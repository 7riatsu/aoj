class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n


    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            print("===========")
            print(x, self.parents[x], self.find(self.parents[x]))
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]


    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return - self.parents[self.find(x)]


    def same(self, x, y):
        return self.find(x) == self.find(y)


n, m = map(int, input().split())

uf = UnionFind(n)
for _ in range(m):
    s, t = map(int, input().split())
    uf.union(s, t)

q = int(input())

for _ in range(q):
    s, t = map(int, input().split())
    print("yes" if uf.find(s) == uf.find(t) else "no")
