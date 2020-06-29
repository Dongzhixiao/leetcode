# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 14:53:14 2020

@author: 34791
最长公共子序列，例如：
输入: str1 = "abcde", str2 = "ace"
输出: 3
解释: 最长公共子序列是 "ace"，它的长度是 3
"""

str1 = "abfa"
str2 = "acfdasfa"
#构造dp[i][j]代表str1前i个字符和str2前j个字符的最长公共子序列长度
M = len(str1)+1
N = len(str2)+1
dp = [[0 for j in range(N)] for i in range(M)]
for i in range(1,M):
    for j in range(1,N):
        if str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            # 谁能让 lcs 最长，就听谁的
            dp[i][j] = max(dp[i][j-1],dp[i-1][j])

res = dp[M-1][N-1]

#如果 s1[i]==s2[j] ，那么这个字符一定在 lcs 中；
#否则的话， s1[i] 和 s2[j] 这两个字符至少
#有1个不在 lcs 中，需要丢弃1个

#如何得到lcs
