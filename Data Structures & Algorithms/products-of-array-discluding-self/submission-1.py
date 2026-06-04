class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # find the product first
        # then insert the product/curr_value
        # into your answer list

        # now, lets consider the edge case
        # what if we have a zero in the list?

        # there's two cases here,
        # with one zero in the list,
        # then every other value in our answer will be zero.
        # BUT, the index where the zero IS will be non-zero

        # the other case is: if we have more than one zero in the list
        # then EVERYTHING is zero

        prod = 1
        answer_list = [0] * len(nums)
        zero_count = 0



        for num in nums:
            if num != 0:
                prod *= num
            elif num == 0:
                zero_count += 1

        if zero_count > 1:
            return answer_list


        for index, num in enumerate(nums):
            if zero_count == 1:
                if nums[index] == 0:
                    answer_list[index] = prod
            else:
                product = prod // num
                answer_list[index] = product

        return answer_list