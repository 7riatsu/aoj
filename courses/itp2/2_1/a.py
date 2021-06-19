class Vector:
    def __init__(self, elems):
        self.elems = []

    def pushBack(self, ele):
        self.elems.append(ele)

    def randomAccess(self, pos):
        if len(self.elems) == 0: return
        print(self.elems[pos])

    def popBack(self):
        if len(self.elems) == 0: return
        self.elems.pop()


if __name__ == '__main__':
    n = int(input())
    ans = Vector([])
    lines = [list(map(int, input().split())) for _ in range(n)]

    for line in lines:
        command = line[0]
        if command == 0:
            ans.pushBack(line[1])
        elif command == 1:
            ans.randomAccess(line[1])
        else:
            ans.popBack()