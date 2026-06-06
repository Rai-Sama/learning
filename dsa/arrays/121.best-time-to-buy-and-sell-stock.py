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
    def maxProfit(self, prices: List[int]) -> int:
        # Anshuman -- arrays -- dp
        i = 0
        j = i + 1
        res = 0
        while i < len(prices) and j < len(prices):
            if prices[j] < prices[i]:
                i = j
                j += 1
            else:
                res = max(res, prices[j] - prices[i])
                j += 1
        return res
            
# @leet end
