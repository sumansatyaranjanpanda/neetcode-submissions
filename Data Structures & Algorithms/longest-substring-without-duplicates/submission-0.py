class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        set1=set()

        maxlen=0
        left=0

        for right in range(0,len(s)):

            while s[right] in set1:
                set1.remove(s[left])
                left=left+1

            set1.add(s[right])
            maxlen=max(maxlen,right-left+1)


        return maxlen

