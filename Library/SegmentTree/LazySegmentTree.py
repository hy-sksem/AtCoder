from typing import List, Optional, Union, Any, Callable


def ceil_pow2(n: int) -> int:
    x = 0
    while (1 << x) < n:
        x += 1

    return x


class LazySegmentTree:
    def __init__(
        self,
        op: Callable[[Any, Any], Any],
        e: Any,
        mapping: Callable[[Any, Any], Any],
        composition: Callable[[Any, Any], Any],
        id_: Any,
        v: Union[int, List[Any]],
    ) -> None:
        self.op = op
        self.e = e
        self.mapping = mapping
        self.composition = composition
        self.id = id_

        if isinstance(v, int):
            v = [e] * v

        self.n = len(v)
        self.log = ceil_pow2(self.n)
        self.size = 1 << self.log
        self.data = [self.e] * (2 * self.size)
        self.lazy = [self.id] * self.size
        for i in range(self.n):
            self.data[self.size + i] = v[i]
        for i in range(self.size - 1, 0, -1):
            self._update(i)

    def set(self, p: int, x: Any) -> None:
        assert 0 <= p < self.n

        p += self.size
        for i in range(self.log, 0, -1):
            self._push(p >> i)
        self.data[p] = x
        for i in range(1, self.log + 1):
            self._update(p >> i)

    def get(self, p: int) -> Any:
        assert 0 <= p < self.n

        p += self.size
        for i in range(self.log, 0, -1):
            self._push(p >> i)
        return self.data[p]

    def prod(self, left: int, right: int) -> Any:
        assert 0 <= left <= right <= self.n

        if left == right:
            return self.e

        left += self.size
        right += self.size

        for i in range(self.log, 0, -1):
            if ((left >> i) << i) != left:
                self._push(left >> i)
            if ((right >> i) << i) != right:
                self._push(right >> i)

        sml = self.e
        smr = self.e
        while left < right:
            if left & 1:
                sml = self.op(sml, self.data[left])
                left += 1
            if right & 1:
                right -= 1
                smr = self.op(self.data[right], smr)
            left >>= 1
            right >>= 1

        return self.op(sml, smr)

    def all_prod(self) -> Any:
        return self.data[1]

    def apply(
        self,
        left: int,
        right: Optional[int] = None,
        f: Optional[Any] = None,
    ) -> None:
        assert f is not None

        if right is None:
            p = left
            assert 0 <= left < self.n

            p += self.size
            for i in range(self.log, 0, -1):
                self._push(p >> i)
            self.data[p] = self.mapping(f, self.data[p])
            for i in range(1, self.log + 1):
                self._update(p >> i)
        else:
            assert 0 <= left <= right <= self.n
            if left == right:
                return

            left += self.size
            right += self.size

            for i in range(self.log, 0, -1):
                if ((left >> i) << i) != left:
                    self._push(left >> i)
                if ((right >> i) << i) != right:
                    self._push((right - 1) >> i)

            l2 = left
            r2 = right
            while left < right:
                if left & 1:
                    self._all_apply(left, f)
                    left += 1
                if right & 1:
                    right -= 1
                    self._all_apply(right, f)
                left >>= 1
                right >>= 1
            left = l2
            right = r2

            for i in range(1, self.log + 1):
                if ((left >> i) << i) != left:
                    self._update(left >> i)
                if ((right >> i) << i) != right:
                    self._update((right - 1) >> i)

    def max_right(self, left: int, g: Callable[[Any], bool]) -> int:
        assert 0 <= left <= self.n
        assert g(self.e)

        if left == self.n:
            return self.n

        left += self.size
        for i in range(self.log, 0, -1):
            self._push(left >> i)

        sm = self.e
        first = True
        while first or (left & -left) != left:
            first = False
            while left % 2 == 0:
                left >>= 1
            if not g(self.op(sm, self.data[left])):
                while left < self.size:
                    self._push(left)
                    left *= 2
                    if g(self.op(sm, self.data[left])):
                        sm = self.op(sm, self.data[left])
                        left += 1
                return left - self.size
            sm = self.op(sm, self.data[left])
            left += 1

        return self.n

    def min_left(self, right: int, g: Any) -> int:
        assert 0 <= right <= self.n
        assert g(self.e)

        if right == 0:
            return 0

        right += self.size
        for i in range(self.log, 0, -1):
            self._push((right - 1) >> i)

        sm = self.e
        first = True
        while first or (right & -right) != right:
            first = False
            right -= 1
            while right > 1 and right % 2:
                right >>= 1
            if not g(self.op(self.data[right], sm)):
                while right < self.size:
                    self._push(right)
                    right = 2 * right + 1
                    if g(self.op(self.data[right], sm)):
                        sm = self.op(self.data[right], sm)
                        right -= 1
                return right + 1 - self.size
            sm = self.op(self.data[right], sm)

        return 0

    def _update(self, k: int) -> None:
        self.data[k] = self.op(self.data[2 * k], self.data[2 * k + 1])

    def _all_apply(self, k: int, f: Any) -> None:
        self.data[k] = self.mapping(f, self.data[k])
        if k < self.size:
            self.lazy[k] = self.composition(f, self.lazy[k])

    def _push(self, k: int) -> None:
        self._all_apply(2 * k, self.lazy[k])
        self._all_apply(2 * k + 1, self.lazy[k])
        self.lazy[k] = self.id
