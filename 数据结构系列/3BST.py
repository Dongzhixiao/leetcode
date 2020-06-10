# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 16:27:37 2020

@author: Dongzhixiao

二叉搜索树（Binary Search Tree，简称 BST）是一种很常用的的二叉树。
它的定义是：一个二叉树中，任意节点的值要大于等于左子树所有节点的值，
且要小于等于右边子树的所有节点的值。
"""

from utils import Node

#1. 这里有个坑，判断是否为有效BST
def isValidBST(node) -> bool:
    def isVBST(node,Min,Max):
        if node == None:
            return True
        if Min != None and Min >= node.val:
            return False
        if Max != None and Max <= node.val:
            return False
        #下面一句话的意思，如果没有返回：
        #该节点已经小于最大值了，所以左边节点更新最大值为该节点
        #该节点已经大于最小值了，所以右边节点更新最小值为该节点
        return isVBST(node.left,Min,node) and \
               isVBST(node.right,node,Max)
    return isValidBST(node,None,None)

#2. BST 中查找一个数是否存在
def isInBST(node,val):
    if node == None:
        return False
    if node.val == val:
        return True
    if node.val < val:
        return isInBST(node.right,val)
    if node.val > val:
        return isInBST(node.left,val)
    
#2.1 根据2得到BST的遍历框架
'''
void BST(TreeNode root, int target) {
    if (root.val == target)
        // 找到目标，做点什么
    if (root.val < target) 
        BST(root.right, target);
    if (root.val > target)
        BST(root.left, target);
}
'''

#3. 实践:在 BST 中插入一个数
## 一旦涉及“改”，函数就要返回 TreeNode 类型，并且对递归调用的返回值进行接收。
def insertValInBST(node,val):
    if node == None:
        return Node(val)
#    if node.val == val:   #一般不会插入已有的数据
#        return node
    if node.val > val:
        node.left = insertValInBST(node.left,val)
    if node.val < val:
        node.right = insertValInBST(node.right,val)
    return node

#4. 在 BST 中删除一个数
def deleteValInBST(node,val):  #假设有该值
    if node == None:
        return None
    if node.val == val:
        #进行删除
        if node.left == None and node.right == None:
            return None
        if node.left == None:
            return node.right
        if node.right == None:
            return node.left
        if node.left != None and node.right != None:  #这一行可以没有，为了理解加上
        #必须找到左子树中最大的那个节点，或者右子树中最小的那个节点来接替自己
        #找到右子树的最小节点
            minNode = getMin(node.right)
            #把 root 改成 minNode
            node.val = minNode.val
            #转而去删除 minNode
            node.right = deleteValInBST(node.right, minNode.val)
    if node.val > val:
        node.left = deleteValInBST(node.left,val)
    if node.val < val:
        node.right = deleteValInBST(node.right,val)
    return node























