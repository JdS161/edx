#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 11:45:49 2019

@author: jds
"""

"""Task_1
s = str("azcbobobegghakl")
numVowels = 0

for char in s:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
       numVowels +=1
         
    
print ('Number of vowels: ' + str(numVowels))
"""

"""Task_2
s = str("azcbobobobegghbobakl")
count =0

numBob = 0

for i in range(len(s)):
    if s[i:i+3] == 'bob':
       numBob +=1
         
         
    
print ('Number of times bob occurs is: ' + str(numBob))   
"""


"""Task_3
s = "abcdefghijk"
temp = ''
ans = ''
for i in range(len(s)):
         if s[i] <= s[i+1:len(s)]:
             temp += s[i]
         else:
             temp += s[i]                         
             if len(temp) > len(ans):
                 ans = temp            
                 temp = ''
             else:
                 temp = ''
print ('Longest substring in alphabetical order is:' + ans)"""