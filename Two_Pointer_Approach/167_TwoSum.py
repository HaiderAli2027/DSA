class Solution(object):
    def twoSum(self, numbers, target):
        l, r = 0, len(numbers) - 1

        while l < r:
            CurSum = numbers[l] + numbers[r]
            if CurSum > target:
                r -= 1
            elif CurSum < target:
                l += 1
            else:
                return [l+1, r+1]
        
print(Solution().twoSum([2, 7, 11, 15], 9))
print(Solution().twoSum([2, 3, 4], 6))
