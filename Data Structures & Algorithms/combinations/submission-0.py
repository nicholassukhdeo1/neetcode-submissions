class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        # we need to make

        res = []

        curCombo = []

        def helper(res,curCombo,start):

            if len(curCombo) == k:
                res.append(curCombo.copy())
                return

            # obviously, no more return 
            if start > n:
                return
            
            # each recursive call of helper should make all pairs
            # for a specific number

            for i in range(start,n+1):

                curCombo.append(i)
                helper(res,curCombo,i+1)
                curCombo.pop()


            # what is backtracking again?



        helper(res,curCombo,1)

        return res



