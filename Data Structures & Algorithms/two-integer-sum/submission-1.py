class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dic={}

        diff=0

        for i in range(0,len(nums)):
            diff=target-nums[i]

            if diff in dic:
                return [dic[diff],i]

            dic[nums[i]]=i





        