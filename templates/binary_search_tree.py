def recursively_bst(root):
    if root:
        return recursively_bst(root.left) + [root.val] + recursively_bst(root.right)
    else:
        return []


def iteratively_bst(root):
    stack = []
    cur = root
    vals = []
    while cur and stack:
        while cur:
            stack.append(cur)
            cur = cur.left

        cur = stack.pop()
        vals.append(cur.val)
        cur = cur.right

    return vals

