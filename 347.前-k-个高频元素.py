#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#
# https://leetcode-cn.com/problems/top-k-frequent-elements/description/
#
# algorithms
# Medium (62.79%)
# Likes:    1133
# Dislikes: 0
# Total Accepted:    278.6K
# Total Submissions: 443.2K
# Testcase Example:  '[1,1,1,2,2,3]\n2'
#
# 给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]
# 
# 
# 示例 2:
# 
# 
# 输入: nums = [1], k = 1
# 输出: [1]
# 
# 
# 
# 提示：
# 
# 
# 1 
# k 的取值范围是 [1, 数组中不相同的元素的个数]
# 题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的
# 
# 
# 
# 
# 进阶：你所设计算法的时间复杂度 必须 优于 O(n log n) ，其中 n 是数组大小。
# 
#

# @lc code=start
import heapq
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map ={}
        pri_que = []
        for num in nums:
            map[num] = map.get(num,0) + 1
        for (key,freq) in map.items():
            heapq.heappush(pri_que,(freq,key))
            if len(pri_que)>k:
                heapq.heappop(pri_que)
        ret=[]
        for i in pri_que:
            ret.append(i[1])
        return ret
# @lc code=end

