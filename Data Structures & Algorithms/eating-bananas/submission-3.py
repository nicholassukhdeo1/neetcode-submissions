class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # you represent an array by using L and R
        L = 1
        R = max(piles)

        res = R


        while L <= R:
            time_req = 0
            mid_k = (L+R) // 2

            for nanners in piles:
                # calculate time to consume
                time_req += math.ceil(nanners/mid_k)
            if time_req > h:
                L = mid_k+1
            elif time_req <= h:
                res = min(res,mid_k)
                R = mid_k-1

        return res