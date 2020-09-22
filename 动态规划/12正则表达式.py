# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 08:47:26 2020

@author: 34791
实现正则表达式的*和.这两种匹配
输入：text,pattern
输出：是否匹配
"""
#暴力递归
def isMatch(text,pattern):
    #基本情况
    if text == '':
        if pattern=='':
            return True
        else:
            return False
    elif pattern == '':
        return False
    preMatch = pattern[0] in [text[0],'.']
    if len(pattern) > 1 and pattern[1] == '*':
        #匹配字符0次，然后跳过该字符和* or preMatch匹配后跳过该字符
        return isMatch(text,pattern[2:]) or (preMatch and isMatch(text[1:],pattern))
    else:
        return preMatch and isMatch(text[1:],pattern[1:])

test = isMatch('abbbbsssf','ab*s*.')