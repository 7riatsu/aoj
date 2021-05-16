N = int(input())
pre_a = list(map(int, input().split()))
in_a = list(map(int, input().split()))
post_a = []

def post(pre_ele, in_ele):
    if pre_ele:
        root = pre_ele[0]
        root_i = in_ele.index(root)
        pre_left = pre_ele[1: root_i + 1]
        in_left = in_ele[:root_i]
        pre_right = pre_ele[root_i + 1 :]
        in_right = in_ele[root_i + 1 :]
        post(pre_left, in_left)
        post(pre_right, in_right)
        post_a.append(root)

post(pre_a, in_a)
print(*post_a)