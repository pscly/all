# coding: utf-8
# 作者:Pscly
# 创建日期:
# 用意：

import yagmail

# yag = yagmail.SMTP('psclyyuan@gmail.com', 'g*** **** **** ****')
yag = yagmail.SMTP('pscly1@163.com', 'UXQSTCRIEKULJEDL', host='smtp.163.com')    # 更改为网易邮箱



# yag.send()


# yag = yagmail.SMTP()
texts = ['这里是文本1111 ', '22222', '333333']
# files = [r'.\aaa.mp3']

# yag.send('pscly@qq.com', '主题1', {'a1':'texts', 'a2':'texts1'})
yag.send('pscly@qq.com', '主题1', ('a1','texts',))

for i in {'texts','texts1'}:
    print(i)
