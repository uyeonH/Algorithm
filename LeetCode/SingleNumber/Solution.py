
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # 1. 빈 배열 만들기
        blank=[] 
        
        # 2. nums 배열에서 blank 배열로 하나씩 옮긴다.
        # 없으면 추가해주고, 있으면 지운다.
        for i in nums:

            if i not in blank:
                blank.append(i)
                
            else:
                blank.remove(i)
                
        # 3. 마지막 남은 요소를 꺼낸다.        
        return blank.pop()
        
