class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        dic=defaultdict(int)
        left=0
        maxsum=0
        sum1=0
        for right in range(len(nums)):
            while nums[right] in dic:
                sum1-=nums[left]
                del dic[nums[left]]
                left+=1 
            dic[nums[right]]=1
            sum1+=nums[right]
            maxsum=max(sum1,maxsum)
        return maxsum
            

        