class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        def inorderHelp(node):
            if not node:
                return
            inorderHelp(node.left)
            result.append(node.val)
            inorderHelp(node.right)
        inorderHelp(root)
        return result
    
    def inorderTraversalIterative(self, root: Treenode) -> List[int]:
        result = []
        stack = []
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            if stack:
                curr = stack.pop()
                result.append(curr.val)
                curr = curr.right
        return result
            
        