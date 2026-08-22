class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # make your adjacency list

        visit = set()

        preMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        

        def dfs(crs, visit):

            # cycle detected, this cant be a valid string of prereqs
            if crs in visit:
                return False
            # if the course has no prerequisites, it is guaranteed that there
            # is no cycle. so return true
            if preMap[crs] == []:
                return True

            visit.add(crs)

            for prereq in preMap[crs]:
                if not dfs(prereq,visit):
                    return False
            
            visit.remove(crs)
            preMap[crs] = []

            return True



        for class_index in range(numCourses):
            if not dfs(class_index,visit):
                return False
        return True