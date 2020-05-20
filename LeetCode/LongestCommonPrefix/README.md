# [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)

## Description

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

가장 긴 공통된 접두사를 찾는 함수를 적으시오.

만약 공통 접두사가 존재하지 않는다면, ""를 반환하시오.

## Solution
       
       # 1.예외처리
         if not strs:
              return ""
              
        # 2.모든 문자열 검사
          for s in strs[1:]:
        
        # 3.TwocommonPrefix 함수에 이전 결과 값 ret과 새 문자열 s 보내기 
              ret = self.TwocommonPrefix(ret, s)
        
        # 4.더 작은 문자열 길이를 기준으로
              length = min(len(A),(len(B)))
              
        # 5.문자열의 문자 한 글자씩 비교  
          for i in range(length):

              if A[i] != B[i]:
                  return A[:i]

          return A[:length]
    
        
