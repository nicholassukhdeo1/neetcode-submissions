class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        

        for i in range(len(nums)):
            nums[i] = nums[i] * -1
        
        
        # we'll have smth in tree form thatll look like[-6,-5,-4]
        heapq.heapify(nums)


        while k > 0:
            insert = heapq.heappop(nums)
            k -= 1


        return insert * -1
