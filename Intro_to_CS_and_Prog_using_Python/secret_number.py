#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 14:18:51 2019

@author: jds
"""

print('Please think of a number between 0 and 100!' )

low = 0.0
high = 100.0
ans = 0
result = ''

while result != 'c':
    ans = (high+low)//2.0
    result = input ('Is your secret number ' + str(ans) + "? \nEnter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if result == 'h':
        high = ans    
    elif result == 'l':
        low = ans
    elif  result == 'c':
        print ('Game over. Your secret number was:' + str(ans))
        break
    else:
        print ('Sorry, I did not understand your input.')
        continue
    
    
"""  
  Enter 'h' to indicate the guess is too high. 
    \nEnter 'l' to indicate the guess is too low. 
    \nEnter 'c' to indicate I guessed correctly.
    
    
    Sorry, I did not understand your input.
    
    Game over. Your secret number was:

        """
