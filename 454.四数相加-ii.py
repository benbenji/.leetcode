#
# @lc app=leetcode.cn id=454 lang=python3
#
# [454] 四数相加 II
#
# https://leetcode-cn.com/problems/4sum-ii/description/
#
# algorithms
# Medium (62.34%)
# Likes:    551
# Dislikes: 0
# Total Accepted:    113K
# Total Submissions: 181.2K
# Testcase Example:  '[1,2]\n[-2,-1]\n[-1,2]\n[0,2]'
#
# 给你四个整数数组 nums1、nums2、nums3 和 nums4 ，数组长度都是 n ，请你计算有多少个元组 (i, j, k, l)
# 能满足：
# 
# 
# 0 <= i, j, k, l < n
# nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
# 输出：2
# 解释：
# 两个元组如下：
# 1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) +
# (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) +
# (-1) + 0 = 0
# 
# 
# 示例 2：
# 
# 
# 输入：nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# n == nums1.length
# n == nums2.length
# n == nums3.length
# n == nums4.length
# 1 <= n <= 200
# -2^28 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 2^28
# 
# 
#

# @lc code=start
from itertools import count
from typing import List
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        Count = {}
        for n1 in nums1:
            for n2 in nums2:
                if n1+n2 not in Count:
                    Count[n1+n2] = 1
                else:
                    Count[n1+n2] = Count[n1+n2] + 1
        ret = 0            
        for n3 in nums3:
            for n4 in nums4:
                if -n3-n4 in Count:
                    ret = ret + Count[-n3-n4]
        return ret
# @lc code=end
solution = Solution()
solution.fourSumCount([1,2],[-2,-1],[-1,2],[0,2])

