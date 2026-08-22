class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # is there a logical chain of courses

        visit = set()

        preMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        def dfs(crs):

            # base case
            # end recursion when we have an unvalid prereq

            # if the prereq's prereq is the course... return false.

            if crs in visit:
                return False
            if preMap[crs] == []:
                return True

            visit.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            preMap[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True