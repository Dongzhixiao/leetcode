# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 12:56:19 2020

@author: Dongzhixiao
"""

if __name__=='__main__':
    l = [1,5,11,5]
    #第一步：定义dp数组——dp[i][j] = x 表示，对于前 i 个物品，
    #当前背包的容量为 j 时，若 x 为 true，则说明可以恰好将背包装满，
    #若 x 为 false，则说明不能恰好将背包装满。
    