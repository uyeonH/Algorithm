
class Solution(object):

    def singleNumber(self, nums):
    
        """
        :type nums: List[int]
        :rtype: int
        """
        # (중복을 제거한 배열 요소의 합 * 2) - (배열 요소의 합)
        return 2 * sum(set(nums)) - sum(nums)
