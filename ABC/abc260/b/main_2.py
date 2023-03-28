N, X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

AB = [(a, b, i + 1) for i, (a, b) in enumerate(zip(A, B))]
AB.sort(key=lambda x: x[0], reverse=True)  # aの得点が高い順にソート
ans = []
for j in range(X):
    ans.append(AB[j][2])
AB = AB[X:]  # 合格したx人を除く
AB.sort(key=lambda x: x[2])  # 番号順にソート
AB.sort(key=lambda x: x[1], reverse=True)  # bの得点が高い順にソート
for j in range(Y):
    ans.append(AB[j][2])
AB = AB[Y:]  # 合格したy人を除く
AB.sort(key=lambda x: x[2])  # 番号順にソート
AB.sort(key=lambda x: x[1] + x[0], reverse=True)  # a+bの得点が高い順にソート
for j in range(Z):
    ans.append(AB[j][2])

ans.sort()
for a in ans:
    print(a)
