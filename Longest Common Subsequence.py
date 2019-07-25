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


Longest Common Subsequence Problem
Example:
Let X be “XMJYAUZ” and  Y be “MZJAWXU”. The longest common subsequence between 
X and Y is “MJAU”, which has length 4.
"""
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


Longest Common Subsequence Problem
Example:
Let a be ['X','M','J','Y','A','U','Z'] and  b be ['M', 'Z', 'J', 'A', 'W', 'X', 'U']. The longest common subsequence between 
a and b is ['M', 'J', 'A', 'U'], which has length 4.
"""
"""
Adapted from https://www.youtube.com/watch?v=NnD96abizww&list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr&index=2
"""
def lcs2(a, b):
    #write your code here
    
    #compute lengths of the two sequences
    m = len(a);
    n = len(b);
    
    #initialize an empty (m+1)x(nx1) grid  with 0(s)
    grid = [[0]*(n+1) for i in range(m+1)]
    
    
    #Dynamic Programming 
    for i in range(1, m+1):
        for j in range(1, n+1):
            # Two cases 
            if (a[i-1] == b[j-1]):
                grid[i][j] = grid[i-1][j-1] +1
            else:
                grid[i][j] = max(grid[i][j-1],grid[i-1][j])
    return grid[m][n]

#**** Test Code ****

a = ['X','M','J','Y','A','U','Z']
b = ['M', 'Z', 'J', 'A', 'W', 'X', 'U']
print(lcs2(a, b))


x = [2, 7, 5]
y = [2, 5]
print(lcs2(x, y))


s = [2, 7, 8, 3]
t = [5, 2, 8, 7]
print(lcs2(s, t))


c = [7]
d = [1, 2, 3, 4]
print(lcs2(c, d))
"""
4
2
2
0
"""

