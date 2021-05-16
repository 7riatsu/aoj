import itertools

n = int(input())
a = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))

l = []
for i in range(1, n + 1):
    l += list(itertools.combinations(a, i))

sum_l = [sum(ele) for ele in l]

for num in m:
    if num in sum_l:
        print('yes')
    else:
        print('no')
