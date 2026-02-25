class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        last = {}
        left = 0
        max_len = 0

        for right,char in enumerate(s):
            if char in last and last[char]>=left:
                left = last[char]+1
            
            current = right-left+1
            if current > max_len:
                max_len = current
            
            last[char]=right
        
        return max_len