# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 22:20:44 2020

@author: 34791
你和你的朋友面前有一排石头堆，用一个数组 piles 表示，piles[i] 表示第 i 堆石子有多少个。
你们轮流拿石头，一次拿一堆，但是只能拿走最左边或者最右边的石头堆。
所有石头被拿完后，谁拥有的石头多，谁获胜。
"""
#注意：定义dp表
#dp[i][j].fir 表示，对于 piles[i...j] 这部分石头堆，先手能获得的最高分数。
#dp[i][j].sec 表示，对于 piles[i...j] 这部分石头堆，后手能获得的最高分数。
#
#举例理解一下，假设 piles = [3, 9, 1, 2]，索引从 0 开始
#dp[0][1].fir = 9 意味着：面对石头堆 [3, 9]，先手最终能够获得 9 分。
#dp[1][3].sec = 2 意味着：面对石头堆 [9, 1, 2]，后手最终能够获得 2 分。

class DPunit(object):
    def __init__(self,fir=0,sec=0):
        self.fir = fir
        self.sec = sec

piles = [3,9,1,2]

#写状态转移方程很简单，首先要找到所有「状态」和每个状态可以做的「选择」，然后择优。
#根据前面对 dp 数组的定义，状态显然有三个：开始的索引 i，结束的索引 j，当前轮到的人。

# 第一步：初始化dp，对角线上面初始化
n = len(piles)
dp = [[None for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(i,n):
        if i == j:
            dp[i][j] = DPunit(piles[i],0) #基本案例，在斜对角上
        else:
            dp[i][j] = DPunit()
for j in range(1,n):
    for i in range(n-j):
#        print(i,i+j)
        if dp[i+1][i+j].sec+piles[i] > dp[i][i+j-1].sec+piles[i+j]: #选择左边
            dp[i][i+j].fir = dp[i+1][i+j].sec+piles[i]
            dp[i][i+j].sec = dp[i+1][i+j].fir
        else: #选择右边
            dp[i][i+j].fir = dp[i][i+j-1].sec+piles[i+j]
            dp[i][i+j].sec = dp[i][i+j-1].fir
res = dp[0][n-1]
print(res.fir,res.sec)
    
    
    
    
    
    
    
    
    
    
    