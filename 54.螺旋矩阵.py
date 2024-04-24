#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#
# https://leetcode-cn.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (48.61%)
# Likes:    1049
# Dislikes: 0
# Total Accepted:    247.3K
# Total Submissions: 508.8K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
# 
# 
# 示例 2：
# 
# 
# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
# 
# 
# 
# 
# 提示：
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 
# -100 
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        ret = []
        up,down,left,right = 0,m-1,0,n-1
        while up < down and left < right:
            for x in range(left,right):
                ret.append(matrix[up][x])
            for y in range(up,down):
                ret.append(matrix[y][right])
            for x in range(right,left,-1):
                ret.append(matrix[down][x])
            for y in range(down,up,-1):
                ret.append(matrix[y][left])  
            up,down,left,right = up + 1 ,down - 1,left + 1,right - 1
        
        if up == down:
            for x in range(left,right+1):
                ret.append(matrix[up][x])
            return ret
        if left == right:
            for y in range(up,down+1):
                ret.append(matrix[y][right])
            return ret
        return ret
            
# @lc code=end
matrix = [[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]
solution = Solution()
print (solution.spiralOrder(matrix))

