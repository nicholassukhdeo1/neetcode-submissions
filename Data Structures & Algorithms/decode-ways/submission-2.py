class Solution:
    def numDecodings(self, s: str) -> int:
        
        size = len(s)

        cache = {}

        def dfs(index):
            if index == size:
                return 1
         
            if s[index] == "0":
                return 0

            if index in cache:
                return cache[index]

            cache[index] = dfs(index+1)
            if index+1 < size:
                if (s[index] == "1") or (s[index] == "2" and s[index+1] in "0123456"):
                    cache[index] += dfs(index+2)


            return cache[index]



        return dfs(0)
            