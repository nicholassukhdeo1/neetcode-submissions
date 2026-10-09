class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # wait.. this was a lab.

        # choose the heaviest stones.. smash em


        # but we want maxheap logic

        stone_len = len(stones)


        for i in range(stone_len):
            stones[i] = stones[i] * -1

        heapq.heapify(stones)

        print(stones)

        # now we have max heap.
        j = 0

        # while stones is not empty
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if x == y:
                continue
            elif x < y:
                y = x + (y*-1)
                heapq.heappush(stones,y)

            print(stones[0] * -1)


        if len(stones) == 1:
            return stones[0] * -1
        else:
            return 0



