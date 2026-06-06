class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        max_sequence = 0
        curr_sequence = 1

        if len(nums) == 0:
            return 0

        max_sequence = 1
        for num in nums:
            if (num-1) in nums:
                curr_sequence += 1
                if curr_sequence > max_sequence:
                    max_sequence = curr_sequence
            else:
                curr_sequence = 1

        return max_sequence