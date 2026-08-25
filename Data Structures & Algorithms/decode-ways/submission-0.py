class Solution:
    def numDecodings(self, s: str) -> int:
        

        size = len(s)
        cache = {}


        def helper(index):

            if index == size:
                return 1
            if "0" == s[index]:
                return 0
            if index in cache:
                return cache[index]

            cache[index] = helper(index+1)
            if index+1 <= size-1:
                if (s[index] == "1") or (s[index] == "2" and s[index+1] in "0123456"):
                    cache[index] += helper(index+2)

            
            return cache[index]


        
        
        return helper(0)




            