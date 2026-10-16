class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        

        res = []

        size = len(nums)


        def helper(c_dx,c_array):


            res.append(c_array.copy())

            for i in range(c_dx,size):
                
                c_array.append(nums[i])
        

                helper(i+1,c_array.copy())
                c_array.pop()

                print(c_array)


        helper(0,[])

        return res
                
                