# Anshuman -- math

from typing import *

from leetgo_py import *

# @lc code=begin

class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        m = n
        prod = 1
        while m:
            x = m % 10 
            prod = prod * x 
            if prod == 0: 
                return n
            m = m//10
        if prod % t == 0: 
            return n
        else:
            return self.smallestNumber(n+1, t)
        
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    t: int = deserialize("int", read_line())
    ans = Solution().smallestNumber(n, t)
    print("\noutput:", serialize(ans, "integer"))
