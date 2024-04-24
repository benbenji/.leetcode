#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#
# https://leetcode-cn.com/problems/sliding-window-maximum/description/
#
# algorithms
# Hard (49.83%)
# Likes:    1566
# Dislikes: 0
# Total Accepted:    277.5K
# Total Submissions: 557K
# Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
#
# 给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k
# 个数字。滑动窗口每次只向右移动一位。
# 
# 返回 滑动窗口中的最大值 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
# 输出：[3,3,5,5,6,7]
# 解释：
# 滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
# ⁠1 [3  -1  -3] 5  3  6  7       3
# ⁠1  3 [-1  -3  5] 3  6  7       5
# ⁠1  3  -1 [-3  5  3] 6  7       5
# ⁠1  3  -1  -3 [5  3  6] 7       6
# ⁠1  3  -1  -3  5 [3  6  7]      7
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [1], k = 1
# 输出：[1]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 1 <= k <= nums.length
# 
# 
#

# @lc code=start
from re import I
from typing import List
class myQueue():
    def __init__(self) -> None:
        self.que = []
    def pop(self,x):
        if self.front() == x:
            self.que.pop(0)
    def push(self,x):
        while self.que and self.que[-1] < x:
            self.que.pop()
        self.que.append(x)
    def front(self):
        return self.que[0]
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        myqueue = myQueue()
        ret = []
        for n in range(len(nums)):
            if n < k - 1:
                myqueue.push(nums[n])
            elif n == k-1:
                myqueue.push(nums[n])
                ret.append(myqueue.front())
            else:
                myqueue.pop(nums[n - k])
                myqueue.push(nums[n])
                ret.append(myqueue.front()) 
        return ret
            
# @lc code=end

