class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        #recursive solution. Fairly straight forward
        result = []
        def inorderHelp(node):
            if not node:
                return
            inorderHelp(node.left)
            result.append(node.val)
            inorderHelp(node.right)
        inorderHelp(root)
        return result
    
    def inorderTraversalIterative(self, root: TreeNode) -> List[int]:
        #iterative solution
        result = []
        stack = []
        curr = root
        while stack or curr:
            while curr:
                #go to leftmost node while adding each node to a stack
                stack.append(curr)
                curr = curr.left
            if stack:
                #pop top of stack (which is current leftmost node) and add value to result
                curr = stack.pop()
                result.append(curr.val)
                #check for any right nodes annd repeat inorder on that subtree
                curr = curr.right
        return result
            
        