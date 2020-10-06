# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        #temp is a stack/list
        #curr starts at root
        #while curr exists
        #1 If left node of curr exists
        # 2 save right node/subtree to temp if right node of curr exists
        # 3 set left node to right node
        # 4 go back to 1
        #5 else (right node of curr doesn't exist)
        # 6 if temp is not empty and curr.right doesn't exist
        # 7 pop top off temp, set to right node of curr
        # 8 go to 1
        # 10 set curr to right node
        # 11 if temp is empty and right node of curr doesn't exist, we are done
        temp = []
        curr = root
        while curr:
            if curr.left:
                if curr.right:
                    temp.append(curr.right)
                curr.right = curr.left
                curr.left = None
            else:
                if temp and not curr.right:
                    curr.right = temp.pop()
            curr = curr.right