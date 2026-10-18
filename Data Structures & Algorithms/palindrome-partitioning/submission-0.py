class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        size = len(s)
        res = []

        def dfs(s_dx,curr_path):

            if s_dx == len(s):
                res.append(curr_path.copy())
                return

            for i in range(s_dx,len(s)):
                
                sub = s[s_dx:i+1]

                if isPalindrome(sub):
                    curr_path.append(sub)
                    dfs(i+1,curr_path.copy())
                    curr_path.pop()

                # undo merge
                

                
                
                
        def isPalindrome(candidate):
            R = len(candidate) - 1

            final_dx = len(candidate)//2 

            for L in range(final_dx):
                if (candidate[L] != candidate[R]):
                    return False
                R -= 1

            return True

        
        dfs(0,[])
        
        return res


