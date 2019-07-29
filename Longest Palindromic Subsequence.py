#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 20:27:14 2019

@author: joscelynec

Given a sequence, find the length of the longest palindromic subsequence in it.

longest-palindromic-subsequence. As an example, if the given sequence is “BBABCBCAB”, 
then the output should be 7 as “BABCBAB” is the longest palindromic subseuqnce in it. 
“BBBBB” and “BBCBB” are also palindromic subsequences of the given sequence, but not the longest ones.

The naive solution for this problem is to generate all subsequences of the given sequence and 
find the longest palindromic subsequence. This solution is exponential in term of time complexity. 
Let us see how this problem possesses both important properties of a Dynamic Programming (DP) Problem 
and can efficiently solved using Dynamic Programming.

https://youtu.be/_nCsPn7_OgI
https://www.geeksforgeeks.org/longest-palindromic-subsequence-dp-12/

"""
#Dynamic Program
def LongestPalindromicSubsequence (lst):
    length = len(lst)
    #Intialize a lengthxlength grid of -1
    grid = [[-1]*(length) for i in range(length)]
    #set the diagonal to 1
    for i in range(length):
        grid[i][i] = 1
    
    for l in range(2, length+1):
        for i in range(0, length - l +1):
            j = i + l - 1
            if(l == 2 and lst[i] == lst[j]):
                grid[i][j] = 2;
            elif(lst[i] == lst[j]):
                grid[i][j] = grid[i + 1][j-1] + 2
            else:
                grid[i][j] = max(grid[i + 1][j], grid[i][j - 1])
                
    return grid[0][length-1]

#Naive Recursive Solution
    
def calculateRecursive(lst, start, length):
    if length <= 1:
        return length
    if(lst[start] == lst[start+length-1]):
        return 2 + calculateRecursive(lst,start+1,length-2)
    else:
        return max(calculateRecursive(lst, start+1, length-1), calculateRecursive(lst, start, length-1))
   
l = []
for item in "BBABCBCAB":
    l.append(item)

print(l)
print(LongestPalindromicSubsequence (l))
print(calculateRecursive (l, 0, len(l)))
"""
['B', 'B', 'A', 'B', 'C', 'B', 'C', 'A', 'B']
7
7
"""