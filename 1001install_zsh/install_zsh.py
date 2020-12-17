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
    os.system('chsh -s $(which zsh)')

def install_oh_my_zsh():
    # https://github.com/pscly/all/blob/master/1001install_zsh/install.sh
    # https://gitee.com/pscly/all/raw/master/1001install_zsh/install.sh
    # https://tc.pscly.cn/install.sh
    # 
    url1 = 'https://tc.pscly.cn/install.sh'
    os.system(f'sh -c "$(curl -fsSL {url1})"')
    # os.system(f'sh -c "$(wget -qO- {url1})"')
    time.sleep(5)
    os.system('chsh -s $(which zsh)')
    
def install_fish():
    os.system('sudo apt install fish')
    os.system('chsh -s $(which fish)')

def install_plugins():
    os.system('git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions')
    # os.system('plugins=(zsh-autosuggestions)')
    time.sleep(5)
    os.system('chsh -s $(which zsh)')
    print('请自己往 ~/.zshrc  plugins 中添加  zsh-autosuggestions ')
    print('使用 vim ~/.zshrc')
    

dakai = {
    '1': [huanyuan, '换源'],
    '2': [install_git, '安装git'],
    '3': [install_zsh, '安装zsh'],
    '3': [install_fish, '安装fish'],
    '4': [install_plugins, '安装zsh插件(就一个小插件， 不如不装)'],
    '5': [exit, '退出'],
}

def dayin():
    for i in dakai:
        print(i,' \t'.expandtabs(6),dakai[i][1])

if __name__ == "__main__":
    import start_funcs as sf
    while 1:
        sf.runs(dakai)


