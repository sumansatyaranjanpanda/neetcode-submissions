class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq=[0]*26

        left=0
        maxfreq=0
        result=0

        for right in range(len(s)):
            idx=ord(s[right])-ord('A')
            freq[idx]+=1


            maxfreq=max(maxfreq,freq[idx])


            while (right-left+1)-maxfreq  > k:
                freq[ord(s[left])-ord('A')]-=1
                left+=1


            result=max(result,right-left+1)

        return result


        