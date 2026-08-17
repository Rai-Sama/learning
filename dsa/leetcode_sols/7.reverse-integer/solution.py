# Anshuman -- TODO_PATH_1

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def reverse(self, x: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    x: int = deserialize("int", read_line())
    ans = Solution().reverse(x)
    print("\noutput:", serialize(ans, "integer"))
