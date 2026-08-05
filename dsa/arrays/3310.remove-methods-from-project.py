# Anshuman -- arrays

from typing import *

from leetgo_py import *

# @lc code=begin

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        # Move forward -- add to dicts (K -> V), if K becomes suspicious (set) all V become suspicious
        # Remove suspicious set from set of all nodes
        # If anything remains, check if any of its dict V's are suspicious
        # If not, return them. If true for any one, return set of all nodes
        # If nothing remained just return the empty List
        nodes = [x for x in range(n)]
        sus = {k}
        rels = [[] for x in nodes]
        for i in invocations:
            rels[i[0]].append(i[1])

        check = [x for x in sus]
        while check:
            x = check.pop()
            for y in rels[x]:
                if not y in sus:
                    sus.add(y)
                    check.append(y)

        # remove sus nodes from master set
        remaining = [x for x in nodes if not x in sus]

        for x in remaining:
            for y in rels[x]:
                if y in sus:
                    return nodes
        return remaining

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    invocations: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().remainingMethods(n, k, invocations)
    print("\noutput:", serialize(ans, "integer[]"))
