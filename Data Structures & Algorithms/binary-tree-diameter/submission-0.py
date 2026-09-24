# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # same with maximum depth of bt,only include this part like delimeter=left+right , maxDel=max(maxDel,delimeter)
        # we are going to do preoreder travelsal


        a=[0]

        def depth(node):
            if node is None:
                return 0

            left=depth(node.left)
            right=depth(node.right)

            diameter=left+right
            a[0]=max(a[0],diameter)

            return 1+max(left,right)

        depth(root)
        return a[0]
        