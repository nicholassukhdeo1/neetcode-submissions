class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # we have different algos to check palindromes for
        # even and odd length. check different middles

        resLen = 0
        res = ""
        size = len(s)


        for middle_index in range(len(s)):

            # check even's middle (an actual letter)
            left, right = middle_index, middle_index

            while left >= 0 and right < size and s[left] == s[right]:
                if (right - left + 1) > resLen:
                    res = s[left:right+1]
                    resLen = right - left + 1

                left -= 1
                right += 1

            # check odd's middle (between left and right letters)

            left, right = middle_index, middle_index+1

            while left >= 0 and right < size and s[left] == s[right]:
                if (right - left + 1) > resLen:
                    res = s[left:right+1]
                    resLen = right - left + 1

                left -= 1
                right += 1

        return res

        