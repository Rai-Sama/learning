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
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        # Anshuman -- arrays

        # Notes:
        ## Solved in O(n) TC and O(n) SC - beat 100% of TC!! SC can be improved to O(1) by avoiding slicing - but that feels like too much unnecessary work

        n = len(intervals)
        i = 0
        
        while i < n: # Skipping any non-overlapping earlier intervals
            if intervals[i][1] < newInterval[0]:
                i += 1
            else: # Found an overlap or a later interval
                break

        if i == n: # Edge case 1: If no later intervals (add to the end)
            intervals.append(newInterval)
            return intervals

        elif i == 0 and newInterval[1] < intervals[0][0]: # Edge case 2: If no earlier intervals (new interval is the first one)
            intervals = [newInterval] + intervals
            return intervals
        
        if newInterval[1] < intervals[i][0]: # If there is no overlap
            intervals = intervals[:i] + [newInterval] + intervals[i:]
            return intervals

        newInterval[0] = min(intervals[i][0], newInterval[0]) # Start time of the merged interval
        
        mark = i # Marking the overlap location for insertion later

        while i < n and newInterval[1] >= intervals[i][0]: # Finding the End time of the merged interval
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1

        if i == n: # All following intervals were merged into the new interval
            intervals = intervals[:mark] + [newInterval]

        else: # Merged somewhere in between
            intervals = intervals[:mark] + [newInterval] + intervals[i:]

        return intervals       
# @leet end
