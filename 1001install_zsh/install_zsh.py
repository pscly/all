#!/usr/bin/python3
# coding: utf-8
# 作者:Pscly
# 创建日期: 
# version: 

import os
import time

def huanyuan():
    now_time = time.strftime("%y-%m-%d--%S")  # 时间是 年-月-日--秒
    os.system(f'sudo cp /etc/apt/sources.list /etc/apt/sources.{now_time}.list')
    os.system('sudo cp ./lists/aliyun.list /etc/apt/sources.list')
    os.system('sudo apt-get update')
    

def install_git():
    os.system("sudo apt install git")
    os.system("echo '\n\n\n\n\n\n\ngit安装完成\n\n\n\n\n\n\n'")

def install_zsh():
    os.system("sudo apt install zsh")


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




