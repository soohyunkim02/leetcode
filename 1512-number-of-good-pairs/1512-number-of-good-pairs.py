class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i,num in enumerate(nums):
            count += nums[i+1:].count(num)
        return count