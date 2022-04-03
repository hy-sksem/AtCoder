class UnionFind:
    """
    Union Find木クラス
    """

    def __init__(self, n):
        """
        Args:
            n (int): The number of objects. 要素数
        """
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        """returns the root of x

        Args:
            x (int): The object to find the root of. 要素

        Returns:
            int: The root of x.
        """
        if self.parents[x] < 0:
            return x
        else:
            # 経路圧縮により、親要素を根要素に更新し根を短くする
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        """unites the root of x and the root of y

        Args:
            x (int): The first object to union. 要素
            y (int): The second object to union. 要素
        """
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        # xとyの木の高さを比較し、低いほうから高いほうに辺を張る
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        """returns the size of the group of x

        Args:
            x (int): The object to find the size of. 要素

        Returns:
            int: The size of the group of x.
        """
        return -self.parents[self.find(x)]

    def same(self, x, y):
        """returns True if the root of x is the same as the root of y

        Args:
            x (int): The first object to check. 要素
            y (int): The second object to check. 要素

        Returns:
            bool: True if the root of x is the same as the root of y.
        """
        return self.find(x) == self.find(y)

    def members(self, x):
        """_summary_

        Args:
            x (int): The object to find the members of. 要素

        Returns:
            list: The members of the group of x.
        """
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        """_summary_

        Returns:
            list: The roots.
        """
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        """returns the number of groups

        Returns:
            int: The number of groups.
        """
        return len(self.roots())

    def all_group_members(self):
        """_summary_

        Returns:
            list: All group members.
        """
        return {r: self.members(r) for r in self.roots()}


H, W = map(int, input().split())
Q = int(input())
red = [[False] * W for _ in range(H)]


def num(r, c):
    return r * W + c


UF = UnionFind(H * W)

for i in range(Q):
    q, *s = map(int, input().split())
    if q == 1:
        r, c = s
        r -= 1
        c -= 1
        red[r][c] = True
        if r != 0 and red[r - 1][c]:
            UF.union(num(r, c), num(r - 1, c))
        if r != H - 1 and red[r + 1][c]:
            UF.union(num(r, c), num(r + 1, c))
        if c != 0 and red[r][c - 1]:
            UF.union(num(r, c), num(r, c - 1))
        if c != W - 1 and red[r][c + 1]:
            UF.union(num(r, c), num(r, c + 1))
    else:
        r1, c1, r2, c2 = s
        r1 -= 1
        c1 -= 1
        r2 -= 1
        c2 -= 1
        if (r1, c1) == (r2, c2):
            if red[r1][c1]:
                print("Yes")
            else:
                print("No")
        else:
            if UF.same(num(r1, c1), num(r2, c2)):
                print("Yes")
            else:
                print("No")
