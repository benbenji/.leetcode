#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#
# https://leetcode-cn.com/problems/binary-tree-paths/description/
#
# algorithms
# Easy (69.40%)
# Likes:    721
# Dislikes: 0
# Total Accepted:    200.3K
# Total Submissions: 288.1K
# Testcase Example:  '[1,2,3,null,5]'
#
# 给你一个二叉树的根节点 root ，按 任意顺序 ，返回所有从根节点到叶子节点的路径。
# 
# 叶子节点 是指没有子节点的节点。
# 
# 
# 示例 1：
# 
# 
# 输入：root = [1,2,3,null,5]
# 输出：["1->2->5","1->3"]
# 
# 
# 示例 2：
# 
# 
# 输入：root = [1]
# 输出：["1"]
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点的数目在范围 [1, 100] 内
# -100 <= Node.val <= 100
# 
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
    def binaryTreePaths(self, root: Optional[TreeNode],) -> List[str]:
        result = []
        if root.right ==None and root.left==None:
            result.append(str(root.val))
        self.get_leavepath(root.left,str(root.val),result)
        self.get_leavepath(root.right,str(root.val),result) 
        return result
    def get_leavepath(self,root:TreeNode,previous_path,result:List[str]):
        if root== None:
            return None 
        path = previous_path+'->'+str(root.val)
        if root.left==None and root.right == None:
            return result.append(path)
        self.get_leavepath(root.left,path,result)
        self.get_leavepath(root.right,path,result)
        

# @lc code=end

