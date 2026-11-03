class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        

        graph = {i: [] for i in range(numCourses)}

        for course, pre in prerequisites:
            graph[pre].append(course)

        # the membership/find fxn for sets are much cheaper
        # than lists
        gray = set()
        black = set()
        finish = []

        def dfs(node):

            # cycle detected
            if node in gray:
                return False

            # add to finish_list
            if node in black:
                return True

            gray.add(node)
            for nxt in graph[node]:
                # if this node doesnt create cycle
                if not dfs(nxt):
                    return False

            gray.remove(node)
            black.add(node)
            finish.append(node)
            return True


        for node in range(numCourses):
            if not dfs(node):
                return []

        return finish[::-1]

