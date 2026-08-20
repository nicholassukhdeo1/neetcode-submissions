"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        # lets do DFS

        # on each pass, change the key

        visit = {}

        def helper(OG_graph, visit):

            # base cases.. 

            # if you are looking at nothing, backtrack
            if OG_graph is None:
                return
            # if this node has already been cloned, backtrack
            if OG_graph in visit:
                return visit[OG_graph]

            # backtracking, do, undo, recurse.

            # do (create copy)
            new_copy = Node(OG_graph.val)
            visit[OG_graph] = new_copy
            # recurse (explore all neighbors)

            for neighbor in OG_graph.neighbors:
                copy_neighbor = helper(neighbor, visit)
                if copy_neighbor:
                    new_copy.neighbors.append(copy_neighbor)

            # undo?

            return new_copy
            
            
        
        return helper(node,visit)

                
