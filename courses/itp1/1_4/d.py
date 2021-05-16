N = int(input())
s = list(map(int, input().split()))

print("{} {} {}".format(min(s), max(s), sum(s)))