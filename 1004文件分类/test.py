# # coding: utf-8
# # 作者:Pscly
# # 创建日期:
# # 用意：复习继承

import os

FILE_PATH = r'C:\Users\pscly\Desktop\tmp'

# print(os.listdir(FILE_PATH))
# print(os.scandir(FILE_PATH))

# with os.scandir(FILE_PATH) as it:

    # for entry in it:
    #     # print(entry)
    #     # if not entry.name.startswith('.') and entry.is_file():  # 如果不是.开头，而且是个文件
    #     #     print('这个是文件')
    #     #     print(entry.name)
    #     #     print(entry.path)
    #     #     continue
    #     # 在这里得到了 里面的文件夹名称和路径
    #     if entry.is_dir():
    #         print('这个是文件夹')
    #         print(entry.name)
    #         print(entry.path)
# #
#
# a = os.scandir(FILE_PATH)
# for i in a:
#     print(i.name)
#     a.close()
#

# def func(arg):
#     if arg == 1:
#         return 1
#     return func(arg - 1) - 1
#
# print(func(6))


# def f1(x):
#     if x == 10:
#         return x
#     f1(x+1)
#
# a = f1(1)
# print(a)



# s1 = 'abcdefg'
# i  = s1.find('d')
# if i == -1:
#     print('-1-1-1')
# print()
# print(type(s1.find('1')))


# a = 0
# b = 0
# def xx():
#     global a
#     global a, b
#     a += 11
#     b += 11
#     return 0
# xx()
# print(a)
# print(b)


# import os, shutil
#
# # from_path = r'C:\Users\pscly\Desktop\tmp2\c1'
# from_path = r'C:\Users\pscly\Desktop\tmp2\c1\cly02.txt'
# to_path = r'C:\Users\pscly\Desktop\tmp2\c2'
# shutil.copy2(from_path, to_path)


# a = os.path.isdir(r'c:/1cly')
# print(a)

# print(os.path.dirname(from_path))
# print(os.path.abspath(from_path))
# a  = os.path.join(from_path,'r','z','s','s.txt')
# print(a)
#
# os.makedirs(a)

def ru(i):
    print(i)
    i += 1


for i in range(5):
    if i == 3:
        ru(i)
    print(i)

