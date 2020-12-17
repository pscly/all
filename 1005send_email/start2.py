
import yagmail

yag = yagmail.SMTP('发送方邮箱账号', '发送方邮箱 密码/授权码', host='发送方的SMTP服务器，默认是谷歌的')

texts = ['这里是文本1111 ', '22222', '333333']   # 在发送邮件的时候每一个元素中间都会自动换行
files = [r'.\aaa.mp3']  # 要注意路径的问题啊

yag.send('550191537@qq.com', '主题1', texts, files)




