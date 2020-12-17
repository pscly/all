# 介绍

通过python自动发送邮件

这个是为了弄一个自动发送电子邮件的东西， 需要安装  yagmail

> pip install yagmail
>
> 如果感觉安装太慢， 建议使用阿里源
>
> pip install yagmail  -i https://mirrors.aliyun.com/pypi/simple





## 初始化邮件，准备发送

```python
# 导入模块
import yagmail
```

yagmail.SMTP()		# 传入账号，密码(邮箱授权码也可以，具体的话，去百度 邮箱授权码(例如： qq邮箱授权码))



```python
yag = yagmail.SMTP('发送方邮箱账号', '发送方邮箱 密码/授权码', host='发送方的SMTP服务器，默认是谷歌的')
```



## 发送邮件

yag.send(目标邮箱, 邮件主题, 邮件正文, 邮件的附件)

其中， 目标邮箱， 邮件正文， 邮件附件， 都可以使用列表来套起来，

```python
yag.send('pscly@qq.com', '主题1', texts, files)
```



## 完整代码

```python
import yagmail

yag = yagmail.SMTP('发送方邮箱账号', '发送方邮箱 密码/授权码', host='发送方的SMTP服务器，默认是谷歌的')

texts = ['这里是文本1111 ', '22222', '333333']   # 在发送邮件的时候每一个元素中间都会自动换行
files = [r'.\aaa.mp3']  # 要注意路径的问题

yag.send('pscly@qq.com', '主题1', texts, files)
```