class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        substr = []
        memo = {len(s) : True}

        def helper(index): # return Bool
            if index in memo:
                return memo[index]

            

            
            for w in wordDict:
                if ((index+len(w))) <= len(s) and (s[index : index + len(w)] == w):
                    if helper(index + len(w)):
                        memo[index] = True
                        return True

            memo[index] = False
            return False



        return helper(0)