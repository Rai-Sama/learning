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
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Anshuman -- arrays -- patterns/two_pointers
        i = j = 0 # i: first 0, j: first non-zero; we will swap i,j
        n = len(nums)
        while j < n and i < n:
            
            while i < n and nums[i] != 0: # Find first 0
                i += 1
            
            while j < n and nums[j] == 0: # Find first non-zero
                j += 1
            
            if i < j and j < n: # Did we find both?
                    nums[i] = nums[j] # Swap
                    nums[j] = 0 # Swap

                    i += 1 # To avoid infinite loops
                    j += 1 # To avoid infinite loops

            elif i > j: # If first 0 is after the first number
                j = i # Start searching for numbers after the first 0





# @leet end        
