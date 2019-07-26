#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 18:24:09 2019

@author: joscelynec
"""
"""
*** Rod Cutting Problem ***
You are given a rod of size n >0, it can be cut into 
any number of pieces k (k ≤ n). Price for each piece 
of size i is represented as p(i) and maximum revenue 
from a rod of size i is r(i) (could be split into 
multiple pieces). Find r(n) for the rod of size n.
"""


# Returns the best obtainable price for a rod of length n  
# and price[] as prices of different pieces 
#Slow recursive version
def cutRodSlow(price, n): 
    if(n <= 0): 
        return 0
    max_val = -float("inf")
      
    # Recursively cut the rod in different pieces   
    # and compare different configurations 
    for i in range(0, n): 
        max_val = max(max_val, price[i] + cutRodSlow(price, n - i - 1)) 
    return max_val 
  
# Driver code 
price = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30] 
print("Maximum Obtainable Value is", cutRodSlow(price, 4))

# Returns the best obtainable price for a rod of length n  
# and price[] as prices of different pieces 
#Uses memoziation  

def cutRod(price, n): 
    val = [0 for x in range(n+1)] 
    # Build the table val[] in bottom up manner and return 
    # the last entry from the table 
    for l in range(1, n+1): 
        max_val = -float("inf")
        for indx in range(l): 
             max_val = max(max_val, price[indx] + val[l-indx-1]) 
        val[l] = max_val 
  
    return val[n] 

print("Maximum Obtainable Value is", cutRod(price, 4))

"""
Maximum Obtainable Value is 10
Maximum Obtainable Value is 10
"""