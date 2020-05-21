
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        
        # 1. TreeNode가 각각 존재하지 않을 경우를 더하지 않으도 되므로 다른 트리의 값을 반환한다.
        # 트리의 말단으로 갔을 때 끝나게 되는 것이다.
        
        if not t1:
            return t2
    
        if not t2:
            return t1
        
        # 2. 1번 트리의 현재 노드 값과 2번 트리의 현재 노트 값을 더해 새로운 트리를 생성한다.  
        t = TreeNode(t1.val+t2.val)
        
        # 3. 이 생성된 트리의 현재 노드의 왼쪽에는 트리1과 트리2 각각의 왼쪽, 오른쪽 노드를 더하여 트리에 연결한다.
        # 재귀 함수로 실행되고, 트리의 끝쪽에서 반환되며 다시 루트노트까지 돌아오게 된다.
        
        t.left = self.mergeTrees(t1.left, t2.left)
        t.right = self.mergeTrees(t1.right, t2.right)
        
        return t
    
    
    
    
