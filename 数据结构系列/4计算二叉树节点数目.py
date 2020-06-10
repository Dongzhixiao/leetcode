# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 23:01:11 2020

@author: Dongzhixiao
"""

from utils import Node

a = Node(1)

#1. 普通二叉树
def countNormalNodes(node):
    if node == None:
        return 0
    return 1+countNormalNodes(node.left) + countNormalNodes(node.right)

#2. 满二叉树
def countFullNodes(node):
    height = 0
    while node != None:
        node = node.left
        height += 1
    return 2**height + 1

#3. 完全二叉树
## 一棵完全二叉树的两棵子树，至少有一棵是满二叉树
## 算法的递归深度就是树的高度 O(logN)，每次递归所花费的时间就是 while 循环，
## 需要 O(logN)，所以总体的时间复杂度是 O(logN*logN)
def countCompleteNodes(node):
    lh = 0
    rh = 0
    while node != None:
        node = node.left
        lh += 1
    while node != None:
        node = node.right
        rh += 1
    if lh == rh:
        return 2**lh + 1
    else:
        return 1 + countCompleteNodes(node.left) + countCompleteNodes(node.right)
        
        
        
        
        
        
        
        
        