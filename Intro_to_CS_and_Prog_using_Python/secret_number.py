#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 14:18:51 2019

@author: jds
"""

x = int(input('Please think of a number between 0 and 100!' ))
epsilon = 0.01
low = 0.0
high = x
ans = (high+low)/2.0

while abs(ans**2 -x) >= epsilon:
    
    
    Enter 'h' to indicate the guess is too high. 
    \nEnter 'l' to indicate the guess is too low. 
    \nEnter 'c' to indicate I guessed correctly.
    
    
    Sorry, I did not understand your input.
    
    Game over. Your secret number was:
    
