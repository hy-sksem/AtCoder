N, A, B = map(int, input().split())

row_color_flag = True
ans = []
for i in range(N):
    row = ""
    for j in range(A):
        column_color_flag = row_color_flag
        for k in range(N):
            for l in range(B):
                row += "." if column_color_flag else "#"
            column_color_flag = not column_color_flag if N != 1 else True
        ans.append(row)
        row = ""
    row_color_flag = False if i % 2 == 0 else True

for i in ans:
    print(i)
