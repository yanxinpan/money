from union_find import UnionFind

"""
A spanning tree is a subgraph of an undirected graph where all vertices are connected
with the minimum numbers of edges.

There are multiple spanning tree

"""

"""
A minimum spanning tree is a spanning tree with the minimum possible total edge weight
in a weighted undirected graph.

Thus, a “weighted undirected graph” can have multiple minimum spanning trees. 
"""

"""
Cut property: For any cut C of the graph, if the weight of an edge E in the cut-set of C 
is strictly smaller than the weights of all other edges of the cut-set of C, 
then this edge belongs to all MSTs of the graph.

"""


def kruskal_algorithm(n, edges):
    """
    Time Complexity: O(E⋅logE)
    Space Complexity: O(V)

    :param n: int, number of vertices.
    :param edges: List[List[vertex_0, vertex_1, weight]]
    :return: List[List[vertex_0, vertex_1, weight]], a subset of edges which forms a minimum spanning tree.
    """
    edges = sorted(edges, key=lambda x: x[-1])
    uf = UnionFind(n)

    ans = []
    for e in edges:
        if uf.union(e[0], e[1]):
            ans.append(e)
            if len(ans) == n - 1:
                return ans
