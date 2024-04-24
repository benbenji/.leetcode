#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] 反转字符串 II
#
# https://leetcode-cn.com/problems/reverse-string-ii/description/
#
# algorithms
# Easy (59.54%)
# Likes:    278
# Dislikes: 0
# Total Accepted:    106.6K
# Total Submissions: 179.1K
# Testcase Example:  '"abcdefg"\n2'
#
# 给定一个字符串 s 和一个整数 k，从字符串开头算起，每计数至 2k 个字符，就反转这 2k 字符中的前 k 个字符。
# 
# 
# 如果剩余字符少于 k 个，则将剩余字符全部反转。
# 如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "abcdefg", k = 2
# 输出："bacdfeg"
# 
# 
# 示例 2：
# 
# 
# 输入：s = "abcd", k = 2
# 输出："bacd"
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 10^4
# s 仅由小写英文组成
# 1 <= k <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        def reverse(left:int,right:int):
            while left < right:
                s[left],s[right] = s[right],s[left]
                left, right = left + 1,right - 1
        s = list(s) 
        i,j = 0,len(s) - 1
        for n in range(0,len(s),2 *k):
            if n+k-1 <= j:
                reverse(n,n+k-1)
            else:
                reverse(n,j)
        return "".join(s)

# @lc code=end
solution = Solution()
solution.reverseStr("abcd",k=2)
