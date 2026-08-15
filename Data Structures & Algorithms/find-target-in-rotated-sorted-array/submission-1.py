class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        low=0
        high=len(nums)-1

        while low<=high:
            mid=low+(high-low)//2

            if nums[mid]==target:
                return mid

            if nums[low]<=nums[mid]:
                 #left arry part sorted

                 if nums[low]<=target<nums[mid]:
                    high=mid-1
                 else:
                    low=mid+1

            else:
                #right array part sorted

                if nums[mid]<target<=nums[high]:
                    low=mid+1
                else:
                    high=mid-1

        return -1

            


