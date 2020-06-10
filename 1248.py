# -*- coding: utf-8 -*-
"""
Created on Wed May 27 16:12:32 2020

@author: 34791

给你一个整数数组 nums 和一个整数 k。

如果某个 连续 子数组中恰好有 k 个奇数数字，我们就认为这个子数组是「优美子数组」。

请返回这个数组中「优美子数组」的数目。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-number-of-nice-subarrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from collections import defaultdict
def numberOfSubarrays(nums, k):
    res = 0
    pre_oodnums_d = defaultdict(int)
    pre_oodnums_d[0] = 1 # 给定一个初始状态，代表0个奇数的情况出现了1次!这个别忘了！
    oddnums = 0  # 到当前位置有几个奇数
    for num in nums:
        if num % 2 != 0:
            oddnums += 1
        if oddnums - k in pre_oodnums_d:
            res += pre_oodnums_d[oddnums-k]
        pre_oodnums_d[oddnums] += 1
    return res