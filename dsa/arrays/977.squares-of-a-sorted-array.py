# @leet imports start
from string import *
from re import *
from datetime import *
from collections import *
from heapq import *
from bisect import *
from copy import *
from math import *
from random import *
from statistics import *
from itertools import *
from functools import *
from operator import *
from io import *
from sys import *
from json import *
from builtins import *
import string
import re
import datetime
import collections
import heapq
import bisect
import copy
import math
import random
import statistics
import itertools
import functools
import operator
import io
import sys
import json
from typing import *
# @leet imports end

# @leet start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Anshuman -- arrays -- patterns/two_pointers
        n = len(nums)
        res = [0]*n
        n = len(nums)
        i = 0
        j = n-1
        for k in range(n-1, -1, -1):
            if abs(nums[i]) > abs(nums[j]):
                res[k] = nums[i]*nums[i]
                i += 1
            else:
                res[k] = nums[j]*nums[j]
                j -= 1
        return res
# @leet end
