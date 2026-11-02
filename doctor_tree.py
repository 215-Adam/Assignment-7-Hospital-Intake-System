class DoctorNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class DoctorTree:
    def __init__(self):
        self.root = None

    def _find(self, node, name):
        # Recursively search both subtrees for the doctor with this name
        if node is None:
            return None
        if node.name == name:
            return node
        found = self._find(node.left, name)
        if found is not None:
            return found
        return self._find(node.right, name)

    def insert(self, parent_name, employee_name, side):
        # Returns True if the doctor was added, False if the insert was invalid
        if side not in ("left", "right"):
            print(f"Invalid side: {side}")
            return False

        parent = self._find(self.root, parent_name)
        if parent is None:
            print(f"Parent not found: {parent_name}")
            return False

        # Refuse to overwrite an existing report and lose their subtree
        if getattr(parent, side) is not None:
            print(f"{parent_name} already has a {side} report")
            return False

        setattr(parent, side, DoctorNode(employee_name))
        return True

    def preorder(self, node):
        if node is None:
            return []
        return [node.name] + self.preorder(node.left) + self.preorder(node.right)

    def inorder(self, node):
        if node is None:
            return []
        return self.inorder(node.left) + [node.name] + self.inorder(node.right)

    def postorder(self, node):
        if node is None:
            return []
        return self.postorder(node.left) + self.postorder(node.right) + [node.name]


# Test your DoctorTree and DoctorNode classes here
if __name__ == "__main__":
    tree = DoctorTree()
    tree.root = DoctorNode("Dr. Croft")

    tree.insert("Dr. Croft", "Dr. Goldsmith", "right")
    tree.insert("Dr. Croft", "Dr. Phan", "left")
    tree.insert("Dr. Phan", "Dr. Carson", "right")
    tree.insert("Dr. Phan", "Dr. Morgan", "left")

    print(tree.preorder(tree.root))
    # ["Dr. Croft", "Dr. Phan", "Dr. Morgan", "Dr. Carson", "Dr. Goldsmith"]
    print(tree.inorder(tree.root))
    # ["Dr. Morgan", "Dr. Phan", "Dr. Carson", "Dr. Croft", "Dr. Goldsmith"]
    print(tree.postorder(tree.root))
    # ["Dr. Morgan", "Dr. Carson", "Dr. Phan", "Dr. Goldsmith", "Dr. Croft"]

    # Edge cases: each insert should print a message and return False
    print(tree.insert("Dr. Nobody", "Dr. Lee", "left"))    # parent doesn't exist
    print(tree.insert("Dr. Phan", "Dr. Lee", "middle"))    # invalid side
    print(tree.insert("Dr. Croft", "Dr. Lee", "left"))     # side already taken
    print(DoctorTree().insert("Dr. Croft", "Dr. Lee", "left"))  # empty tree

    # Edge cases: traversing an empty tree returns an empty list
    empty = DoctorTree()
    print(empty.preorder(empty.root))   # []
    print(empty.inorder(empty.root))    # []
    print(empty.postorder(empty.root))  # []

    # The failed inserts should not have changed the tree
    print(tree.preorder(tree.root))
    # ["Dr. Croft", "Dr. Phan", "Dr. Morgan", "Dr. Carson", "Dr. Goldsmith"]
