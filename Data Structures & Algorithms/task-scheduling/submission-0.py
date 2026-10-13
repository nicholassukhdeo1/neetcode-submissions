class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        # look at all tasks that you are ALLOWED to add

        # the best one to add is the one with the highest frequency


        counts = Counter(tasks)
        max_heap = [-cnt for cnt in counts.values()]
        heapq.heapify(max_heap)

        q = deque()  # stores tuples of (remaining_count, available_at_time)
        time = 0

        while max_heap or q:
            time += 1
            if max_heap:
                cnt = heapq.heappop(max_heap) + 1  # decrements count since negative
                if cnt < 0:
                    q.append((cnt, time + n))
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])

                     
        return time


