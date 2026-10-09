class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:


        res = []
        res2 = []

        for i in range (len(points)):
            x = (points[i][0] - 0) ** 2
            y = (points[i][1] - 0) ** 2
            dist = (x + y) ** 0.5

            res.append((dist,points[i]))


        # sorts in ascending order
        heapq.heapify(res)

        # this dont work cuz min heap ordering isnt contiguous



        while k > 0:
            dist, point = heapq.heappop(res)
            res2.append(point)

            k -= 1


        return res2

        