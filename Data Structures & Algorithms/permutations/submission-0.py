class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []

        size = len(nums)
        pick = [False for i in range(size)]

        print(pick)

        num_count = Counter(nums)
        


        def dfs(s_index,curr_path,pick):

            if len(curr_path) == size:
                res.append(curr_path.copy())
                return

            for i in range(size):
                if pick[i] == False:
                    curr_path.append(nums[i])
                    pick[i] = True
                    dfs(i+1,curr_path.copy(),pick)
                    curr_path.pop()
                    pick[i] = False


        dfs(0,[],pick)

        return res

