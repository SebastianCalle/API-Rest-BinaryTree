import collections
from binarytree import Node


def insert(root, node):
    # Function that insert Node in order bst
    if root is None:
        root = node
    else:
        if root.value < node.value:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)


def lca(root, n1, n2):
    # Base Case
    if root is None:
        return None

    # If both n1 and n2 are smaller than root, then LCA recursive for left way
    if root.value > n1 and root.value > n2:
        return lca(root.left, n1, n2)

    # If both n1 and n2 are greater than root, then LCA recursive for right way
    if root.value < n1 and root.value < n2:
        return lca(root.right, n1, n2)

    return root.value


class Code:
    """
    Class serialize and deserialize Binary Tree
    """
    def serialize(self, root):
        # Serialize Binary Tree
        result = []

        def encode(node):
            # Function that convert node to str
            if not node:
                return result.append('None')
            result.append(str(node.value))
            encode(node.left)
            encode(node.right)
        encode(root)
        return ','.join(result)

    def deserialize(self, data):
        # Deserialize Binary Tree
        deque = collections.deque(data.split(','))

        def decode():
            # Function that convert each element of the list in a new node
            try:
                node_str = deque.popleft()
                if node_str == 'None':
                    return None
                node = Node(int(node_str))
                node.left = decode()
                node.right = decode()
                return node
            except IndexError:
                pass

        root = decode()
        return root

