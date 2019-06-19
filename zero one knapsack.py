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

"""
#Classic bottom up 0/1 knapsack
#Return the Dynamic Programming matrix
def compute_knapsack_matrix(items, max_weight):
    
#Fill with 0 dynamic programing matrix size: (#items x (max_weight + 1))
    T = [[0 for j in range(max_weight +1 )] for j in range(len(items))]
    
    #Loop through items 
    for i in range(len(items)):
        #record current item's weight and value
        wt = items[i][0]
        val = items[i][1]
        #compute current row in T
        for j in range(1, max_weight+1):
            #if current weight is admissible, update entry in T
            if wt <= j:
                diff = j - wt
                #special case for first row
                if i == 0:
                    T[i][j] = val
                elif i > 0:
                     T[i][j] = max(val + T[i-1][diff], T[i-1][j])
           #if current weight is not admissible, bring down above value
            elif wt > j and i > 0:
                T[i][j] = T[i-1][j]
    #return the matrix           
    return T


# Initialize items as list of lists [[weight, value], ... ,[weight, value], ... , ]
items = [[12, 4],[1, 2],[4, 10],[1, 1], [2, 2], [1, 5]]

#set knapsack max weight
max_weight = 15
               
# compute the dynamic programming matrix
matrix = compute_knapsack_matrix(items, max_weight)

#Dispaly Dynamic Programming matzix
def display_matrix(m):
    for row in m:
        print(row)  
#return the optimal value      
def get_optimal_value(m):
    rows = len(m) - 1 
    cols = len(m[0]) -1 
    return m[rows][cols]

# Test code
display_matrix(matrix)

print("optimal value:", get_optimal_value(matrix))

"""
sample output          
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4]
[0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 6, 6, 6]
[0, 2, 2, 2, 10, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]
[0, 2, 3, 3, 10, 12, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13]
[0, 2, 3, 4, 10, 12, 13, 14, 15, 15, 15, 15, 15, 15, 15, 15]
[0, 5, 7, 8, 10, 15, 17, 18, 19, 20, 20, 20, 20, 20, 20, 20]
20            
"""


