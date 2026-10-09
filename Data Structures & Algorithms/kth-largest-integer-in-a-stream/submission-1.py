import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # min heap doesnt require weird business

        self.kth_largest = []
        self.k = k

        for num in nums:
            heapq.heappush(self.kth_largest,num)

        return

        

    def add(self, val: int) -> int:

        heapq.heappush(self.kth_largest,val)

        while len(self.kth_largest) > self.k:
            heapq.heappop(self.kth_largest)

        return self.kth_largest[0]

        
        
