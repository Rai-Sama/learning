# Anshuman -- arrays

from typing import *

from leetgo_py import *

# @lc code=begin


class Solution:
    def remainingMethods(
        self, n: int, k: int, invocations: List[List[int]]
    ) -> List[int]:
        # Move forward -- add to dicts (K -> V), if K becomes suspicious (set) all V become suspicious
        # Remove suspicious set from set of all nodes
        # If anything remains check if any of its dict V's are suspicious
        # If not, return them. If true for any one, return set of all nodes
        # If nothing remained just return the empty List
        nodes = set()
        sus = {k}
        unsus = set()
        rels = {}
        master = {}
        good_nodes = {}
        for i in invocations:
            nodes.update([i[0], i[1]])  # Add new nodes to master set of nodes
            if i[0] in rels:
                rels[i[0]].add(i[1])  # Add edge
            else:
                rels[i[0]] = {i[1]}  # Edge from a new node
            if i[0] in sus:
                sus.add(i[1])  # Incoming node is sus so this node is sus
                if i[1] in rels:
                    sus.update(
                        rels[i[1]]
                    )  # All edges outgoing from sus node become sus

        # remove sus nodes from master set
        remaining = nodes - sus

        for x in remaining:
            if x in rels:
                good_nodes = sus - rels[x]
            else:
                good_nodes = sus
            if len(good_nodes) < len(
                sus
            ):  # Non-suspicious link goes to a sus one - removal impossible scenario
                sol = list(nodes)
                return sol
        sol = list(remaining)
        return sol


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    invocations: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().remainingMethods(n, k, invocations)
