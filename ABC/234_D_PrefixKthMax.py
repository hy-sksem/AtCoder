import heapq

N, K = map(int, input().split())
P = list(map(int, input().split()))

que = P[:K]
heapq.heapify(que)
print(que[0])
for i in range(K, N):
    min = heapq.heappop(que)
    min = max(min, P[i])
    heapq.heappush(que, min)
    ans = heapq.heappop(que)
    print(ans)
    heapq.heappush(que, ans)
