
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[j]==target-nums[i]:
                    print(nums[i],nums[j])
                    return [i,j]
