import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dic={}

        for i in nums:
            dic[i]=dic.get(i,0)+1

        
        bucket=[[] for _ in range(len(nums)+1)]

        for num,freq in dic.items():
            bucket[freq].append(num)

        
        result=[]

        for freq in range(len(bucket)-1,0,-1):
            for ele in bucket[freq]:
                result.append(ele)
                if len(result)==k:
                    return result
        
        return result





        