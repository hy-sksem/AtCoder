N, K = map(int, input().split())

reversed_K = int(str(K)[::-1])
if reversed_K < K:
    print(0)
    exit()
ans = set()
while True:
    if K > N and reversed_K > N:
        break
    if K <= N:
        ans.add(K)
        K *= 10
    if reversed_K <= N:
        ans.add(reversed_K)
        reversed_K *= 10
print(len(ans))
