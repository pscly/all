#!/usr/bin/python3
# coding: utf-8
# 作者:Pscly
# 创建日期: 
# version: 

def huanyuan():
    pass

def install_git():
    pass

def install_zsh():
    pass

def install_plugins():
    pass

def runs():
    pass

dakai = {
    '1': [huanyuan, '换源'],
    '2': [install_git, '安装git'],
    '3': [install_zsh, '安装zsh'],
    '4': [install_plugins, '安装zsh插件'],
    '5': [runs, '输入一堆，然后按顺序执行'],
    '6': [exit, '退出'],
}

def dayin():
    for i in dakai:
        print(i,' \t'.expandtabs(6),dakai[i][1])




