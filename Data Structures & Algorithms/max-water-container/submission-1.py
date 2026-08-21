class Solution:
    def maxArea(self, heights: List[int]) -> int:
        j = 0
        vol = 0
        k = len(heights)-1
        while j<k:
            vol = max(vol,(k-j) * min(heights[k],heights[j]))
            if heights[j]<heights[k]:
                j+=1
            else:
                k-=1
        return vol
            

        

        