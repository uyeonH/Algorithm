
class Solution:

    def invertTree(self, root: TreeNode) -> TreeNode:
        
        # 예외처리
        if root is None:
            return None
            
        root.left, root.right = \
            self.invertTree(root.right), self.invertTree(root.left)
            
        return root
