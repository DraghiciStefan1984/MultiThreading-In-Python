#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 13:38:52 2018

@author: user
"""

import threading

def add_nums(num1, num2):
    print(str(num1+num2))
   
# single thread
t=threading.Thread(target=add_nums, args=(8, 18))
t.start()

# multiple threads
for i in range(5):
    t=threading.Thread(target=add_nums, args=(8, 18))
    t.start()