class Solution:
    
    def TwocommonPrefix(self, A, B):
    
        # 4.더 작은 문자열 길이를 기준으로
        length = min(len(A),(len(B)))
        
        # 5.문자열의 문자 한 글자씩 비교  
        for i in range(length):
            
            if A[i] != B[i]:
                return A[:i]
            
        return A[:length]
    
    def longestCommonPrefix(self, strs):
        
        # 1.예외처리
        if not strs:
            return ""
        
        ret = strs[0]
        
        # 2.모든 문자열 검사
        for s in strs[1:]:
            
            # 3.TwocommonPrefix 함수에 이전 결과 값 ret과 새 문자열 s 보내기 
            ret = self.TwocommonPrefix(ret, s)
            
        return ret
