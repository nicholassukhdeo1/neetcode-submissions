class Solution:
    def jump(self, nums: List[int]) -> int:
        


        
        # first group is everything one jump can reach

        # 2nd group is first group + everything this index can reach

        # 3rd group is second group + everything index can reach



        # [3,3,1,2,1,1]


        path_len = len(nums)

        start = 0

        next_start_point = 0

        jump = 0

        # choose the index that from there gets us the furthest

        curr_group_end = 0
        next_group_start = 0



        while curr_group_end < path_len-1:

            jump += 1

            for j in range(next_group_start,curr_group_end+1):

                # remember what j is

                candidate = j + nums[j]

                next_start_point = max(candidate,next_start_point)

            next_group_start = curr_group_end + 1
            curr_group_end = next_start_point



        return jump


            


            




            
            