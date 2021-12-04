N = input()

ans = N.zfill(3) if int(N) < 42 else str(int(N)+1).zfill(3)
print("AGC"+ans)
