class UnionFind:
    def __init__(self, n):
        """
            Time Complexity: O(n)
        """
        self.root = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, i):
        """
            Time Complexity: O(alpha(n)). The inverse Ackermann algorithm
        """
        if i == self.root[i]:
            return i
        self.root[i] = self.find(self.root[i])
        return self.root[i]

    def union(self, i, j):
        """
                    Time Complexity: O(alpha(n)). The inverse Ackermann algorithm
                """
        pi = self.root[i]
        pj = self.root[j]

        if pi == pj:
            return 0
        if self.rank[pi] > self.rank[pj]:
            self.root[pj] = pi
        elif self.rank[pi] < self.rank[pj]:
            self.par[pi] = pj
        else:
            self.par[pj] = pi
            self.rank[pi] += 1

        return 1

    def connected(self, x, y):
        """
                    Time Complexity: O(alpha(n)). The inverse Ackermann algorithm
                """
        return self.find(x) == self.find(y)

