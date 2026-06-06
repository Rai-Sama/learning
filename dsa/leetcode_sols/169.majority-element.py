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
    def majorityElement(self, nums: List[int]) -> int:
        # Anshuman -- divide_conquer -- data_structures/hash_map
        '''
        cnts = {}
        n = len(nums)
        if n <= 2:
            return nums[0]
        for i in nums:
            if i in cnts:
                cnts[i] += 1
                if cnts[i] > n/2:
                    return i
            else:
                cnts[i] = 1
        '''
        res = nums[0]
        cnt = 0
        for i in nums[1:]:
            if i != res:
                cnt -= 1
                if cnt < 0:
                    res, cnt = i, 0
            else:
                cnt += 1
        return res
        
# @leet end
