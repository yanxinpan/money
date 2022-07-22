from collections import deque


def bfs(root):
    # keep status or path in queue if needed
    # deque is a doubly linked list
    q = deque([root])  # keep q and child_q when layer number is needed.
    visited = set()  # visited set is not needed if there is no cycle or possibility of repeated visits, such as tree.

    while q:
        node = q.popleft()
        if node not in visited:
            visited.add(node)
            for n in node.neighbors:
                q.append(n)

