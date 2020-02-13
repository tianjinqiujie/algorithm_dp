#-*- coding:utf-8 -*-
# 通过回溯法求解0-1背包问题
info = [
    [3,8],
    [2,5],
    [5,12]
]

selects = []
max_selects =[]
max_value = 0
def search(depth,rest):
    if depth == 3:
        print(selects)
        values = []
        for index,select in enumerate(selects):
            values.append(select*info[index][1])
        global max_value
        if sum(values) > max_value:
            max_value = sum(values)
            print(max_value)
            global max_selects
            max_selects = selects[:]
            print(max_selects)
    else:
        # 1.不放
        # 1.设置现场
        selects.append(0)
        # 2.递归
        search(depth+1,rest)
        # 3.恢复现场
        selects.pop()

        # 2.放
        if rest >= info[depth][0]:
            # 1.设置相缠
            selects.append(1)
            # 2.递归
            search(depth+1,rest-info[depth][0])
            # 3.恢复现场
            selects.pop()
if __name__ == "__main__":
    search(0,5)
