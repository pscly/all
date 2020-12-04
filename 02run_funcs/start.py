#!/usr/bin/python3
# coding: utf-8
# 作者:Pscly

from funcs_file import *  # 引入方法


def fun_func(func_id, funcs_):
    if func_id == 'q':
        quit("退出")
        return False
    if func_id not in funcs_:
        print('你输入有误')
        return False

    funcs_[func_id][0]()
    return True


def dayin(funcs):
    print("--------------------------------------------")
    for i in funcs:
        print(i, ' \t'.expandtabs(6), funcs[i][1])


def in_func_fun(funcs, out_1='请输入>>:'):
    in_1 = input(out_1).strip().lower()
    in_1_list = in_1.split(' ')
    if not len(in_1_list) == 1:
        for i in in_1_list:
            fun_func(i, funcs)

    else:
        fun_func(in_1, funcs)

def runs(funcs, out_1='请输入>>:'):
    while 1:
        dayin(funcs)
        in_func_fun(funcs, out_1)
        print('\n')


if __name__ == "__main__":
    funcs = {
        #    函数名    解释
        '1': [func1, '方法1'],
        '2': [func2, '方法2'],
        '3': [func3, '方法3'],
        '4': [func4, '方法4'],
        'q': [None, '退出'],
    }
    while 1:
        runs(funcs)


