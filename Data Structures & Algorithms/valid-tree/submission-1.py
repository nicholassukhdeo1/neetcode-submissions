class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # build an adjacency list

        tree = {root: [] for root in range(n)}

        for root, kids in edges:
            tree[root].append(kids)
            tree[kids].append(root)

        visit = set()

        def dfs(curr,prev):
            if curr in visit:
                return False
            
            visit.add(curr)

            for children in tree[curr]:
                if children == prev:
                    continue
                if not dfs(children,curr):
                    return False

            return True




        return dfs(0,-1) and len(visit) == n