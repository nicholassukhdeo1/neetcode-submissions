class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        

        res = []
        nums.sort()

        def dfs(s_index,curr_path):

            # no need for base case, the for loop guarantees the s_index wont get too long

            # do 
            print(curr_path)

            if curr_path not in res:
                res.append(curr_path.copy())

            #recurse
            for i in range(s_index,len(nums)):
                curr_path.append(nums[i])
                dfs(i+1,curr_path.copy())
                curr_path.pop()


            # undo

            # you had a current_path, and start_index


        dfs(0,[])

        # unique = set(tuple(subset) for subset in res)

        # for key in unique:
        #     temp = list(key)
        #     res2.append(temp)

        return res