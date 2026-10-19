class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []            


            
        

        def dfs(curr_path):

            if len(curr_path) == n*2:
                res.append("".join(curr_path))
                return


            paren_count = Counter(curr_path)
            open_count = paren_count['(']
            close_count = paren_count[')']
            

                # if more open than close, can add close


            if open_count < n:
                curr_path.append('(')
                dfs(curr_path.copy())
                curr_path.pop()
            
            if open_count > close_count:
                curr_path.append(')')
                dfs(curr_path.copy())
                curr_path.pop()


                # if you cant add close, add open



        dfs([])

        return res