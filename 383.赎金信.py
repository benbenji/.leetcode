#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#
# https://leetcode-cn.com/problems/ransom-note/description/
#
# algorithms
# Easy (64.41%)
# Likes:    308
# Dislikes: 0
# Total Accepted:    157.1K
# Total Submissions: 243.9K
# Testcase Example:  '"a"\n"b"'
#
# 给你两个字符串：ransomNote 和 magazine ，判断 ransomNote 能不能由 magazine 里面的字符构成。
# 
# 如果可以，返回 true ；否则返回 false 。
# 
# magazine 中的每个字符只能在 ransomNote 中使用一次。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：ransomNote = "a", magazine = "b"
# 输出：false
# 
# 
# 示例 2：
# 
# 
# 输入：ransomNote = "aa", magazine = "ab"
# 输出：false
# 
# 
# 示例 3：
# 
# 
# 输入：ransomNote = "aa", magazine = "aab"
# 输出：true
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= ransomNote.length, magazine.length <= 10^5
# ransomNote 和 magazine 由小写英文字母组成
# 
# 
#

# @lc code=start
from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        record_m = defaultdict(int)
        for s in magazine:
            record_m[s] = record_m[s] + 1

        for s in ransomNote:
            record_m[s] = record_m[s] - 1
            if record_m[s] < 0:
                return False
        
        return True
# @lc code=end

