# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 10:11:07 2020

@author: dongzhixiao
问题描述：
给你一个可装载重量为 W 的背包和 N 个物品，每个物品有重量和价值两个属性。
其中第 i 个物品的重量为 wt[i]，价值为 val[i]，
现在让你用这个背包装物品，最多能装的价值是多少？
"""

if __name__ == '__main__':
    N=3
    W=20
    wt=[2,1,3]
    val=[4,2,3]
    #第一步定义dp数组——dp[i][w]代表可装载w的背包在前i个物品中选择时，能够装的最大价值
    dp = [[0 for j in range(W+1)] for i in range(N+1)]
    
    for i in range(1,N+1):
        for w in range(1,W+1):   #w代表重量
            if w-wt[i-1] < 0:   
    #错误一：忘记增加这句话，必须保证处理了w - wt[i-1]可能小于0导致数组索引越界的问题
                dp[i][w] = dp[i-1][w]
            else:
    #注意理解dp[i-1][w-wt[i-1]]+val[i-1]：在装第i个物品前提下，背包能装的最大价值是多少？
    #显然，寻找剩余重量w-wt[i-1]限制下能装的最大价值，加上第i个物品的价值val[i-1]即为答案。
                dp[i][w] = max(dp[i-1][w],dp[i-1][w-wt[i-1]]+val[i-1])
    res = dp[N][W]
    print(str(res))
    
    #ooooooooo
    #ooooooooo
    #oooooAooB
    #ooooooooX
    #想象上图X结果在A、B位置做出选择，AB之间的距离就是第i个物体的质量