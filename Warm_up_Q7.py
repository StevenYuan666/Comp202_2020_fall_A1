#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 23:51:37 2020

@author: stevenyuan
"""

def fruit(x, y, z):
    condition = z == 3 or z == x + y
    return condition

if __name__ == '__main__':
    print(fruit(1,1,3))
    print(fruit(1,3,4))
    print(fruit(1,1,1))
    