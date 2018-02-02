#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 13:31:32 2018

@author: user
"""

import threading as T

def hello():
    print("Hello!")

# single thread   
thread=T.Thread(target=hello)
thread.start()

# multiple threads
threads=[]
for i in range(5):
    t=T.Thread(target=hello)
    threads.append(t)
    t.start()