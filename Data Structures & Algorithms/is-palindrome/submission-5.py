class Solution:
    def isPalindrome(self, s: str) -> bool:
        

        # only take in alphanumeric

        res = []

        for L in range(len(s)):
            if (s[L] >= 'a' and s[L] <= 'z') or (s[L] >= 'A' and s[L] <= 'Z'):
                to_input = (s[L]).lower()
                res.append(to_input)
            elif (s[L] >= '0' and s[L] <= '9'):
                res.append(s[L])

        R = len(res) - 1

        print(res)

        for L in range((len(res)//2)):
            if res[L] != res[R]:
                return False
            R -= 1

        return True