def preorder_traversal(root):
    if root is None:
        return []
    else:
        return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right)


def inorder_traversal(root):
    if root is None:
        return []
    else:
        return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)


def postorder_traversal(root):
    if root is None:
        return []
    else:
        return postorder_traversal(root.left) + postorder_traversal(root.right) + [root.val]

