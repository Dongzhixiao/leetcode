# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 08:33:24 2020

@author: Dongzhixiao
"""

def zcdzzxl(l):
    #第一步：定义dp数组:dp[i]代表以l[0]~l[i]中以l[i]结尾的最长递增子序列的长度
    dp = [1 for i in range(len(l))]  #错误1：要全部初始为1，因为最少也是自己本身组成一个序列
    #第二步：计算dp数组
    for i in range(len(dp)):
        if i == 0:
            dp[i] = 1
            continue
        for j in range(i):
            if l[i]>l[j]:
                dp[i] = max(dp[j]+1,dp[i])
#            else:   #错误2：这个千万不能有，否则就不是以l[i]结尾的最长递增子序列了！
#                dp[i] = max(dp[j],dp[i])
    #第三步：得到结果
    res = max(dp)  
    return res
    
if __name__ == '__main__':
    l = [10,9,2,5,3,7,101,18,17,16,15,14,13,14,15]
#    l = [1,2,3,4,3,2,1]
    
    
    res = zcdzzxl(l)
    print(str(l)+'的最长递增子序列的长度是：'+str(res))
    