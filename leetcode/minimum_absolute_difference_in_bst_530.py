# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        bst = array_to_bst(root)
        return bst

def array_to_bst(array: list[int]) -> TreeNode:
    root = TreeNode(array[0])
    for i in range(1, len(array)):
        insert(root, array[i])
    return root

def insert(root: TreeNode, val: int) -> TreeNode:
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

def print_tree(root: TreeNode):
    if root is None:
        return
    print_tree(root.left)
    print(root.val)
    print_tree(root.right)

solution = Solution()
answer = solution.getMinimumDifference([4, 2, 6, 1, 3])
print_tree(answer)
assert answer == 1