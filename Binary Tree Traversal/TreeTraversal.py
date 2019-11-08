class TreeNode:
    def __init__(self, x):
        """Defines a binary tree node"""
        self.val = x
        self.left = None
        self.right = None


class BuildTree:
    """Creates an object representing our binary tree from a list"""
    def insertLevel(self, arr, root, i, n):
        if i < n:
            temp = TreeNode(arr[i])
            root = temp
            root.left = BuildTree.insertLevel(self, arr, root.left, 2 * i + 1, n)
            root.right = BuildTree.insertLevel(self, arr, root.right, 2 * i + 2, n)
        return root


class Traversal:

    def __init__(self):
        self._inData = []
        self._preData = []

    def inOrder(self, root):
        """traverses our binary tree object in order, adds the value of the node
        to a list that is returned"""
        if root:
            self.inOrder(root.left)
            if root.val is not None:
                self._inData.append(root.val)
            self.inOrder(root.right)
        return self._inData

    def preOrder(self, root):
        """traverses our binary tree object pre order, adds the value of the node
                to a list that is returned"""
        if root:
            if root.val is not None:
                self._preData.append(root.val)
            self.preOrder(root.left)
            self.preOrder(root.right)
        return self._preData


tree = [1,None,2,3]
n = len(tree)

builder = BuildTree()
traveler = builder.insertLevel(tree, None, 0, n)

test = Traversal()
print(test.inOrder(traveler))
print(test.preOrder(traveler))



