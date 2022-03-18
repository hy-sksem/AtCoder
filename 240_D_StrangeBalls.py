N = int(input())
A = list(map(int, input().split()))

stack = []
ans = 0
for i in range(N):
    ans += 1
    if not stack:
        stack.append([A[i],1])
    elif stack[-1][0] != A[i]:
        stack.append([A[i],1])
    elif stack[-1][1] != A[i]-1:
        stack[-1][1] += 1
    else:
        stack.pop()
        ans -= A[i]
    print(ans)

