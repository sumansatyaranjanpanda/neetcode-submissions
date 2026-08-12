class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:


        stack=[]
        maxarea=0

        heights.append(0)


        for i,height in enumerate(heights):

            while stack and heights[stack[-1]]>height:

                h=heights[stack.pop()]

                if not stack:
                    w=i
                else:
                    w=i-stack[-1]-1

                area= w*h
                maxarea=max(maxarea,area)

            stack.append(i)

        return maxarea


        