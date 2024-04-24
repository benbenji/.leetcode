#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#
# https://leetcode-cn.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (57.45%)
# Likes:    1872
# Dislikes: 0
# Total Accepted:    569.4K
# Total Submissions: 989.8K
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# 给你一个二叉树的根节点 root ， 检查它是否轴对称。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [1,2,2,3,4,4,3]
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 输入：root = [1,2,2,null,3,null,3]
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点数目在范围 [1, 1000] 内
# -100 <= Node.val <= 100
# 
# 
# 
# 
# 进阶：你可以运用递归和迭代两种方法解决这个问题吗？
# 
#

# @lc code=start
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: 
            return True
        else:
            return self.compare(root.left,root.right)
    def compare(self,left:TreeNode,right:TreeNode):
        if left==None and right!=None:
            return False
        if left!=None and right ==None:
            return False
        if left==None and right == None:
            return True
        if left.val != right.val:
            return False
        else :
            outside = self.compare(left.left,right.right)
            inside = self.compare(left.right,right.left)
            return outside and inside
# @lc code=end

