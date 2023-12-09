class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        self.height = 1


def height(node):
    if node is None:
        return 0
    return node.height


def update_height(node):
    if node is not None:
        node.height = max(height(node.left), height(node.right)) + 1


def balance_factor(node):
    return height(node.left) - height(node.right)


def rotate_right(y):
    x = y.left
    T2 = x.right

    x.right = y
    y.left = T2

    update_height(y)
    update_height(x)

    return x


def rotate_left(x):
    y = x.right
    T2 = y.left

    y.left = x
    x.right = T2

    update_height(x)
    update_height(y)

    return y


def insert(root, key):
    if root is None:
        return Node(key)

    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    update_height(root)

    balance = balance_factor(root)

    if balance > 1:
        if key < root.left.key:
            return rotate_right(root)
        else:
            root.left = rotate_left(root.left)
            return rotate_right(root)

    if balance < -1:
        if key > root.right.key:
            return rotate_left(root)
        else:
            root.right = rotate_right(root.right)
            return rotate_left(root)

    return root


def max_knowledge(root, k, current_level=1):
    if root is None or current_level > k:
        return 0

    knowledge = root.key
    knowledge += max_knowledge(root.left, k, current_level + 1)
    knowledge += max_knowledge(root.right, k, current_level + 1)

    return knowledge


def find_max_knowledge_hours(hours, knowledge_hogwarts, knowledge_cin):
    root = None

    for knowledge in knowledge_hogwarts:
        root = insert(root, knowledge)

    for knowledge in knowledge_cin:
        root = insert(root, knowledge)

    return max_knowledge(root, hours, current_level=1)

n, m = map(int, input().split())
knowledge_hogwarts = list(map(int, input().split()))
knowledge_cin = list(map(int, input().split()))
hours = int(input())

result = find_max_knowledge_hours(hours, knowledge_hogwarts, knowledge_cin)
print("valor total de conhecimento:", result)
