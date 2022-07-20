from collections import deque


class UnionFind:
    """Union Find木クラス
    Attributes:
        parent (list): 親要素を格納するリスト。親要素は自身のサイズを格納する。
    Notes:
        - parent[i] < 0 の場合、iは根。この時、-parent[i]はそのグループのサイズ
        - parent[i] = -1 とすると、iは独立。
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
        if x == y:  # すでに同じ親
            return
        # union by size
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
        """returns the members of the group of x

        Args:
            x (int): The object to find the members of. 要素

        Returns:
            list: The members of the group of x.
        """
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        """returns the roots

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
        """returns all groups

        Returns:
            list: All group members.
        """
        return {r: self.members(r) for r in self.roots()}


N = int(input())
Q = int(input())
uf = UnionFind(N + 1)
dq = deque()
d = [-1] * (N + 1)

for i in range(Q):
    t, x, y, v = map(int, input().split())
    if t == 0:
        uf.union(x, y)
        d[y] = v
    else:
        if uf.same(x, y):
            dq.append((x, y, v))
        else:
            dq.append((-1, -1, -1))

a = [0] * (N + 1)
for i in range(1, N + 1):
    if d[i] == -1:
        continue
    else:
        a[i] = d[i] - a[i - 1]

while dq:
    x, y, v = dq.popleft()
    if x == -1:
        print("Ambiguous")
    else:
        diff = v - a[x]
        if x % 2 == y % 2:
            print(a[y] + diff)
        else:
            print(a[y] - diff)
