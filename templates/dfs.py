def dfs(root, target):
    stack = [root]
    visited = set()
    while stack:
        cur = stack.pop()
        if cur == target:
            return True
        if cur not in visited:
            visited.add(cur)
            for n in cur.neighbors:
                stack.append(n)

    return False


def dfs_recursive(cur, target, visited):
    if cur == target:
        return True
    if cur not in visited:
        visited.add(cur)
        for n in cur.neighbors:
            if dfs_recursive(n, target, visited):
                return True

    return False
