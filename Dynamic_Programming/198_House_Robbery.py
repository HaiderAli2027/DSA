class Solution(object):
    def rob(self, nums):
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

print(Solution().rob([1, 2, 3, 1]))
print(Solution().rob([2, 7, 9, 3, 1]))