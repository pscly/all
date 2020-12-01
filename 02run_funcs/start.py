#!/usr/bin/python3
# coding: utf-8
# 作者:Pscly
# 创建日期: 
# version: 

from funcs_file import *
import time, os

def fun_func(func_id, funcs_):
    if func_id == 'q':
        return False
    if func_id not in funcs_:
        print('你输入有误')
        return False

    funcs_[in_1][0]()
    return True
    

def runs():
    pass

funcs = {
    '1': [func1, '方法1'],
    '2': [func2, '方法2'],
    '3': [func3, '方法3'],
    '4': [func4, '方法4'],
    # '5': [runs, '输入一堆，然后按顺序执行'], # 也许我该让他默认就这样?
    '5': [exit, '退出'],
}

def dayin(stat=''):
    print("--------------------------------------------")
    for i in funcs:
        print(i,' \t'.expandtabs(6),funcs[i][1])



if __name__ == "__main__":
    while 1:
        print('\n')
        dayin()
        in_1 = input("输入模式>>:").strip().lower()
        in_1_list = in_1.split(' ')
        if not len(in_1_list) == 1:
            for i in in_1_list:
                if not fun_func(i, funcs):
                    
                

        else:
            fun_func(in_1, funcs)





