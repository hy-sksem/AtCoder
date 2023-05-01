class FordFulkerson:
    def __init__(self, N: int):
        """Ford-Fulkerson algorithm
        args:
            N: int
                number of nodes
        """
        self.N = N
        self.G = [[] for i in range(N)]

    def add_edge(self, fr: int, to: int, cap: int) -> None:
        """
        args:
            fr: int
                from
            to: int
                to
            cap: int
                capacity
        """
        forward = [to, cap, None]
        forward[2] = backward = [fr, 0, forward]
        self.G[fr].append(forward)
        self.G[to].append(backward)

    def add_multi_edge(self, v1: int, v2: int, cap1: int, cap2: int) -> None:
        """add edge v1-v2 and v2-v1
        args:
            v1: int
                vertex 1
            v2: int
                vertex 2
            cap1: int
                capacity 1
            cap2: int
                capacity 2
        """
        edge1 = [v2, cap1, None]
        edge1[2] = edge2 = [v1, cap2, edge1]
        self.G[v1].append(edge1)
        self.G[v2].append(edge2)

    def dfs(self, v: int, t: int, f: int) -> int:
        """depth first search
        args:
            v: int
                vertex
            t: int
                target
            f: int
                flow
        returns:
            d: int
                flow
        """
        if v == t:
            return f
        used = self.used
        used[v] = 1
        for e in self.G[v]:
            w, cap, rev = e
            if cap and not used[w]:
                d = self.dfs(w, t, min(f, cap))
                if d:
                    e[1] -= d
                    rev[1] += d
                    return d
        return 0

    def flow(self, s: int, t: int) -> int:
        """
        args:
            s: int
                source
            t: int
                sink
        returns:
            flow: int
                max flow
        """
        flow = 0
        f = INF = 10**9 + 7
        N = self.N
        while f:
            self.used = [0] * N
            f = self.dfs(s, t, INF)
            flow += f
        return flow
