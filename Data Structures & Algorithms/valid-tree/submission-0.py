class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        tree = {root: [] for root in range(n)}

        for root,kids in edges:
            tree[root].append(kids)
            tree[kids].append(root)

        visit = set()

        def dfs(node, prev):
            # we have returned to the node
            if node in visit:
                return False

            visit.add(node)
            # for an entire route, i better not see a duplicate arise.

            for neighbor in tree[node]:
                if neighbor == prev:
                    continue
                if not dfs(neighbor, node):
                    return False

            return True

        return dfs(0, -1) and len(visit) == n