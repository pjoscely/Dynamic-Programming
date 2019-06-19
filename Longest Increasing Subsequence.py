#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

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


Longest Increasing Subsequence problem
Given an array of numbers, find the length of the longest increasing subsequence 
in the array. The subsequence does not necessarily have to be contiguous.

For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], 
the longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15.
"""

#Function to return the max value of a list
def get_max(input_list):
    max = input_list[0]
    for i in range(1, len(input_list)):
        if input_list[i] > max:
            max = input_list[i]
        
    return max

# Returns the length of the longest increasing subsequence in the input list.
#Uses a bottom up Dynamic Programming algorithm
def LIS(input_list):
    #find length of input_list
    length = len(input_list)
    #Initialize working list
    L = [1]*length
    #L[i] = length of the longest inreasing subsequence that contains input_list[i]
    #Loop through L updating its entries
    for i in range(1,length):
        #key idea: use the definition of L to recursively build up its entries
        for j in range(0, i):
            if input_list[j] < input_list[i] and L[i] < 1 + L[j]:
                L[i] = 1 + L[j]
    return get_max(L)
                
print("*** Test Code ***")
            
input_list = [1]
print(LIS(input_list)) 

input_list = [2,1]
print(LIS(input_list)) 

input_list = [1,2]
print(LIS(input_list)) 

input_list = [1,2,2,3]
print(LIS(input_list)) 


input_list = [5,7,4,-3,9,1,10,4,5,8,9,3]
print(LIS(input_list)) 
           
input_list = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]  
print(LIS(input_list))         
""" 
Sample Output       
*** Test Code ***
1
1
2
3
6
6      
"""        
        
        
        
        
        
        
        