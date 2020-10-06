# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        #check if the nodes are the same
        def check(node1, node2):
            if not node1 and not node2:
                return True
            if (not node1 and node2) or (node1 and not node2):
                return False
            if node1.val == node2.val:
                return True
            else:
                return False
        #traverse through both trees. If not check, return false, else return true
        def traverse(node1, node2):
            if not check(node1, node2):
                return False
            if not node1 and not node2:
                return True
            return traverse(node1.left, node2.left) and traverse(node1.right, node2.right)
        return traverse(p, q)