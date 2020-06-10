# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 06:58:59 2020

@author: Dongzhixiao
"""

class Node(object):
    def __init__(self,val,left=None,right=None): #节点必须有数值，可以没有子节点
        self.val = val
        self.left = left
        self.right = right