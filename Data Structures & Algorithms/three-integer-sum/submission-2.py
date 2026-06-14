class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:


        answer_tuples = []
        nums.sort()

        for i in range(len(nums)):
            # initialize L at i+1 because you always want nums[i]
            # to be different from what nums[L] is. 
            L = i + 1
            R = len(nums) - 1
            while L < R:
                if nums[L] + nums[R] == -nums[i]: #yes, cuz then all these elements added are 0
                    curr_list = [nums[L], nums[R], nums[i]]
                    curr_tuple = tuple(sorted(curr_list))
                    answer_tuples.append(curr_tuple)
                    L += 1
                    R -= 1
                    continue

                # sum isnt big enough to counteract nums[i]?
                # make the sum bigger then.
                if nums[L] + nums[R] < -nums[i]:
                    L += 1
                # sum over-counteracts nums[i]? shrink it then
                else:
                    R -= 1


        return list(set(answer_tuples))