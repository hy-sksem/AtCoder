from typing import List, Union, Any, Callable


class SegTree:
    def __init__(
        self,
        op: Callable[[Any, Any], Any],
        e: Any,
        v: Union[int, List[Any]],
    ) -> None:
        self._op = op
        self._e = e

        if isinstance(v, int):
            v = [e] * v

        self._n = len(v)
        self._log = (self._n - 1).bit_length()
        self._size = 1 << self._log
        self._df = [e] * (2 * self._size)
        for i in range(self._n):
            self._df[self._size + i] = v[i]
        for i in range(self._size - 1, 0, -1):
            self._update(i)

    def set(self, p: int, x: Any) -> None:
        assert 0 <= p < self._n

        p += self._size
        self._df[p] = x
        # 親のノードを更新
        for i in range(1, self._log + 1):
            self._update(p >> i)

    def get(self, p: int) -> Any:
        assert 0 <= p < self._n
        return self._df[p + self._size]

    def prod(self, left: int, right: int) -> Any:
        assert 0 <= left <= right <= self._n
        sml, smr = self._e, self._e
        left += self._size
        right += self._size

        while left < right:
            if left & 1:
                sml = self._op(sml, self._df[left])
                left += 1
            if right & 1:
                right -= 1
                smr = self._op(self._df[right], smr)
            left >>= 1
            right >>= 1

        return self._op(sml, smr)

    def all_prod(self) -> Any:
        return self._df[1]

    def max_right(self, left: int, f: Callable[[Any], bool]) -> int:
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
        self._df[k] = self._op(self._df[2 * k], self._df[2 * k + 1])

    def debug(self) -> List[any]:
        """
        デバッグ用
        returns:
            葉を出力
        """
        return self._df[self._size :]
