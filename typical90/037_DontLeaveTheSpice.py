from typing import List, Union, Any, Callable


class SegTree:
    """
    SegmentTreeクラス
    """

    def __init__(
        self,
        op: Callable[[Any, Any], Any],
        e: Any,
        v: Union[int, List[Any]],
    ) -> None:
        """
        SegmentTreeクラスのプロパティ
        args:
            op: 演算
            e: 単位元
            v: 対象の列
        """
        self._op = op
        self._e = e

        if isinstance(v, int):
            v = [e] * v

        self._n = len(v)  # 対象の列の要素数
        self._log = (self._n - 1).bit_length()  # n以上で2の冪乗となる最小値(木の高さ)
        self._size = 1 << self._log  # 葉の数
        self._df = [e] * (2 * self._size)  # 2 * 葉の数の要素を持つ一次元配列

        # 葉に値をセット
        for i in range(self._n):
            self._df[self._size + i] = v[i]
        # 葉以外のノードを更新
        for i in range(self._size - 1, 0, -1):
            self._update(i)

    def set(self, p: int, x: Any) -> None:
        """
        p番目の要素をxに変更する
        args:
            p: 位置
            x: 値
        """
        # assert 0 <= p < self._n

        p += self._size
        self._df[p] = x
        # 親のノードを更新
        for i in range(1, self._log + 1):
            self._update(p >> i)

    def get(self, p: int) -> Any:
        """
        葉のp番目の要素を返す
        args:
            p: 位置
        returns:
            p番目の要素
        """
        # assert 0 <= p < self._n
        return self._df[p + self._size]

    def prod(self, left: int, right: int) -> Any:
        """
        leftからrightまでの積を返す
        args:
            left: 左端
            right: 右端
        returns:
            leftからrightまでの積
        """

        # assert 0 <= left <= right <= self._n
        sml, smr = self._e, self._e
        left += self._size
        right += self._size

        while left < right:
            # 自身が右子ノードの場合
            if left & 1:
                sml = self._op(sml, self._df[left])
                left += 1
            if right & 1:
                right -= 1
                smr = self._op(self._df[right], smr)
            # 親へ移動
            left >>= 1
            right >>= 1

        return self._op(sml, smr)

    def all_prod(self) -> Any:
        """
        全ての積を返す
        returns:
            全ての積
        """
        return self._df[1]

    def max_right(self, left: int, f: Callable[[Any], bool]) -> int:
        """
        leftから右端までの最大の要素を返す
        args:
            left: 左端
            f: 条件
        returns:
            leftから右端までの最大の要素
        """
        assert 0 <= left <= self._n
        assert f(self._e)

        if left == self._n:
            return self._n

        left += self._size
        sm = self._e

        first = True
        while first or (left & -left) != left:
            first = False
            while left % 2 == 0:
                left >>= 1
            if not f(self._op(sm, self._df[left])):
                while left < self._size:
                    left *= 2
                    if f(self._op(sm, self._df[left])):
                        sm = self._op(sm, self._df[left])
                        left += 1
                return left - self._size
            sm = self._op(sm, self._df[left])
            left += 1

        return self._n

    def min_left(self, right: int, f: Callable[[Any], bool]) -> int:
        """
        rightから左端までの最小の要素を返す
        args:
            right: 右端
            f: 条件
        returns:
            rightから左端までの最小の要素
        """
        assert 0 <= right <= self._n
        assert f(self._e)

        if right == 0:
            return 0

        right += self._size
        sm = self._e

        first = True
        while first or (right & -right) != right:
            first = False
            right -= 1
            while right > 1 and right % 2:
                right >>= 1
            if not f(self._op(self._df[right], sm)):
                while right < self._size:
                    right = 2 * right + 1
                    if f(self._op(self._df[right], sm)):
                        sm = self._op(self._df[right], sm)
                        right -= 1
                return right + 1 - self._size
            sm = self._op(self._df[right], sm)

        return 0

    def _update(self, k: int) -> None:
        """
        k番目の要素の左子ノードと右子ノードのopをk番目の要素に適用する
        args:
            k: 位置
        """
        self._df[k] = self._op(self._df[2 * k], self._df[2 * k + 1])

    def debug(self) -> List[any]:
        """
        デバッグ用
        returns:
            葉を出力
        """
        return self._df[self._size :]


W, N = map(int, input().split())
inf = 1 << 60
st = SegTree(max, -inf, W + 1)
st.set(0, 0)

for i in range(N):
    l, r, v = map(int, input().split())
    for j in range(W, l - 1, -1):
        sum_values = st.prod(max(0, j - r), j - l + 1)
        if st.get(j) < sum_values + v:
            st.set(j, sum_values + v)
print(max(-1, st.get(W)))
