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


N, M = map(int, input().split())
edges = []
for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((a - 1, b - 1, c))

edges.sort(key=lambda x: x[2])
uf = UnionFind(N)

ans = 0
for a, b, c in edges:
    if uf.same(a, b):
        continue
    uf.union(a, b)
    ans += c
print(ans)
