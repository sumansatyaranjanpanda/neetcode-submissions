class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:



        smaller = nums2 if len(nums1)>len(nums2) else nums1
        larger =  nums1 if len(nums1)>len(nums2) else nums2

        totalsize=len(nums1)+len(nums2)

        l=0
        r=len(smaller)

        while l<=r:
            px=l+(r-l)//2
            py=(totalsize+1)//2-px

            l1 = float('-inf') if  px==0 else smaller[px-1]
            r1 = float('inf') if px==len(smaller) else smaller[px]

            l2 = float('-inf') if py == 0 else larger[py-1]
            r2 = float('inf') if py == len(larger) else larger[py]

            if l1<=r2 and l2<=r1:
                if totalsize%2==1:
                    return max(l1,l2)
                else:
                    return (max(l1,l2)+min(r1,r2))/2.0

            if l1>r2:
                r=px-1
            else:
                l=px+1

        return 0

        