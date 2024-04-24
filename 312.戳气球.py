#
# @lc app=leetcode.cn id=312 lang=python
#
# [312] 戳气球
#

# @lc code=start
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # targetlist = []
        nums = [1]+nums+[1]
        matrixsize = len(nums) - 1
        dp = [[0]*matrixsize for i in range(matrixsize)]
        for r in range(1,matrixsize):
            for k in range(matrixsize- r):
                max = 0
                maxindex = 0
                for j in range(r):
                    temp=dp[k][k+j]+dp[k+j+1][k+r]+nums[k]*nums[k+j+1]*nums[k+r+1]
                    if max < temp:
                        max = temp
                dp[k][k+r] = max
        return dp[0][matrixsize-1]
    

solution = Solution()
print(solution.maxCoins([3,1,5,8]))
# @lc code=end

