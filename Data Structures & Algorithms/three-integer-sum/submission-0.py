class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j = i+1
            k = len(nums)-1
            while j<k:
                if nums[j]+nums[k]+nums[i]==0:
                    ans.append([nums[i],nums[j],nums[k]])
                    j+=1
                    while nums[j] == nums[j-1] and j<k:
                        j += 1
                elif nums[j]+nums[k]+nums[i]>0:
                    k-=1
                elif nums[j]+nums[k]+nums[i]<0:
                    j+=1 
        return ans

        