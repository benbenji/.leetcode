#
# @lc app=leetcode.cn id=459 lang=python3
#
# [459] 重复的子字符串
#
# https://leetcode-cn.com/problems/repeated-substring-pattern/description/
#
# algorithms
# Easy (50.89%)
# Likes:    676
# Dislikes: 0
# Total Accepted:    108.5K
# Total Submissions: 213.3K
# Testcase Example:  '"abab"'
#
# 给定一个非空的字符串 s ，检查是否可以通过由它的一个子串重复多次构成。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: s = "abab"
# 输出: true
# 解释: 可由子串 "ab" 重复两次构成。
# 
# 
# 示例 2:
# 
# 
# 输入: s = "aba"
# 输出: false
# 
# 
# 示例 3:
# 
# 
# 输入: s = "abcabcabcabc"
# 输出: true
# 解释: 可由子串 "abc" 重复四次构成。 (或子串 "abcabc" 重复两次构成。)
# 
# 
# 
# 
# 提示：
# 
# 
# 
# 
# 1 <= s.length <= 10^4
# s 由小写英文字母组成
# 
# 
#
# class Solution:
#     def repeatedSubstringPattern(self, s: str) -> bool:
#         n = len(s)
#         for i in range(1, n // 2 + 1):
#             if n % i == 0:
#                 if all(s[j] == s[j - i] for j in range(i, n)):
#                     return True
#         return False

# @lc code=start
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) == 0:
            return False
        match = False
        for i in range(1,len(s)//2+1):
            if len(s) % i == 0:
                for k in range(i,len(s)):
                    if s[k] != s[k-i]:
                        match = False
                        break
                else:
                    match = True
                    break
        return match
                

# @lc code=end
solution = Solution()
solution.repeatedSubstringPattern("ababab")

