"""
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ""
        maxLen = 0
        for char in s:
            print("substring", substring)
            if char in substring:
                print("1",substring.split(char))
                print("2", substring.split(char)[1] + char)
                substring = substring.split(char)[1] + char
            else:
                substring += char
                if len(substring) > maxLen: 
                    maxLen = len(substring)
            
        return maxLen
    
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = 0
        l = []
        s = list(map(lambda c: ord(c), s))
        for i in range(len(s)):
            m = self.maxStr(s[i:], m)
            if m not in l:
                l.append(m)
        return max(l) if l else 0
    def maxStr(self, s_list, max_v=0):
        sublist = []
        for c in s_list:
            if c in sublist:
                break
            sublist.append(c)
        return max(max_v, len(sublist))
        """

