# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 21:31:55 2019

@author: ryu11
"""

import threading
from queue import Queue

def job(l, q):
    for i in range(len(l)):
        l[i] = l[i] ** 2;
    q.put(l);

def multithread():
    q = Queue();
    threads = [];
    data = [[1,2,3],[3,4,5],[4,4,4],[5,5,5]];
    for i in range(4):
        t = threading.Thread(target = job, args = (data[i], q));
        t.start();
        threads.append(t);
    for thread in threads:
        thread.join();
    res = [];
    for _ in range(4):
        res.append(q.get());
    print(res);
    
if __name__ == '__main__':
    multithread();