from union_find import UnionFind
import heapq
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


def prim_algorithm(n, edges):
    """
       Time Complexity: O(E⋅logE)
       Space Complexity: O(V)

       :param n: int, number of vertices.
       :param edges: List[List[ weight, vertex_0, vertex_1,]]
       :return: List[List[vertex_0, vertex_1, weight]], a subset of edges which forms a minimum spanning tree.
       """
    edges_dict = {}
    for n1, n2, w in edges:
        edges_dict[n1] = edges_dict.get(n1, []) + [(n2, w)]
    heap = []
    heapq.heapify(heap)  # use weight in heapq.
    for n2, w in edges_dict[0]:
        heapq.heappush(heap, [w, n2])

    visited = set(0)
    used_edges = 0
    while used_edges < n:
        w, n1 = heapq.heappop(heap)
        if n1 not in visited:
            visited.add(n1)
            for n2, w in edges_dict[n1]:
                heapq.heappush([w, n2])
                used_edges += 1
    

