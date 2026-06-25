from typing import List


class Solution:
    def MaxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        CurSum = 0

        for n in nums:
            if CurSum < 0:
                CurSum = 0

            CurSum += n
            maxSub = max(maxSub, CurSum)
        return maxSub

print(Solution().MaxSubArray([-2,1,-3,4,-1,2,1,-5,7]))
print(Solution().MaxSubArray([-1,-3,-4]))
