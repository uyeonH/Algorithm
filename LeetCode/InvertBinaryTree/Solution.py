
class Solution:

    def invertTree(self, root: TreeNode) -> TreeNode:
        
        # 배열이 비어있으면, 
        if root is None:
            return None
            
        root.left, root.right = \
            self.invertTree(root.right), self.invertTree(root.left)
            
        return root
