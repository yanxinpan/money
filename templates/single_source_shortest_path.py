import heapq
"""
To find the shortest path in a weighted graph, 
use Dijkstra algorithm (non-negative weight) and use Bellman Ford elsewhere. 
To find the shortest path in an unweighted graph, use BFS.
"""


def dijkstra_algorithm(n, k, graph):
    """
    Find the shortest path in a non-negative weight graph.
    :param n: The number of vertices
    :param k: The starting vertex
    :param graph: the dictionary describing the graph
    :return: List. the length of the shortest path from k to every node.

    Time complexity： O(V + E log(V))
    Space complexity: O(V)
    """
    heap = []
    heapq.heapify(heap)
    heapq.heappush(heap, (0, k))
    visited = set()

    path_len = [float('inf')] * n
    path_len[k] = 0

    while heap:
        current_w, node = heapq.heappop(heap)
        visited.add(node)
        for v, w in graph[node]:
            if v not in visited:
                new_w = current_w + w
                if new_w < path_len[v]:
                    path_len[v] = new_w
                    heapq.heappush(heap, (new_w, v))

    return path_len

