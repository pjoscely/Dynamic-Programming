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


#Classic naive Fibonacci recursion -> O(2^n) time complexity

import time
def fib(n): 
   
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)



#Top-down dynamic Fibonacci solution
#Compute the nth Fibonacci number recursively.
#Optimized by caching subproblem results yields
#O(n) time and space complexity.


def fib_cache(n):
    if (n < 2):
        return n
# Create cache and initialize to -1
    cache = [-1]*(n+1)

# Fill initial values in cache
    cache[0] = 0
    cache[1] = 1
    return fib_cache_helper(n, cache)

# 
def fib_cache_helper(n, cache):
# If value is set in cache, return
    if (cache[n] >= 0):
        return cache[n]
# Compute and add to cache before returning
    cache[n] = fib_cache_helper(n-1, cache) + fib_cache_helper(n-2, cache)
    return cache[n]



#Bottom-up dynamic Fibonacci solution
#Compute the nth Fibonacci number iteratively
#yields O(n) time and space complexity.


def fib_bottom_up(n):
    if (n < 2):
        return n
# Define cache
    cache = []
# Initialize cache
    cache.append(0)
    cache.append(1)

# Fill cache iteratively
    for i in range (2, n+1):
        cache.append(cache[i-1] + cache[i-2])
    return cache[n]


#Optimized bottom-up dynamic Fibonacci
#Compute the nth Fibonacci number iteratively with O(n) tine but O(1) space.

def fib_iter(n):    
 if (n < 2):
     return n;
 n1 = 1
 n2 = 0
 for i in range(2, n):
     n0 = n1 + n2
     n2 = n1
     n1 = n0

 return n1 + n2;

#TEST HARNESS
print("This test harness computes a Fibonnaci number using each")
print("of the four methods along with run times.")
print("Suggestion: please start small." )

n= int(input('Enter a non-negative integer:'))
t0 = time.time()
f = fib(n)
t1 = time.time()
print("Test naive Fibonacci method")
print("Fibonacci of",n,"=",f,"time:",(t1-t0),"secs")

t0 = time.time()
f = fib_cache(n)
t1 = time.time()
print("Test the cache Fibonacci method")
print("Fibonacci of",n,"=",f,"time:",(t1-t0),"secs")

t0 = time.time()
f = fib_bottom_up(n)
t1 = time.time()
print("Test the bottom_up Fibonacci method")
print("Fibonacci of",n,"=",f,"time:",(t1-t0),"secs")

t0 = time.time()
f = fib_iter(n)
t1 = time.time()
print("Test the iterative Fibonacci method")
print("Fibonacci of",n,"=",f,"time:",(t1-t0),"secs")

""" 
**** Sample Output ****
This test harness computes a Fibonnaci number using each
of the four methods along with run times.
Suggestion: please start small.

Enter a non-negative integer:30
Test naive Fibonacci method
Fibonacci of 30 = 832040 time: 0.48146605491638184 secs
Test the cache Fibonacci method
Fibonacci of 30 = 832040 time: 2.2172927856445312e-05 secs
Test the bottom_up Fibonacci method
Fibonacci of 30 = 832040 time: 1.1920928955078125e-05 secs
Test the iterative Fibonacci method
Fibonacci of 30 = 832040 time: 6.198883056640625e-06 secs
"""