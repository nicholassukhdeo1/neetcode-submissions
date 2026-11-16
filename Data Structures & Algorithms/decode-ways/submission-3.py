class Solution:
    def numDecodings(self, s: str) -> int:
        

        cache = {}

        size = len(s)

        # we want dfs to return the answer


        def dfs(index):

            if index >= size:
                return 1

            if s[index] == "0":
                return 0

            if index in cache:
                return cache[index]

            # only go further in the number list if all nums are valid

            cache[index] = dfs(index+1)

            if index+1 < size:
                # at each step, will a new path emerge?
                if s[index] == "1" or (s[index] == "2" and s[index+1] in "0123456"):
                    cache[index] += dfs(index+2)


            return cache[index]



        return dfs(0)