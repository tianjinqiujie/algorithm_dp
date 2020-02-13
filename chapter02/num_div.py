#-*- coding:utf-8 -*-
num = 7

datas = []
def search(rest):
    if rest <= 0:
        print(datas)
    else:
        for i in range(1,rest+1):
            # 1.设置现场
            datas.append(i)
            # 2.递归
            search(rest-i)
            # 3.恢复现场
            datas.pop()

search(num)