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
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Anshuman -- arrays -- data_structures/hash_map
        cnts = {}
        for i in nums:
            if i in cnts:
                return True
            else:
                cnts[i] = 1
        return False

# @leet end
