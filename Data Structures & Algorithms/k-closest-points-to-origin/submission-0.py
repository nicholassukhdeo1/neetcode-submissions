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
        res.sort()

        for j in range(len(res)):
            res2.append(res[j][1])

            k -= 1

            if k == 0:
                break



        return res2

        