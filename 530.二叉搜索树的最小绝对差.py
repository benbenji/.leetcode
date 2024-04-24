#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] 二叉搜索树的最小绝对差
#
# https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/description/
#
# algorithms
# Easy (62.52%)
# Likes:    340
# Dislikes: 0
# Total Accepted:    113.1K
# Total Submissions: 180.2K
# Testcase Example:  '[4,2,6,1,3]'
#
# 给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。
# 
# 差值是一个正数，其数值等于两值之差的绝对值。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [4,2,6,1,3]
# 输出：1
# 
# 
# 示例 2：
# 
# 
# 输入：root = [1,0,48,null,null,12,49]
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点的数目范围是 [2, 10^4]
# 0 <= Node.val <= 10^5
# 
# 
# 
# 
# 注意：本题与 783
# https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/ 相同
# 
#

# @lc code=start
# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        def middleorder(root:TreeNode,res:List):
            if root == None:
                return
            middleorder(root.left,res) 
            res.append(root.val)
            middleorder(root.right,res)
        res =[]
        middleorder(root,res)
        diff = 10**5
        for i in range(len(res)-1):
            if diff > res[i+1]- res[i]:
                diff = res[i+1] - res[i]
        
        return diff
# [543,384,652,null,445,null,699]
node1 = TreeNode(543)
node2 = TreeNode(384)
node3 = TreeNode(652)
node4 = TreeNode(445)
node5 = TreeNode(699)
node1.left = node2
node1.right = node3
node2.right = node4
node3.right = node5
solution = Solution()
solution.getMinimumDifference(node1)
# @lc code=end

