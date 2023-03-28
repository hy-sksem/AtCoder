from typing import List, Tuple

import sys


class CSR:
    def __init__(self, n: int, edges: List[Tuple[int, int]]) -> None:
        self.start = [0] * (n + 1)
        self.elist = [0] * len(edges)

        for e in edges:
            self.start[e[0] + 1] += 1

        for i in range(1, n + 1):
            self.start[i] += self.start[i - 1]

        counter = self.start.copy()
        for e in edges:
            self.elist[counter[e[0]]] = e[1]
            counter[e[0]] += 1


class SCCGraph:
    """
    Reference:
    R. Tarjan,
    Depth-First Search and Linear Graph Algorithms
    """

    def __init__(self, n: int) -> None:
        """
        n: number of vertices
        args:
            n: int
        """
        self._n = n
        self._edges: List[Tuple[int, int]] = []

    def num_vertices(self) -> int:
        """
        Returns the number of vertices.
        """
        return self._n

    def add_edge(self, from_vertex: int, to_vertex: int) -> None:
        """
        Adds an edge from from_vertex to to_vertex.
        args:
            from_vertex: int
            to_vertex: int
        """
        n = self.num_vertices()
        assert 0 <= from_vertex < n
        assert 0 <= to_vertex < n
        self._edges.append((from_vertex, to_vertex))

    def scc_ids(self) -> Tuple[int, List[int]]:
        """
        Returns a list of group ids and a list of vertices in each group.
        """
        g = CSR(self._n, self._edges)
        now_ord = 0
        group_num = 0
        visited = []
        low = [0] * self._n
        order = [-1] * self._n
        ids = [0] * self._n

        sys.setrecursionlimit(max(self._n + 1000, sys.getrecursionlimit()))

        def dfs(v: int) -> None:
            """
            Depth-First Search
            args:
                v: int
            """
            nonlocal now_ord
            nonlocal group_num
            nonlocal visited
            nonlocal low
            nonlocal order
            nonlocal ids

            low[v] = now_ord
            order[v] = now_ord
            now_ord += 1
            visited.append(v)
            for i in range(g.start[v], g.start[v + 1]):
                to = g.elist[i]
                if order[to] == -1:
                    dfs(to)
                    low[v] = min(low[v], low[to])
                else:
                    low[v] = min(low[v], order[to])

            if low[v] == order[v]:
                while True:
                    u = visited[-1]
                    visited.pop()
                    order[u] = self._n
                    ids[u] = group_num
                    if u == v:
                        break
                group_num += 1

        for i in range(self._n):
            if order[i] == -1:
                dfs(i)

        for i in range(self._n):
            ids[i] = group_num - 1 - ids[i]

        return group_num, ids

    def scc(self) -> List[List[int]]:
        """
        Returns a list of groups.
        """
        ids = self.scc_ids()
        group_num = ids[0]
        counts = [0] * group_num
        for x in ids[1]:
            counts[x] += 1
        groups: List[List[int]] = [[] for _ in range(group_num)]
        for i in range(self._n):
            groups[ids[1][i]].append(i)

        return groups


n, m = map(int, sys.stdin.readline().split())
g = SCCGraph(n)

for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    g.add_edge(u, v)

scc = g.scc()

print(len(scc))
for c in scc:
    print(len(c), *c)
