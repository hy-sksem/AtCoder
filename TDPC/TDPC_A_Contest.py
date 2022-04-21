# https://atcoder.jp/contests/tdpc/tasks/tdpc_contest

N = int(input())
P = list(map(int, input().split()))

num_list = [0]*(100*1000)
num_list[0] = 1
for p in P:
    for j in range(N * 100 + 1, 0, -1):
        if j >= p:
            if num_list[j-p] == 1:
                num_list[j] = 1 
print(sum(num_list))