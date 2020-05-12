class Solution:
    def twoSum(self, nums, target):
        dic = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in dic:
                dic[num] = i
            else:
                return [dic[n], i]
