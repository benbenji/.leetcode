#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#
# https://leetcode-cn.com/problems/implement-strstr/description/
#
# algorithms
# Easy (40.22%)
# Likes:    1384
# Dislikes: 0
# Total Accepted:    620.6K
# Total Submissions: 1.5M
# Testcase Example:  '"hello"\n"ll"'
#
# 实现 strStr() 函数。
# 
# 给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0
# 开始）。如果不存在，则返回  -1 。
# 
# 
# 
# 说明：
# 
# 当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
# 
# 对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与 C 语言的 strstr() 以及 Java 的 indexOf()
# 定义相符。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：haystack = "hello", needle = "ll"
# 输出：2
# 
# 
# 示例 2：
# 
# 
# 输入：haystack = "aaaaa", needle = "bba"
# 输出：-1
# 
# 
# 示例 3：
# 
# 
# 输入：haystack = "", needle = ""
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= haystack.length, needle.length <= 10^4
# haystack 和 needle 仅由小写英文字符组成
# 
# 
#

# @lc code=start
from operator import ne


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def getNext(s:str):
            j = -1
            next = {}
            next[0] = j
            for i in range(1,len(s)):
                while s[i] != s[j+1] and j >= 0:
                    j = next[j]
                if s[i] == s[j +1]:
                    j +=1
                next[i] = j
            return next
        next = getNext(needle)
        j = -1
        for i in range(len(haystack)):
            while j>=0 and needle[j + 1] != haystack[i]:
                j = next[j]
            if needle[j + 1] == haystack[i]:
                j = j + 1
            if j==len(needle) - 1:
                return i-len(needle) + 1
        return -1
# @lc code=end
solution = Solution()
solution.strStr("mississippi","issip")

