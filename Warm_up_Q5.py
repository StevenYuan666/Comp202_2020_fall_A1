#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 23:35:20 2020

@author: stevenyuan
"""
def greeting_v1(input_value):
    print('Hello ' + str(input_value))
    
def greeting_v2(input_value):
    print('Hello', end = ' ')
    print(str(input_value))
    
def greeting_v3(input_value):
    result = 'Hello ' + str(input_value)
    print(result)
    
if __name__ == '__main__':
    greeting_v1('World!')
    greeting_v2('World!')
    greeting_v3('World!')