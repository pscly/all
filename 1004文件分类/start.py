# coding: utf-8
# 作者:Pscly
# 创建日期: 
# 用意：项目主文件

import os, shutil

from os import path

'''
！ 居然完成了
我是真的真的真的天秀！！！！
虽然有点自大，但是真的真的真的，心情舒畅！！！！！
要不是因为是晚上(2020年7月21日22点30分)，我不敢拍掌拍大声，不然我估摸着我能手都麻！！！
00点12分  BUG修复完毕
'''
print('这个是我用来筛选壁纸的工具:  qq:550191537')

# FILE_PATH = r'C:\Users\pscly\Desktop\tmp2\cs1'
# TO_PATH = r'C:\Users\pscly\Desktop\tmp2\cs2'
# FILE_PATH = r'.'
# FILE_PATH = r'D:\下载\百度云\壁纸分享'
# pd = 0      # 用来进行判断进行了几次的目录

dir_deep = 2  # 这个用来控制文件夹的深度
path_name = ''  # 这个表示当前文件夹的名字


# 方法2
def files_1(PATH_1):
    # 得到 文件的指令，让我们可以通过迭代来得到当前目录下面有什么东西
    # with os.scandir(FILE_PATH) as it1:
    #     # for entry in it1:
    #     return it1
    it1 = os.scandir(PATH_1)
    return it1


def my_1(s1, d1):
    '''
    这个是自定义功能函数，要实现的功能都放在这个里面
    我现在打算放个跳过第一层的功能（每周精选壁纸分享）作为关键字
    :param s1:  放入字符
    :param d1:  放入字典，字典里面放关键字,  或者直接放入关键字也可以
    :return:
    '''
    if isinstance(d1, dict):
        for i in d1:
            if s1.find(i) != -1:
                # 好了，匹配，跳过吧，这里是上级目录
                return True
    if isinstance(d1, str):
        if s1.find(d1) != -1:
            # 匹配，跳过吧，
            return True


def save_file(from_path, save_path, save_file_name):
    '''
    执行最终的保存文件 并且验证文件夹是否存在
    :param save_path: 要保存到的文件夹位置
    :param save_file_name: 文件名
    :return:
    '''
    if not os.path.isdir(save_path):  # 查看上一级文件夹是否存在
        os.makedirs(save_path)
    
    shutil.copy2(from_path, os.path.join(save_path, save_file_name))  # 复制文件


def copy_file(from_file_path, to_file_path, file_name, path_name, dir_name):
    '''
    进行保存(复制前的最后操作)
    :param from_file_path:  文件原始目录(文件从哪来)(完整)
    :param to_file_path:  放目标目录, 这个最好还是让用户输入
    :param file_name: 原来的文件名字
    :param path_name:  文件类别,(类别)(手机, 4k)
    :param dir_name:  文件名的上一级 (几期)
    :return:
    '''
    # now_file_path = r'C:\Users\pscly\Desktop\tmp2\c1\cly02.txt'
    # to_file_path = r'C:\Users\pscly\Desktop\tmp2\c2'
    # file_name = '01.jpg'
    # path_name = '4k'
    # dir_name = '1期'

    # save_file_name = os.path.join(path_name, dir_name, file_name)        # 这个是文件的名字
    save_file_name = dir_name + file_name  # 这个是文件的名字
    save_path_1 = os.path.join(to_file_path, '分类', path_name)  # 这个是保存的文件路径1
    save_path_2 = os.path.join(to_file_path, '汇总')  # 这个是保存的文件路径2

    # 让专门保存(复制)的去保存(复制)
    save_file(from_file_path, save_path_1, save_file_name)  # 保存到分类那边去
    save_file(from_file_path, save_path_2, path_name + save_file_name)  # 保存到汇总那边去


root_dir_name = ''


def for_all(it, file_info=None, type_1=None, pd=0):
    # it : 这里的it是应该是it2
    # type_1 : 判断是不是特殊模式
    # pd 用来判断进入了几次目录
    global dir_deep, path_name

    for all in it:
        print(f'我是{all.name}，我位于{all.path}, 现在pd是{pd}, 我上面是{root_dir_name}, ')
        if all.is_dir():
            pd += 1

            if pd == dir_deep:  # 如果目录深度到了
                it3 = files_1(all.path)
                file_info_1 = {'type_1': all.name, 'dir_name': root_dir_name, 'jiekou': all}
                for_all(it3, file_info_1, type_1=True, pd=pd)  # 进入特殊模式

                pd -= 1
                continue

            # 目录深度还没到的情况
            it3 = files_1(all.path)
            for_all(it3, pd=pd)

        #TODO 如果要限制深度
        if all.is_file() and (pd == dir_deep):
            print('这个是文件%s' % all.name)
            if type_1:
                copy_file(all.path, TO_PATH, all.name, file_info['type_1'], file_info['dir_name'])
                # 文件目录(完整)， 目标文件目录(大致位置)， 文件名， 文件类别， 文件期数


def run(it):
    # is_copy : 进行判断是否进行拷贝(移动)文件
    # pd 用来判断当前进入了几次目录
    global dir_deep, path_name, root_dir_name
    for all in it:
        pd = 0  # pd 用来判断当前进入了几次目录

        root_dir_name = all.name  # 如果他是一个文件， 就会变成文件名， 但是如果是文件，就不会走下面的东西了
        if all.is_dir():
            pd += 1

            if pd == dir_deep:
                it2 = files_1(all.path)
                file_info_1 = {'type_1': all.name, 'dir_name': root_dir_name, 'jiekou': all}
                for_all(it2, file_info_1, pd=pd)

                pd -= 1
                continue

            it2 = files_1(all.path)
            for_all(it2, pd=pd)


if __name__ == '__main__':
    dir_deep = 2  # 控制文件夹的深度(根目录算是0)

    FILE_PATH = input('请输入待处理的文件夹:').strip(' ')
    TO_PATH = input('请输入要放到的目的地>>:').strip(' ')
    it1 = files_1(FILE_PATH)

    run(it1)

    input('完毕，回车键退出')
