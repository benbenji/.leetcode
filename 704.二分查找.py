#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#
# https://leetcode-cn.com/problems/binary-search/description/
#
# algorithms
# Easy (54.30%)
# Likes:    758
# Dislikes: 0
# Total Accepted:    539.1K
# Total Submissions: 992.8K
# Testcase Example:  '[-1,0,3,5,9,12]\n9'
#
# 给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的
# target，如果目标值存在返回下标，否则返回 -1。
# 
# 
# 示例 1:
# 
# 输入: nums = [-1,0,3,5,9,12], target = 9
# 输出: 4
# 解释: 9 出现在 nums 中并且下标为 4
# 
# 
# 示例 2:
# 
# 输入: nums = [-1,0,3,5,9,12], target = 2
# 输出: -1
# 解释: 2 不存在 nums 中因此返回 -1
# 
# 
# 
# 
# 提示：
# 
# 
# 你可以假设 nums 中的所有元素是不重复的。
# n 将在 [1, 10000]之间。
# nums 的每个元素都将在 [-9999, 9999]之间。
# 
# 
#

# @lc code=start
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right = 0,len(nums) - 1 
        while left<=right:
            middle = (left + right)//2
            if nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                return middle
        
        return -1
# @lc code=end
solution = Solution()
print(solution.search([-1,0,3,5,9,12],13))

