class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        #initialize adjacency list
        tree = {root: [] for root in range(n)}

        for root, kids in edges:
            tree[root].append(kids)
            tree[kids].append(root)
        
        count = 0

        visit = set()

        def dfs(root,prev):
            if root in visit:
                return
            if tree[root] == []:
                return
            
            #singular, no edges node.

            

            visit.add(root)

            for kids in tree[root]:
                if kids == prev:
                    continue

                dfs(kids,root)
        
        for index in range(n):
            if index not in visit:
                count += 1
                dfs(index,-1)
                



        return count


        