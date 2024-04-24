#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#
# https://leetcode-cn.com/problems/balanced-binary-tree/description/
#
# algorithms
# Easy (56.86%)
# Likes:    986
# Dislikes: 0
# Total Accepted:    347K
# Total Submissions: 609.8K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，判断它是否是高度平衡的二叉树。
# 
# 本题中，一棵高度平衡二叉树定义为：
# 
# 
# 一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [3,9,20,null,null,15,7]
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 输入：root = [1,2,2,3,3,null,null,4,4]
# 输出：false
# 
# 
# 示例 3：
# 
# 
# 输入：root = []
# 输出：true
# 
# 
# 
# 
# 提示：
# 
# 
# 树中的节点数在范围 [0, 5000] 内
# -10^4 
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if self.get_hight(root) == -1:
            return False
        else:
            return True
    def get_hight(self,root:TreeNode):
        if root == None:
            return 0
        if (right_high:= self.get_hight(root.right)) ==-1:
            return -1
        if (left_high:=self.get_hight(root.left)) == -1:
            return -1
        if abs(right_high-left_high) > 1:
            return -1
        return 1+max(right_high,left_high)
solution = Solution()

# @lc code=end

