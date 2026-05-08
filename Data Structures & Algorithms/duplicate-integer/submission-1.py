class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        if len(nums)==0:
            return False
        dic={}

        for i in nums:
            dic[i]=dic.get(i,0)+1

        
        if max(dic.values())>1:
            return True
        
        return False