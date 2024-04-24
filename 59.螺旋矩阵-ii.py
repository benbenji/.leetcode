#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#
# https://leetcode-cn.com/problems/spiral-matrix-ii/description/
#
# algorithms
# Medium (76.63%)
# Likes:    670
# Dislikes: 0
# Total Accepted:    183.8K
# Total Submissions: 239.9K
# Testcase Example:  '3'
#
# 给你一个正整数 n ，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 3
# 输出：[[1,2,3],[8,9,4],[7,6,5]]
# 
# 
# 示例 2：
# 
# 
# 输入：n = 1
# 输出：[[1]]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 
# 
#

# @lc code=start
from operator import le
from typing import List
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ret = [[0]*n for _ in range(n)] # 注意初始化不能用[[0]*n]*n 否则会出现行相同的问题
        left,right,up,down = 0,n-1,0,n-1
        index =1
        while left < right:
            for x in range(left,right):
                ret[up][x] = index
                index += 1
            for y in range(up,down):
                ret[y][right] = index
                index += 1
            for x in range(right,left,-1):
                ret[down][x] = index
                index += 1
            for y in range(down,up,-1):
                ret[y][left] = index
                index += 1
            left,right,up,down = left + 1, right -1, up + 1, down - 1
        if left ==right:
            ret[left][up] = index
        return ret
# @lc code=end
solution = Solution()
solution.generateMatrix(3)
