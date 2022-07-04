# 0-index
def int1(x: int) -> int:
    return int(x) - 1


# 両端キュー
from collections import deque

N, Q = map(int, input().split())
d = deque(input())

d.append()
d.appendleft()
# iterable objectの追加
d.extend()
d.extendleft()
d.insert()

d.pop()
d.popleft()
# 引数に指定した値と等しい最初の要素の削除
d.remove()
# すべての要素の削除 ≒ 空のdeque
d.clear()

# 右に引数分ローテートされる（負の値を渡すと左）
d.rotate()

# 引数に指定した値に一致する最初の要素のindexを返す
d.index()

# maxlenでキューの長さを制限できる。追加すると逆側の要素が削除される
d = deque(input(), maxlen=N)
