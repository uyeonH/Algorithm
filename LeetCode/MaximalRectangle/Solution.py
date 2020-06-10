class Solution:
    def maximalRectangle(self, matrix):
        # 빈 행렬인지 체크
        if not matrix or not matrix[0]:
            return 0
        
        n = len(matrix[0])
        height = [0] * (n + 1) # 높이를 담는 리스트 (열 단위로 누적)
        result = 0
       
        for r in matrix:
            for i in range(n):
                #현재 값이 1이면 누적해서 1을 더하고, 아니면 0으로 초기화
                height[i] = height[i] + 1 if r[i] == '1' else 0
            
            stack = [-1]
            for i in range(n + 1):
                while height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i - 1 - stack[-1]
                    result = max(result, h * w)
                stack.append(i)
                
        return result

                
   
