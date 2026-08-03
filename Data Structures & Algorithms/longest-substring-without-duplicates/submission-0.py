class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        L = 0
        length = 0
        sub = []
        

        for R in range(len(s)):
        
            while s[R] in sub:
                sub.pop(0)
                L += 1

            sub.append(s[R])

            length = max(length, len(sub))
                

            


        return length