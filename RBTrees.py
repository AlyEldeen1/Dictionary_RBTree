from Node import Node


class RBTrees:

    def __init__(self):
        self.nil = Node(None, "BLACK")
        self.root = self.nil

    def insert(self, value):
        new = Node(value)

        parent = self.nil
        current = self.root
        while current != self.nil:
            parent = current
            if new.value < current.value:
                current = current.left
            else:
                current = current.right
        new.parent = parent
        if parent is self.nil:
            self.root = new
        elif new.value < parent.value:
            parent.left = new
        else:
            parent.right = new
        new.left = self.nil
        new.right = self.nil
        self._fixup_insert(new)

    def _fixup_insert(self, node):
        while node != self.root and node.parent.color == "RED":
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == "RED":  # CASE 1
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:  # CASE 2
                        node = node.parent
                        self._left_rotate(node)
                    # CASE 3
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self._right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == "RED":
                    # Case 1
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        # Case 2:
                        node = node.parent
                        self._right_rotate(node)
                    # Case 3:
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self._left_rotate(node.parent.parent)
        self.root.color = "BLACK"

    def _left_rotate(self, x):
        y = x.right

        x.right = y.left
        if y.left is not None:
            y.left.parent = x
            y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.left is not None:
            y.right.parent = x
            y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.right = x
        x.parent = y

    def search(self, value):
        return self._search_helper(self.root, value)

    def _search_helper(self, root, value):
        if root == self.nil:
            return 0
        elif root.value == value:
            return 1
        else:

            if value < root.value:
                return self._search_helper(root.left, value)
            else:
                return self._search_helper(root.right, value)

    def tree_height(self):
        return self._tree_height_helper(self.root)

    def _tree_height_helper(self, node):
        if node == self.nil:
            return 0
        else:
            left_height = self._tree_height_helper(node.left)
            right_height = self._tree_height_helper(node.right)
            return max(left_height, right_height) + 1

    def black_height(self):
        # Start the calculation from the root node
        return self._black_height_helper(self.root)

    def _black_height_helper(self, node):
        if node == self.nil:
            # For sentinel nodes, the black height is 0
            return 0
        else:
            # Recursively calculate the black height of left and right subtrees
            left_black_height = self._black_height_helper(node.left)
            right_black_height = self._black_height_helper(node.right)

            # Check if the left and right subtrees have the same black height
            if left_black_height != right_black_height:
                # If they don't have the same black height, it indicates a violation of the red-black tree property
                raise ValueError(
                    "Red-Black tree property violation: Left and right subtrees have different black heights")

            # Increment the black height if the current node is black
            if node.color == "BLACK":
                return left_black_height + 1
            else:
                return left_black_height

    def tree_size(self):
        return self._tree_size_helper(self.root)

    def _tree_size_helper(self, node):
        if node == self.nil:
            # For sentinel nodes, the size of the subtree is 0
            return 0
        else:
            # Recursively calculate the size of left and right subtrees
            left_size = self._tree_size_helper(node.left)
            right_size = self._tree_size_helper(node.right)

            # Return the total size of the subtree rooted at the current node
            return left_size + right_size + 1

    # def print_tree(self):
    #     self._print_tree_helper(self.root)
    #
    # def _print_tree_helper(self, node, indent="", last=True):
    #     if node != self.nil:
    #         print(indent, end="")
    #         if last:
    #             print("R----", end="")
    #             indent += "     "
    #         else:
    #             print("L----", end="")
    #             indent += "|    "
    #
    #         color = "RED" if node.color == "RED" else "BLACK"
    #         print(str(node.value) + " (" + color + ")")
    #         self._print_tree_helper(node.left, indent, False)
    #         self._print_tree_helper(node.right, indent, True)
