import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        res=[]

        for i in nums:
            dic[i]=dic.get(i,0)+1

        res=[]
        for k1,v in dic.items():
            heapq.heappush(res,(v,k1))
            if len(res)>k:
                heapq.heappop(res)

        return [r2 for r1,r2 in res]




        