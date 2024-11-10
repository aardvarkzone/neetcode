# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right

# class Solution:
#     def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         #recursive
#         if not root: return None
#         temp = root.right
#         root.right = root.left
#         root.left = temp
#         self.invertTree(root.left)
#         self.invertTree(root.right)
#         return root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #use DFS "ripple" with stack 
        #while stack populated, 
            #pop off the node 
            #grab the left and right child - switch them
            #add new left and new right to stack 
        if not root: return None
        stack = [root]
        while stack:
            temp = stack.pop()
            temp.left, temp.right = temp.right, temp.left
            if temp.left: stack.append(temp.left)
            if temp.right: stack.append(temp.right)
        return root
