# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        q = deque()
        result = []
        if root:
            q.append(root)
        while q:
            size = len(q)
            currLevel = []
            for i in range(size):
                currNode = q.popleft()
                currLevel.append(currNode.val)
                if currNode.left:
                    q.append(currNode.left)
                if currNode.right:
                    q.append(currNode.right)
            result.append(currLevel)
        return result
    