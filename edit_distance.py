# Uses python3

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
Edit Distance

****Problem Introduction****

The edit distance between two strings is the minimum number of 
operations (insertions, deletions, and substitutions of symbols) 
to transform one string into another. It is a measure of 
similarity of two strings. Edit distance has applications, 
for example, in computational biology, natural language processing, and spell checking. 
Your goal in this problem is to compute the edit distance between two strings.

Problem Description

Task. The goal of this problem is to implement the algorithm for computing the 
edit distance between two strings.
Input Format. Each of the two lines of the input contains a string 
consisting of lower case latin letters. 
Constraints. The length of both strings is at least 1 and at most 100.
Output Format. Output the edit distance between the given two strings.
"""


def edit_distance(s, t):
    
    #compute lengths of the two strings s,t
    m = len(s);
    n = len(t);
    
    #initialize an empty (m+1)x(nx1) grid  with 0(s)
    grid = [[0]*(n+1) for i in range(m+1)]
    
    #Fill first column 
    for i in range(m+1):
        grid[i][0] = i
        
     #Fill first row 
    for j in range(n+1):
        grid[0][j] = j
    
    #Dynamic Programming 
    for i in range(1, m+1):
        for j in range(1, n+1):
            # Two cases 
            if (s[i-1] == t[j-1]):
                grid[i][j] = grid[i-1][j-1]
            else:
                grid[i][j] = 1 + min(grid[i][j-1],grid[i-1][j],grid[i-1][j-1])
    return grid[m][n]
    
    
"""
For submission to an online grader
if __name__ == "__main__":
    print(edit_distance(input(), input()))
"""


print(edit_distance("distance", "editing"))
#5
print(edit_distance("random words typed here", "more random typed over here"))
#5
