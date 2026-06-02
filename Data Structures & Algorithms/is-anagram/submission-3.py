class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # hash table

        # nah lets do defaultdict and go on our ways

        if len(s) != len(t):
            return False

        count_s = defaultdict(int) #cuz that means our vals are ints
        count_t = defaultdict(int) #and each val starts as 0.

        word_len = len(s)

        for i in range(word_len):
            count_s[s[i]] += 1
            count_t[t[i]] += 1

        return count_s == count_t

