# INPUTを降順にソート
N=sorted(input())[::-1]
A=N[0::2] # 奇数番目
B=N[1::2] # 偶数番目
for i in range(min(len(A),len(B))):
	if A[i]!=B[i]:
		A[i],B[i]=B[i],A[i]
		break
print(int("".join(A))*int("".join(B)))