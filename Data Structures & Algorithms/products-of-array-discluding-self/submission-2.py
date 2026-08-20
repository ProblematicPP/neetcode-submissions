class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * (len(nums)+1)
        postfix = [1] * (len(nums)+1)
        
        # Left-to-Right loop for Prefix
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i]
            
        # Right-to-Left loop for Postfix
        postfix[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            postfix[i] = postfix[i+1] * nums[i]
        ans = []
        for i in range(n):
            ans.append(prefix[i-1]*postfix[i+1])
        return ans
        
            
        
            
            
            

        
        