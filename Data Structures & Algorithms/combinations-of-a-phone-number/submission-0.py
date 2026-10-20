class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if len(digits) == 0:
            return []

        res = []
        
        num_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        size = len(digits)

        def dfs(i,curr_path):

            if len(curr_path) == size:
                res.append(curr_path)
                return


            # do

            # recurse

            print(curr_path)

            for letter in num_map[digits[i]]:
                curr_path += letter
                dfs(i+1,curr_path)
                curr_path = curr_path[0:-1]

            # undo

        dfs(0,"")

        return res

