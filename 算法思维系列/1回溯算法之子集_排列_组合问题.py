# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 10:42:34 2020

@author: 34791
"""


#回溯算法之排列问题
s = '喵中之皇'
res = []
def A(s):
    res = []
    def all_rest(a,b):
        if b == '':
            res.append(a)
            return
        for i in b:
            a+=i
            all_rest(a,b.replace(i,'',1))
            a = a[:-1]
    all_rest('',s)
    return res

t = A(s)
print(t)