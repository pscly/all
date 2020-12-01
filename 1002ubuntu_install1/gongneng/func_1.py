import os
import time

def huanyuan():
    now_time = time.strftime("%y-%m-%d--%S")  # 时间是 年-月-日--秒
    os.system(f'sudo cp /etc/apt/sources.list /etc/apt/sources.{now_time}.list')
    os.system('sudo cp ./lists/aliyun.list /etc/apt/sources.list')
    os.system('sudo apt-get update')
    # os.system('sudo apt install python3-pip')

if __name__ == "__main__":
    print()

