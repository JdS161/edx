#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 15:11:57 2019

@author: jds
"""
#answer - beggh


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
print ('Longest substring in alphabetical order is:' + ans)

                    


