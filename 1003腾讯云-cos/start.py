#!/usr/bin/python3
# coding: utf-8
# 作者:Pscly
# 创建日期: 
# version: 
# 

# 1. 设置用户配置, 包括 secretId，secretKey 以及 Region
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import sys
import logging
import json

logging.basicConfig(level=logging.INFO, stream=sys.stdout)


secret_id = 'AAA'      # 替换为用户的 secretId
secret_key = 'BBB'      # 替换为用户的 secretKey
region = 'ap-chengdu'     # 替换为用户的 Region
token = None                # 使用临时密钥需要传入 Token，默认为空，可不填
scheme = 'https'            # 指定使用 http/https 协议来访问 COS，默认为 https，可不填
config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key, Token=token, Scheme=scheme)
# 2. 获取客户端对象
client = CosS3Client(config)
# 参照下文的描述。或者参照 Demo 程序，详见 https://github.com/tencentyun/cos-python-sdk-v5/blob/master/qcloud_cos/demo.py
response = client.list_buckets()

if __name__ == '__main__':
    print(response)

