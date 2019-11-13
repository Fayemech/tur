# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 21:10:50 2019

@author: ryu11
"""

import threading
import time

def threadJob():
    print('T1 start\n');
    for i in range(10):
        time.sleep(0.1);
    print('T1 finish\n')

def T2Job():
    print('T2 start\n');
    print('T2 finish\n');
    
def main():
    add_thread = threading.Thread(target = threadJob, name = 'T1');
    thread2 = threading.Thread(target = T2Job, name = 'T2');
    add_thread.start();
    thread2.start();
    thread2.join();
    add_thread.join();
    print('all done\n');
    
if __name__ == '__main__':
    main()