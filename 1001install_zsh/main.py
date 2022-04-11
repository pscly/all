#!/usr/bin/python3
# coding: utf-8
# 作者:Pscly
# 创建日期: 
# version: 

import os
import time


sudo = 'sudo'

def huanyuan():
    now_time = time.strftime("%y-%m-%d--%S")  # 时间是 年-月-日--秒
    os.system(f'{sudo} cp /etc/apt/sources.list /etc/apt/sources.{now_time}.list')
    os.system(f'{sudo} cp ./lists/aliyun.list /etc/apt/sources.list')
    os.system(f'{sudo} apt-get update')
    

def install_git():
    os.system("f{sudo} apt install git")
    os.system("echo '\n\n\n\n\n\n\ngit安装完成\n\n\n\n\n\n\n'")

def install_zsh():
    os.system(f"{sudo} apt install zsh")
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
    os.system(f'{sudo} apt install fish')
    os.system('chsh -s $(which fish)')

def install_plugins():
    os.system('git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions')
    os.system('git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting')

    # os.system('plugins=(zsh-autosuggestions)')
    time.sleep(5)
    os.system('chsh -s $(which zsh)')
    print('请自己往 ~/.zshrc  plugins 中添加  zsh-autosuggestions,zsh-syntax-highlighting ')
    print('使用 vim ~/.zshrc')
    
def install_zsh_i():
    in1 =input("使用国内源输入1，国外源输入2\n:").strip
    install_url = ''
    if in1 == '1':
        install_url = 'https://gitee.com/mo2/zsh/raw/master/zsh.sh'
    else:
        install_url = 'git.io/zsh.sh'
    os.system(f'bash -c "$(wget -qO- {install_url})"')

def install_nvim():
    os.system(f'{sudo} apt install neovim')
    os.system(f'{sudo} apt install python3-pip')

    os.system("""sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs \
       https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'""")

    # 在用户目录下创建.config/nvim 目录
    os.system('mkdir -p ~/.config/nvim')
    
    os.system(f'cp {os.path.join(os.path.dirname(os.path.abspath(__file__)), "init.vim")} ~/.config/nvim/init.vim')

    os.system('nvim +PlugInstall +qall')


dakai = {
    '1': [huanyuan, '换源'],
    '2': [install_git, '安装git'],
    '3': [install_zsh, '安装zsh'],  
    '4': [install_fish, '安装fish'],
    '5': [install_plugins, '安装zsh插件(就一个小插件， 不如不装)'],
    '6': [install_zsh_i, '安装zsh插件(zsh-i),相当于是zsh整合包'],
    '7': [install_nvim, '安装nvim 和一堆插件'],
    'q': [exit, '退出'],
}

def dayin():
    for i in dakai:
        print(i,' \t'.expandtabs(6),dakai[i][1])

if __name__ == "__main__":
    import start_funcs as sf
    in1 = input('是否需要sudo Y/n:').strip()
    if in1.upper() == 'N':
        sudo = ''
        
    while 1:
        sf.runs(dakai)


