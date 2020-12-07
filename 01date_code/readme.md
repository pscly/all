# 简介

![](https://img.shields.io/badge/bulid-1.0.1-<COLOR>)

![](https://img.shields.io/badge/powered by-pscly-<COLOR>)

这个是 通过当前时间来判定使用时间， 或者是使用临时验证码来使用



## 使用方法

```python
import time_auth	# 导入文件
time_auth.run(func_1)	# func_1 是你自己需要加时间验证的功能，

# 如果你的函数需要传参，就自己在函数后面加参数就行了
time_auth.run(func_1, xxx, yyy=1)	# xxx是func_1的位置参数，yyy是func_1的关键字参数
```

 

## 1.0.1

第一个版本
