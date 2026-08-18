class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res = []

        curCombo = []
        
        def helper(res,curCombo,start):
            
            # base case of recursion is to add a valid combo
            if len(curCombo) == k:
                res.append(curCombo.copy())
                return

            # edge case.. stop recursion if we're adding values not in our range
            if start > n:
                return


            for i in range(start,n+1):
                curCombo.append(i)
                helper(res,curCombo,i+1)
                curCombo.pop()





        helper(res,curCombo,1)

        return res



        