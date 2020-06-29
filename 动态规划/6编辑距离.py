# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 14:45:19 2020

@author: 34791
s1和s2两个字符串，计算s1到s2的转换的最少操作数
插入、删除、替换
"""

if __name__ == '__main__':
    s1 = 'rad'
    s2 = 'apple'
    #第一步：构造dp[i][j]，其中第i行第j列代表s1前i个字母变成s2所用的最少操作数
    M = len(s1)+1
    N = len(s2)+1
    dp = [[1 for j in range(N)] for i in range(M)]
    #dp[0][0] = 0  错误一：基础案例是1,N次增加、删除
    for i in range(M):
        dp[i][0] = i
    for j in range(N):
        dp[0][j] = j
    for i in range(1,M):
        for j in range(1,N):
            if s1[i-1] == s2[j-1]:
#                dp[i][j] = min(dp[i-1][j-1],dp[i-1][j]+1,dp[i][j-1]+1)
                dp[i][j] = dp[i-1][j-1]  #错误二：相等不用选择？
            else:
                dp[i][j] = min(dp[i-1][j-1]+1,dp[i-1][j]+1,dp[i][j-1]+1)
    re = dp[M-1][N-1]
    
#ooooooooo
#ooooooooo
#oooooooAB
#oooooooCX
#想象上图X结果在A、B位置做出选择，A:插入、B：删除、C：替换或者跳过
#之间的距离就是第i个物体的质量



