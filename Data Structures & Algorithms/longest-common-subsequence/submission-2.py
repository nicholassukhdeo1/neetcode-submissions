class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        cache = [[0] * len(text2) for _ in range(len(text1))]
        
        def dfs(i1,i2,cache):
            if i1 >= len(text1):
                return 0
            if i2 >= len(text2):
                return 0
            if cache[i1][i2] > 0:
                return cache[i1][i2]
    
            if text1[i1] == text2[i2]:
                cache[i1][i2] = 1 + dfs(i1+1,i2+1,cache)
            else:
                cache[i1][i2] = max(dfs(i1+1,i2,cache),dfs(i1,i2+1,cache))

            return cache[i1][i2]

        return dfs(0,0,cache)

        
            