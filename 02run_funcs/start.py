#!/usr/bin/python3
# coding: utf-8
# 作者:Pscly
# 创建日期: 
# version: 

from funcs import *

def runs():
    pass

dakai = {
    '1': [func1, '方法1'],
    '2': [func2, '方法2'],
    '3': [func3, '方法3'],
    '4': [func4, '方法4'],
    # '5': [runs, '输入一堆，然后按顺序执行'], # 也许我该让他默认就这样?
    '5': [exit, '退出'],
}

def dayin(stat=''):
    print()
    for i in dakai:
        print(i,' \t'.expandtabs(6),dakai[i][1])



if __name__ == "__main__":
    dayin()
    in_1 = input('请输入功能>>>:')




