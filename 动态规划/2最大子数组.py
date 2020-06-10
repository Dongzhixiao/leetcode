# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 09:45:58 2020

@author: 34791
"""
import copy

def zdzsz(l):
    pass

if __name__ == '__main__':
    l = [-2,1,-3,4,-1,2,1,-5,4]
    #第一步：定义dp数组——dp[i]即代表以i为结尾的最大和
    dp = copy.copy(l)  #极端情况下本身求个和
    #第二步：遍历状态，做出选择
    for i in range(1,len(dp)):
        dp[i] = max(dp[i-1]+dp[i],dp[i])
    res = max(dp)
    print(str(res))
    