# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    #recursive solution

    
    #check if the nodes are the same
    def check(self, node1, node2):
        if not node1 and not node2:
            return True
        if (not node1 and node2) or (node1 and not node2):
            return False
        if node1.val == node2.val:
            return True
        else:
            return False

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        #traverse through both trees. If not check, return false, else return true
        def traverse(node1, node2):
            if not self.check(node1, node2):
                return False
            if not node1 and not node2:
                return True
            return traverse(node1.left, node2.left) and traverse(node1.right, node2.right)
        return traverse(p, q)
    
    #iterative solution
    def isSameTreeIterative(self, p: TreeNode, q: TreeNode) -> bool:
        stack1 = [p]
        stack2 = [q]
        while stack1 and stack2:
            node1 = stack1.pop()
            node2 = stack2.pop()
            if not self.check(node1, node2):
                return False
            if node1.left:
                stack1.append(node1.left)
            if node1.right:
                stack1.append(node1.right)
            if node2.left:
                stack2.append(node2.left)
            if node2.right:
                stack2.append(node2.right)
        return not(stack1 or stack2)