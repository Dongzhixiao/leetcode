# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 22:24:22 2020

@author: Dongzhixiao

LRU( Least Recently Used) 缓存淘汰算法就是一种常用策略。
LRU 算法实际上是让你设计数据结构：首先要接收一个 capacity 参数作为缓存的最大容量，
然后实现两个 API，一个是 put(key, val) 方法存入键值对，
另一个是 get(key) 方法获取 key 对应的 val，如果 key 不存在则返回 -1。
注意：get 和 put 方法必须都是 O(1) 的时间复杂度
"""

# LRU 缓存算法的核心数据结构就是哈希链表，双向链表和哈希表的结合体，见图2.jpg

# 哈希表查找快，但是数据无固定顺序；链表有顺序之分，插入删除快，但是查找慢。
# 所以结合一下，形成一种新的数据结构：哈希链表。

#1. 构造链表的结点和双向链表
class node(object):
    def __init__(self,k,v):
        self.key = k
        self.value = v
        self.prev = None
        self.next = None

class doubleList(object):
    def __init__(self)