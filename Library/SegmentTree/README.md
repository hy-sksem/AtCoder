# セグメント木

## SegmentTree(セグメント木)

### セグメント木でできること

### セグメント木 Python 実装 コメント有

```python
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
        assert 0 <= p < self._n

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
        assert 0 <= p < self._n
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

        assert 0 <= left <= right <= self._n
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

```

### セグメント木 Python 実装 コメント無

[Library/SegmentTree/SegmentTree.py](Library/SegmentTree/SegmentTree.py)

## Lazy Segment Tree(遅延評価セグメント木)

### コメント有

```python
from typing import List, Optional, Union, Any, Callable


def ceil_pow2(n: int) -> int:
    x = 0
    while (1 << x) < n:
        x += 1

    return x


class LazySegmentTree:
    """
    LazySegmentTreeクラス
    """

    def __init__(
        self,
        op: Callable[[Any, Any], Any],
        e: Any,
        mapping: Callable[[Any, Any], Any],
        composition: Callable[[Any, Any], Any],
        id_: Any,
        v: Union[int, List[Any]],
    ) -> None:
        """
        Args:
            op: 演算
            e: 単位元
            mapping: 値を変換する関数
            composition: 関数の結合
            id_: 関数のid
            v: 初期化値
        """
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
        """replace the value at the given position
        Args:
            p: position
            x: 値
        """
        assert 0 <= p < self.n

        p += self.size
        for i in range(self.log, 0, -1):
            self._push(p >> i)
        self.data[p] = x
        for i in range(1, self.log + 1):
            self._update(p >> i)

    def get(self, p: int) -> Any:
        """returns the value of the node at the given position
        Args:
            p: position
        """
        assert 0 <= p < self.n

        p += self.size
        for i in range(self.log, 0, -1):
            self._push(p >> i)
        return self.data[p]

    def prod(self, left: int, right: int) -> Any:
        """returns the product of the elements in the given range
        Args:
            left: 左端
            right: 右端
        """
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
        """returns the product of all elements"""
        return self.data[1]

    def apply(
        self,
        left: int,
        right: Optional[int] = None,
        f: Optional[Any] = None,
    ) -> None:
        """reverse lazy propagation
        Args:
            left: 左端
            right: 右端
            f: 関数
        """
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
        """returns the index of the rightmost element that satisfies the given predicate

        Args:
            left: 左端
            g: 関数
        """

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
        """returns the index of the leftmost element that satisfies the given predicate
        args:
            right: 右端
            g: 関数
        """
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
        """update the node at the given position
        Args:
            k: position
        """
        self.data[k] = self.op(self.data[2 * k], self.data[2 * k + 1])

    def _all_apply(self, k: int, f: Any) -> None:
        """apply the function to the node at the given position
        Args:
            k: position
            f: 関数
        """
        self.data[k] = self.mapping(f, self.data[k])
        if k < self.size:
            self.lazy[k] = self.composition(f, self.lazy[k])

    def _push(self, k: int) -> None:
        """push the node at the given position
        Args:
            k: position
        """
        self._all_apply(2 * k, self.lazy[k])
        self._all_apply(2 * k + 1, self.lazy[k])
        self.lazy[k] = self.id

```

### コメント無

```python
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
```
