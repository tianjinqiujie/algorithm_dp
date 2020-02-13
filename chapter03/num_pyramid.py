#-*- coding:utf-8 -*-
pyramid = [
    [13],
    [11,8],
    [12,7,26],
    [6,14,15,8],
    [12,17,13,24,11]
]
datas = [13]
total_path = []
def search(depth,x,y):
    if depth == len(pyramid):
        total_path.append(datas[:])
        # print(total_path)
    else:
        # 1.选择下方的值
        # 1.设置现场
        datas.append(pyramid[x+1][y])
        # 2.递归
        search(depth+1,x+1,y)
        # 3.恢复现场
        datas.pop()

        # 1.选择右下方的值
        # 1.设置现场
        datas.append(pyramid[x+1][y+1])
        # 2.递归
        search(depth+1,x+1,y+1)
        # 3.恢复现场
        datas.pop()

if __name__ == "__main__":
    search(1,0,0)
    max = 0
    max_pos = 0
    for index,data in enumerate(total_path):
        if sum(data) > max:
            max = sum(data)
            max_pos = index
    print(total_path[max_pos])
