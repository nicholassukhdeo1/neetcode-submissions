class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        strip_string = []

        for char in s:
            if char.isalnum():
                strip_string.append(char.lower())

        L = 0
        R = len(strip_string) - 1


        for L in range(len(strip_string)):
            if strip_string[L] != strip_string[R]:
                return False
            R -= 1
            if L >= R:
                return True

        return True