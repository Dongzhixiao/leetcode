# -*- coding: utf-8 -*-
"""
Created on Wed May 27 19:48:47 2020

@author: 34791
"""
s = "eleetminicoworoep"
# bit_mask由左至右对应 aeiou 5个元音字母的出现次数的奇偶性，
# 1代表某个字母出现奇数次，0代表出现偶数次
bit_mask = eval('0b00000')
# 下面一行，初始化状态集，一开始元音字母都是0次(都为偶数)，这种情况发生在-1位置，即0位置的左侧
# state_first_idx的含义为，某种状态(key)：第一次出现的位置(index)
state_first_idx = {eval('0b00000'): -1}
vowels = 'aeiou'
ans = 0
for i in range(len(s)):
    idx = vowels.find(s[i]) # str的find方法，找不到返回-1，找到返回元素在字符串中的index，将找到的结果放在idx中
    if idx > -1:  
        bit_mask ^= eval('0b10000') >> idx  # 找到idx后，就要将对应位置进行翻转(用异或实现)
                                            # eval('0b10000') >> idx，就是将找到的元音所对应的那位设为1，
                                            # 它再和原始的 bit_mask 异或就实现了将元音对应位置翻转
    if bit_mask not in state_first_idx:  # 如果当前状态没有出现，则将其记录
        state_first_idx[bit_mask] = i
    ans = max(ans, i - state_first_idx[bit_mask])  # 更新结果
