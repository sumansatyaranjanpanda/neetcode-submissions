class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        res=[]

        for i in nums:
            dic[i]=dic.get(i,0)+1


        sorted_dic=sorted(dic,key=lambda x:dic[x],reverse=True)

        return sorted_dic[:k]

        