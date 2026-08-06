class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False

        need_dic={}
        window_dic={}

        for i in s1:
            need_dic[i]=need_dic.get(i,0)+1

        for i in range(len(s1)):
            window_dic[s2[i]]=window_dic.get(s2[i],0)+1

        if window_dic == need_dic :
            return True

        left=0

        for right in range(len(s1),len(s2)):
            window_dic[s2[right]]=window_dic.get(s2[right],0)+1

            window_dic[s2[left]]-=1

            if window_dic[s2[left]]==0:
                del window_dic[s2[left]]

            left+=1

            if window_dic == need_dic:
                return True

        return False

    






        