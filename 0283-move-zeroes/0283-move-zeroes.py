class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left=0
        right=1
        while right<len(nums):
            while left<len(nums) and nums[left]!=0:
                left+=1
            right=left+1
            while right<len(nums) and nums[right]==0:
                right+=1
            if right<len(nums) and left<len(nums):
                nums[left],nums[right]=nums[right],nums[left]
        