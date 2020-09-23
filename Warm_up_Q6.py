#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 23:39:39 2020

@author: stevenyuan
"""

def display_two_v1():
    print('  22 ')
    print('2   2')
    print('   2 ')
    print(' 2   ')
    print('22222')
    
def display_two_v2():
    print(2 * ' ' + 2 * '2')
    print('2' + 3 * ' ' + '2')
    print(3 * ' ' + '2')
    print(' 2')
    print(5 * '2')
    
def display_twenty():
    print('  22        000   ')
    print('2   2      0   0  ')
    print('   2      0     0 ')
    print(' 2         0   0  ')
    print('22222       000   ')
    
if __name__ == '__main__':
    display_two_v1()
    display_two_v2()
    display_twenty()