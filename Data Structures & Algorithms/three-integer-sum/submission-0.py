class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        if nums is None or len(nums)<3:
            return []

        nums.sort()

        result=set()

        for i in range(len(nums)-2):
            left=i+1
            right=len(nums)-1 ## fix 

            while left<right:
                sum1=nums[i]+nums[left]+nums[right]

                if sum1==0:
                    result.add((nums[i],nums[left],nums[right]))
                    left+=1
                    right-=1
                elif sum1>0:
                    right-=1
                else:
                    left+=1

        return [list(i) for i in result]

        

        


        