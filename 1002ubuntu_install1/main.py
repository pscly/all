#!/usr/bin/python3
# coding:utf-8

# version:1.1.0
# 修复了一些问题（什么问题？ 我也忘了   哈哈哈哈哈）

import os

os.system('sudo timedatectl set-timezone Asia/Shanghai')
os.system("echo '时间设置完成'")


def set_network():
    """
    更改网络设置
    """
    from gongneng import set_network
    
    set_network.run()


def update_apt():
    """  将apt进行换个源  """
    from gongneng import func_1
    func_1.huanyuan()   # 换源


def install_git():
    ''' 
    并且安装git
    '''
    os.system("sudo apt install git")
    os.system("echo '\n\n\n\n\n\n\ngit安装完成\n\n\n\n\n\n\n'")


def install_ssr1():
    """
    安装ssr
    """
    from ssr_2 import ssr2
    ssr2.install_ssr()
    

def install_pkgs():
    '''
    安装离线包 chrome 和 code
    '''

    os.system("sudo dpkg -i ./pkgs/code_1.51.1-1605051630_amd64.deb")
    os.system("sudo dpkg -i ./pkgs/google-chrome-stable_current_amd64.deb ")
    os.system("echo '离线包安装完成'")


def install_lantern():
    ''' 安装蓝灯 '''
    # os.system('sudo dpkg -i ./pkgs/lantern-installer-64-bit.deb')
    from ssr_2 import ssr2
    ssr2.install_ssr()



def all_1():
    """
    全部功能都走一遍，按照顺序
    """
    pass


funcs = {
    '1': [set_network, set_network.__doc__.strip()],
    '2': [update_apt, update_apt.__doc__.strip()],
    '3': [install_git, install_git.__doc__.strip()],
    '4': [install_ssr1, install_ssr1.__doc__.strip()],
    '5': [install_pkgs, install_pkgs.__doc__.strip()],
    # '6': [update_apt, update_apt.__doc__.strip()],
    # '6': [install_lantern, install_lantern.__doc__.strip()],
    '7': [all_1, all_1.__doc__.strip()]
}

def all_1():
    for i in funcs:
        if (i == '1') or (i == '7'):
            # 就别再去设置网络了, 和再跑一次自己了
            continue
        
        funcs[i][0]()


def daying():
    print('''
    ! 千万注意， 如果要使用ssr那就得先安装ssr
    否则后面在用的时候，apt就会出现谜一样的问题
    (也可以去使用lantern)

    ''')
    print('默认会将时间地区改变')
    print('=====================================================')
    print('退出请输入q')
    for i in funcs:
        print(f'{i}\t{funcs[i][1]}')




while 1:
    print('\n')
    daying()
    in1 = input("输入模式>>:").strip().lower()
    if in1 == 'q':
        break
    if in1 not in funcs:
        print('你输入有误')
        continue
    
    funcs[in1][0]()
    


print('==OVER==')

