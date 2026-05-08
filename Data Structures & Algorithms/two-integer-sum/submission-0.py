class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        diff=0
        dic={}
        
        for i in range(len(nums)):
            diff=target-nums[i]

            if diff in dic:
                return [dic[diff],i]

            dic[nums[i]]=i

        