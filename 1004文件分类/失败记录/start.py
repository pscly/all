# coding: utf-8
# 作者:Pscly
# 创建日期: 
# 用意：项目主文件

'''
问题：
    第一行不能正确的对正
    15可以对上0   拷贝成功
    16就会对上1   整个文件夹就什么都不会拷贝了
    17又绘对上0   拷贝成功
    18就会对上1   整个文件夹就什么都不会拷贝了

'''

import os, shutil

from os import path

print('！ 居然完成了')
# FILE_PATH = input('请输入待处理的文件夹:')
# TO_PATH = input('请输入要放到的目的地>>:')
#
FILE_PATH = r'C:\Users\pscly\Desktop\tmp2\cs1'
TO_PATH = r'C:\Users\pscly\Desktop\tmp2\cs2'
# FILE_PATH = r'.'
# FILE_PATH = r'D:\下载\百度云\壁纸分享'
# pd = 0      # 用来进行判断进行了几次的目录
dir_deep = 2    # 这个用来控制文件夹的深度
path_name = ''  # 这个表示当前文件夹的名字

# # 方法1
# for root, dirs, files in os.walk(FILE_PATH):
#     print('----------------------------------')
#     print(root)     # 当前的相对目录
#     print(dirs)     # 这个目录下有那些文件夹
#     print(files)    # 这个目录下有哪些文件
#     if root == 'he':
#         print(0000)


# 方法2
def files_1(PATH_1):
    # 得到 文件的指令，让我们可以通过迭代来得到当前目录下面有什么东西
    # with os.scandir(FILE_PATH) as it1:
    #     # for entry in it1:
    #     return it1
    it1 = os.scandir(PATH_1)
    return it1

it1 = files_1(FILE_PATH)

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
    if not os.path.isdir(save_path):        # 查看上一级文件夹是否存在
        os.makedirs(save_path)

    shutil.copy2(from_path, os.path.join(save_path, save_file_name))        # 复制文件


def copy_file(from_file_path, to_file_path, file_name, path_name, dir_name):
    '''

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
    save_path_1 = os.path.join(to_file_path, '分类', path_name)     # 这个是保存的文件路径
    save_path_2 = os.path.join(to_file_path, '汇总')     # 这个是保存的文件路径
    print('-----',to_file_path, '分类', path_name)

    save_file(from_file_path, save_path_1, save_file_name)      # 保存到分类那边去
    save_file(from_file_path, save_path_2, path_name+save_file_name)      # 保存到汇总那边去



root_dir_name = ''

def for_all(it, file_info=None, type_1=None, pd=0, *args, **kwargs):
    # is_copy : 进行判断是否进行拷贝(移动)文件
    # pd 用来判断进入了几次目录
    global dir_deep, path_name, root_dir_name


    for all in it:
        print(f'我是{all.name}，我位于{all.path}, 现在pd是{pd}')
        if all.is_dir():
            if pd == 3:
                pd = 0
            pd += 1
            print('这个是文件夹', pd, all.name, '--', all.path)

            if pd == dir_deep-1:
                print('1111文件夹', pd, all.name, '--', all.path)
                root_dir_name = all.name     # 这个指的是几期几期，
                it2 = files_1(all.path)
                for_all(it2, pd=pd)
                continue
            if pd == dir_deep:
                print('2222文件夹', pd, all.name, '--', all.path)
                # 当目录进入到第二层(手机, 4k)
                # 保留当前目录的名字, 方便之后进行分类存放
                path_name_now = all.name    # 这个指的是类别(手机, 4k)
                dir_path = all.path    # 这个指的是详细位置

                it2 = files_1(all.path)
                file_info_1 = {'type_1': all.name, 'dir_name': root_dir_name, 'jiekou': all}
                for_all(it2, file_info_1, type_1=True, pd=pd)  # 进入特殊模式

                pd -= 1
                continue
                # file_info = {'from_dir_path': all.path, 'type_1': all.name, 'jiekou': all}
                # for_all(it2, file_info)  # 进入特殊模式

                # pd = 0


            it2 = files_1(all.path)
            for_all(it2, pd=pd)


        if all.is_file() and pd > dir_deep-1:
            print('这个是文件%s' %all.name)

            if type_1:

                file_info_2 = {'from_dir_path': all.path, 'type_1': all.name, 'jiekou': all}
                copy_file(all.path, TO_PATH, all.name, file_info['type_1'], file_info['dir_name'])
                # 文件目录(完整)， 目标文件目录(大致位置)， 文件名， 文件类别， 文件期数


if __name__ == '__main__':
    for_all(it1)

# for all in  it1:
#     if all.is_dir():
#         print('这个是文件夹')
#         print(all.name)
#         print(all.path)
#
#         it2 = files_1(all.path)
#         for all2 in it2:
#             if all2.is_dir():
#                 print('这个是文件夹----')
#                 print(all2.name)
#                 print(all2.path)
#
#                 if all2.name == 'h2':
#                     print('这里是h--=-=-=')
#
#     if all.is_file():
#         print('这个是文件')
#         print(all.name)
#         print(all.path)
