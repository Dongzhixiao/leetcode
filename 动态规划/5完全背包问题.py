# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 14:37:46 2020

@author: 34791
"""

if __name__=='__main__':
    l = [2]
    amount=3
    #第一步：定义dp数组——dp[i][j],若只使用 coins 中的前 i 个硬币的面值，
    #若想凑出金额 j，有 dp[i][j] 种凑法。