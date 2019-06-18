#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Adapted from https://www.byte-by-byte.com/dpbook/

# Copyright (c) 2019 Charles Joscelyne
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

"""
Given an integer representing a given amount of change, write a
function to compute the total minunum number of coins required 
to make that amount of change. You can assume that there is 
always a1¢ coin.

eg. (assuming US coins: 1, 5, 10, and 25 cents)
makeChange(1) = 1 (1)
makeChange(6) = 2 (5 + 1)
makeChange(49) = 7 (25 + 10 + 10 + 1 + 1 + 1 + 1)


Naive Making Change solution
Brute force solution. Go through every
combination of coins that sum up to c to
find the minimum number
"""
import math 
import time
coins = [10, 6, 1]
def makeChange(c):
    if (c == 0):
        return 0;
    minCoins = math.inf; #set minCoins to infinity 
# Try removing each coin from the total and
# see how many more coins are required
    for coin in coins:
# Skip a coin if it’s value is greater
# than the amount remaining
        if (c - coin) >= 0:
            currMinCoins = makeChange(c - coin)
            if (currMinCoins < minCoins):
                minCoins = currMinCoins
# Add back the coin removed recursively
    return minCoins + 1

#Top down dynamic making change solution. Cache the values as we compute them.
#Uses only using O(c) space, even with the recursive stack.
#The time complexity is a O(c * (number of coins).

def makeChange_Cache(c):
# Initialize cache with values as -1
 cache = [-1]*(c+1)
 cache[0] = 0
 
 return makeChange_helper(c, cache)

# Recursive helper function
def makeChange_helper(c, cache):
# Return the value if it’s in the cache
    if (cache[c] >= 0):
        return cache[c]
    minCoins = math.inf; #set minCoins to infinity 

# Find the best coin
    for coin in coins:
        if (c - coin) >= 0:
            currMinCoins = makeChange_helper(c - coin, cache)
            if (currMinCoins < minCoins):
                minCoins = currMinCoins

# Save the value into the cache
    cache[c] = minCoins + 1
    return cache[c]

#Bottom up dynamic programming solution.
#Iteratively compute number of coins for
#larger and larger amounts of change
def makeChange_Bottom_Up(c):
    cache = [0]*(c+1) #create cache
    for i in range(1, c+1):
        minCoins = math.inf
        for coin in coins:
            if (i - coin) >= 0:
                currCoins = cache[i-coin] + 1
                if (currCoins < minCoins):
                    minCoins = currCoins;
        cache[i] = minCoins 
    return cache[c]

#TEST HARNESS
print("This test harness computes the mininum number of coins need") 
print("for a given amount using coins: 10, 6, 1 for the")
print("three above methods along with their run times.")
print("Suggestion: please start small." )

n = int(input('Enter a non zero amount:'))
t0 = time.time()
f = makeChange(n)
t1 = time.time()
print("Test naive make change method")
print("Mininum of coins for amount",n,"=",f,"coins, time:",(t1-t0),"secs")


t0 = time.time()
f = makeChange_Cache(n)
t1 = time.time()
print("Test Cache change method")
print("Mininum of coins for amount",n,"=",f,"coins, time:",(t1-t0),"secs")


t0 = time.time()
f = makeChange_Bottom_Up(n)
t1 = time.time()
print("Test bottom up change method")
print("Mininum of coins for amount",n,"=",f,"coins, time:",(t1-t0),"secs")











