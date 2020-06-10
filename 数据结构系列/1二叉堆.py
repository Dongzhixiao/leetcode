# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 21:38:21 2020

@author: Dongzhixiao

二叉堆（Binary Heap）:其主要操作就两个，sink（下沉）和 swim（上浮），用以维护二叉堆的性质。
其主要应用有两个，首先是一种排序方法「堆排序」，
第二是一种很有用的数据结构「优先级队列」。
"""

'''
二叉堆其实就是一种特殊的二叉树（完全二叉树），只不过存储在数组里。
一般的链表二叉树，我们操作节点的指针，而在数组里，我们把数组索引作为指针
'''

#1. 索引，见图1.png。注意数组的第一个索引 0 空着不用

class BinaryHeap(object):
    def __init__(self):
        # 存储元素的数组
        self.pq = [None]
    
    #父节点的索引
    def parent(self,root:int) -> int:
        return root // 2  #错误2： python除法总是返回浮点！ 3.0+改了……
    # 左孩子的索引
    def left(self,root:int) -> int:
        return root * 2
    # 右孩子的索引
    def right(self,root:int) -> int:
        return root * 2 + 1

#注意：把 arr[1] 作为整棵树的根的话，每个节点的父节点和左右孩子的索引都可以通过简单的运算得到，
#这就是二叉堆设计的一个巧妙之处

#二叉堆还分为最大堆和最小堆。最大堆的性质是：每个节点都大于等于它的两个子节点。
#类似的，最小堆的性质是：每个节点都小于等于它的子节点

#对于一个最大堆，根据其性质，显然堆顶，也就是 arr[1] 一定是所有元素中最大的元素。
        
#2. 以最大堆为例子，实现优先级队列
#优先级队列这种数据结构有一个很有用的功能，你插入或者删除元素的时候，
#元素会自动排序，这底层的原理就是二叉堆的操作。
    # 返回当前队列中最大元素
    def MaxPQ(self):
        return self.pq[1]
    # 交换数组的两个元素
    def exch(self,i,j):
        tem = self.pq[i]
        self.pq[i] = self.pq[j]
        self.pq[j] = tem
    # pq[i] 是否比 pq[j] 小？
    def less(self,i,j) -> bool:
        return self.pq[i] - self.pq[j] < 0

#3.下面是核心函数
    # 上浮
    def swim(self,k):
         # 如果浮到堆顶，就不能再上浮了
        while k > 1 and self.less(self.parent(k), k):
        # 如果第 k 个元素比上层大
        # 将 k 换上去
            self.exch(self.parent(k), k)
            k = self.parent(k)
    # 下沉
    def down(self,k):
         # 如果沉到堆底，就沉不下去了
        while self.left(k) < len(self.pq)-1: #错误1：所有出现len的必须-1，因为0号位置空
            # 先假设左边节点较大
            biggerChild = self.left(k)
            # 如果右边节点存在且较大，则换最大孩子
            if self.right(k) < len(self.pq)-1 and self.less(biggerChild,self.right(k)):
                biggerChild = self.right(k)
            # k 比大的孩子还大，则不必下沉
            if self.less(biggerChild,k):
                break
            # 否则下沉并且继续循环
            self.exch(k,biggerChild)  
            k = biggerChild
                
#4. 下面是删除最大元素和插入一个元素
    def delMax(self):
        # 如果只剩下一个元素None，则没东西了返回
        if len(self.pq) == 1:
            print('已经空了，没东西了！')
            return None
        # 最大元素换到最后，然后删除
        maxVal = self.pq[1]
        self.exch(1,len(self.pq)-1)
        del self.pq[-1]
        # 让pq[1]下沉到正确位置
        self.down(1)
        return maxVal
    
    def insert(self,val):
        #先把元素加入到最后
        self.pq.append(val)
        # 然后上浮到正确位置
        self.swim(len(self.pq)-1)
        
if __name__ == '__main__':
    bt = BinaryHeap()
    bt.insert(1)
    bt.insert(3)        
    bt.insert(5)
    bt.insert(4)
#    bt.delMax()
        
        









