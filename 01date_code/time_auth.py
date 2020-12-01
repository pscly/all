# coding: utf-8
# 作者:Pscly
# 创建日期: 2020年11月17日
# version: 1.0.1

'''
密码，日期中(日)的和
例如: 2020年4月12日  = 1+2 = 3   # 密码是3
4月06日 = 0+6 = 6   # 密码是6
输入密码:  01234  取 [1:3] 然后相加 (1+2+3)
也可以去修改这个东西

为啥没有用装饰器呢？
因为我认为用装饰器有点不对劲，这个东西只是在程序开始的时候使用以下， 如果是是用装饰器的话，不太好

'''

import datetime, time


def my_sum(date_1):
    '''
    判断进来的字符串是不是数字，如果不是，就返回none
    如果是数字，就会把每个字符相加 '23'  --> 5(2+3)
    :param riqi: 字符串，而且必须是数字
    :return:
    '''
    mms_l1 = []
    if date_1.isdigit():
        # 验证是不是数字
        for i in date_1:
            i = int(i)
            mms_l1.append(i)
        he = sum(mms_l1)    # sum将数字求和
        return he


def date_duibi(end_time_str = '2020-10-21'):
    '''

    :param end_time_str:  软件停止使用的日期(感觉似乎不是很准确啊)
    :return: 如果在使用的时间就会返回True, 否则就是False
    '''
    end_time = datetime.datetime.strptime(end_time_str, '%Y-%m-%d')
    d3 = time.strftime('%Y-%m-%d')  # 先得到时间，他会自动变成字符串
    now_time = datetime.datetime.strptime(d3, '%Y-%m-%d')  # 然后吧字符串变成时间  （当前时间）
    if now_time < end_time:
        return True     # 在激活时间以内


def jihuoma():
    print('软件有全新版本,请联系qq:550191537 or 微信:ps1cly 获取')
    jhm = input('你也可以输入激活码>>:').strip()
    if len(jhm) < 4: exit('激活码错误')

    # d3 = time.strftime('%m')     # 返回字符串，月份
    d3 = time.strftime('%d')     # 返回字符串，日份
    end_time2 = my_sum(d3)   # 将月份的数字相加(11月)-->2


    mms = jhm[1:4]      # 密码是取012345 的 123
    key1 = my_sum(mms)
    print(end_time2)
    if key1:    # 验证是不是数字，如果是就把结果输出
        if key1 == end_time2:   # 对比验证码
            run(1)
            pass
        else:
            print('验证码过期了')
            input('输入回车退出，')
            quit()
    else:
        print('激活码错误')


def run1(b, c=1, a=1):
    print(a)
    print(b)
    print(c)
    print('123运行了')


def run(def_1,*args,**kwargs):
    '''
    入口,当然
    '''

    if date_duibi():
        def_1(*args,**kwargs)

    else:
        def_1(*args,**kwargs)


if __name__ == '__main__':
    run(run1,12,a=11,c=15)


