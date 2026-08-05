class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        counts = collections.defaultdict(int)
        max_f = 0
        length = 0
        for R in range(len(s)):
            counts[s[R]] += 1
            max_f = max(max_f, counts[s[R]])
            
            # If (current window size - frequency of most common character) > k,
            # we cannot make the window valid by replacing k characters.
            while (R - L + 1) - max_f > k:
                counts[s[L]] -= 1
                L += 1
                
            length = max(length, R - L + 1)

        return length