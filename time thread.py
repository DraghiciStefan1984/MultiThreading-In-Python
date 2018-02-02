#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 13:38:52 2018

@author: user
"""

import threading
import time

def timer():
    print(threading.currentThread().getName(), 'Start')
    time.sleep(2)
    print(threading.currentThread().getName(), 'End')
   
# single thread
t=threading.Thread(target=timer)
t.start()
