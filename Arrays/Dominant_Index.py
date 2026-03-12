class Solution(object):
    def dominantIndex(self, nums):
        max_num = max(nums)
        index = nums.index(max_num)
        
        for i in nums:
            if i != max_num and max_num < 2*i:
                return -1
        return index
        
sol = Solution()
num = [1,2,3,4]
print(sol.dominantIndex(num))
            
            
        