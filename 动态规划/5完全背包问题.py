# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 14:37:46 2020

@author: 34791
"""

if __name__=='__main__':
    l = [1,2,5]
    amount=5
    #第一步：定义dp数组——dp[i][j],若只使用 coins 中的前 i 个硬币的面值
    #若想凑出金额 j，有 dp[i][j] 种凑法。
    M = amount+1
    N = len(l)+1
    dp = [[0 for j in range(M)] for i in range(N)]
    for i in range(1,N):
        for j in range(1,M):
            dp[i][j] = dp[i-1][j]
            # 如果后面使用dp[i][j-l[i-1]]，就不用下面的while这么复杂了
            n = 1
            while j-n*l[i-1] > 0:
                dp[i][j] += dp[i-1][j-n*l[i-1]]
                n += 1
            if j-n*l[i-1] == 0:  
                dp[i][j] += 1   #完全等于零说明完全用该硬币的这种方法
    re = dp[N-1][M-1]