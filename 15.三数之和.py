#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
# https://leetcode-cn.com/problems/3sum/description/
#
# algorithms
# Medium (35.09%)
# Likes:    4641
# Dislikes: 0
# Total Accepted:    915.3K
# Total Submissions: 2.6M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0
# 且不重复的三元组。
# 
# 注意：答案中不可以包含重复的三元组。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
# 
# 
# 示例 2：
# 
# 
# 输入：nums = []
# 输出：[]
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [0]
# 输出：[]
# 
# 
# 
# 
# 提示：
# 
# 
# 0 
# -10^5 
# 
# 
#

# @lc code=start
from re import I
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []
        for idx in range(len(nums)-2):
            if idx >= 1 and nums[idx - 1]==nums[idx]:
                    continue
            left = idx +1 
            right = len(nums) - 1
            while left<right:
                if nums[left] + nums[right] + nums[idx]>0:
                    right = right - 1
                elif nums[left] +nums[right] + nums[idx]<0:
                    left = left + 1
                else:
                    ret.append([nums[idx],nums[left],nums[right]])
                    while left != right and nums[left] == nums[left + 1]: left += 1
                    while left != right and nums[right] == nums[right - 1]: right -= 1
                    left = left +1
                    right = right -1
        return ret
solution = Solution()
solution.threeSum([-1,0,1,2,-1,-4])
# @lc code=end

