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
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Anshuman -- data_structures/linked_list
        val1 = l1.val
        val2 = l2.val
        carry = 0
        res = ListNode()
        prev = res
        while l1 != None or l2 != None or carry != 0: # All 3 must be false
            val1 = l1.val if l1 != None else 0
            val2 = l2.val if l2 != None else 0
            val = val1 + val2 + carry
            carry = val//10
            curr = ListNode(val%10)
            prev.next = curr
            prev = curr

            l1 = l1.next if l1 != None else None
            l2 = l2.next if l2 != None else None

        return res.next

# @leet end

