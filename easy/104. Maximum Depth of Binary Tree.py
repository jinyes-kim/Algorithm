class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def maxDepth(self, root):
        answer = 0
        if not root:
            return answer
        else:
            answer += 1

        if root.left is None and root.right is None:
            return answer
        else:
            answer += max(self.maxDepth(root.left), self.maxDepth(root.right))
            print(answer)
        return answer


"""
# code test

rrr = TreeNode(7)
rrl = TreeNode(6)
ll = TreeNode(5)
r = TreeNode(3, rrl, rrr)
l = TreeNode(2, right=ll)
root = TreeNode(1, l, r)

res = Solution().maxDepth(root)
"""