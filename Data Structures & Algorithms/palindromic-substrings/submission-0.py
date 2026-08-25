class Solution:
    def countSubstrings(self, s: str) -> int:
        
        res = []
        count = 0
        size = len(s)

        for start_index in range(len(s)):

            #even check (btwn two letters)
            left, right = start_index, start_index+1

            while left >= 0 and right < size and s[left] == s[right]:
                count += 1
    


                left -= 1
                right += 1

            #odd check (middle pt on a letter)

            left, right = start_index, start_index


            while left >= 0 and right < size and s[left] == s[right]:
                count += 1
    


                left -= 1
                right += 1

        return count



