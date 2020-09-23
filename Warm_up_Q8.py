#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 23:55:44 2020

@author: stevenyuan
"""

def fruit(x, y, op):
    if(op == '+'):
        return x + y
    elif(op == '*'):
        return x * y
    else:
        return 0
    
if __name__ == '__main__':
   print(fruit(1, 1, '+'))
   print(fruit(2, 2, '*'))
   print(fruit(1, 1, '=='))
   