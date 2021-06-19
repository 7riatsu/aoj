class Deque:
    def __init__(self, elms):
        self.elms = []

    def push(self, d, elm):
        if d == 0:
            self.elms.insert(0, elm)
        else:
            self.elms.append(elm)

    def randomAccess(self, pos):
        if len(self.elms) == 0: return
        print(self.elms[pos])

    def pop(self, d):
        if len(self.elms) == 0: return
        if d == 0:
            self.elms.pop(0)
        else:
            self.elms.pop()


if __name__ == '__main__':
    n = int(input())
    lines = [list(map(int, input().split())) for _ in range(n)]
    q = Deque([])

    for line in lines:
        if line[0] == 0:
            q.push(line[1], line[2])
        elif line[0] == 1:
            q.randomAccess(line[1])
        else:
            q.pop(line[1])
