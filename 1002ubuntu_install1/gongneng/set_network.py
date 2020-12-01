import os


"""

sudo ifconfig eth0 192.168.2.1 netmask 255.255.255.0
将IP地址改为：192.168.2.1，子网掩码改为：255.255.255.0
sudo route add default gw 192.168.2.254         # 网关

Ubuntu IP设置DNS 修改/etc/resolv.conf 在其中加入nameserver DNS的地址1 和 nameserver DNS的地址2 完成。

sudo /etc/init.d/networking restart # 重启

"""


def run():
    # TODO  不知道离线能不能安装这个工具包了(不能！)
    # 参考: https://blog.csdn.net/davidhzq/article/details/102991577?depth_1-

    os.system('sudo apt install net-tools')

    os.system('sudo ifconfig eth0 192.168.1.39 netmask 255.255.255.0')

    os.system('sudo route add default gw 192.168.1.1')

    print("还需要自己去设置dns")
    os.system("sudo chmode 777 /etc/resolv.conf")
    os.system("sudo echo 'nameserver 192.168.1.1' >> /etc/resolv.conf")
    os.system("sudo echo 'nameserver 180.76.76.76'")
 
    os.system('sudo /etc/init.d/networking restart')


