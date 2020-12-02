import json

with open('腾讯云配置.json', 'r', encoding='utf-8') as f:
    # text1 = f.read()
    # json.dump(d1, f)

    res = json.load(f)

COS_SECRETID = res.get("cos_secretid")
COS_SECRETKEY = res.get("cos_secretkey")

if __name__ == '__main__':
    print(COS_SECRETID)
    print(COS_SECRETKEY)
    print('over')
    # input()
