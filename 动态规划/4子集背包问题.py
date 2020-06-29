# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 12:56:19 2020

@author: Dongzhixiao
给定一个数组，是否可以分割成两个元素和相等的数组？
"""

if __name__=='__main__':
    l = [1,5,11,5,1,1]
    assert(sum(l)%2==0)
    #第一步：定义dp数组——dp[i][j] = x 表示，对于前 i 个物品，
    #当前背包的容量为 j 时，若 x 为 true，则说明可以恰好将背包装满，
    #若 x 为 false，则说明不能恰好将背包装满。
    bagWeight = sum(l)/2
    M = len(l)+1 #一共有多少个物体
    N = int(bagWeight+1) #重量是多少，必须是能被2整除的整数！
    #我们想求的最终答案就是 dp[N][sum/2]
    #base case 就是 dp[..][0] = true 和 dp[0][..] = false
    #因为背包没有空间的时候，就相当于装满了，而当没有物品可选择的时候，肯定没办法装满背包
    dp = []
    for i in range(M):
        tem = [False for i in range(N)]
        tem[0] = True
        dp.append(tem)
    dp[0][0] = False
    for i in range(1,M):
        for j in range(1,N):
            if j - l[i-1]<0:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-l[i-1]]
    re = dp[M-1][N-1]                