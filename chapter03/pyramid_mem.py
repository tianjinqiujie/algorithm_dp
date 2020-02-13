
pyramid = [
    [13],
    [11,8],
    [12,7,26],
    [6,14,15,8],
    [12,17,13,24,11]
]
datas = [13]
total_path = []
max_value = 0
info = {}
def search_max(depth,y):
    if depth == len(pyramid)-1:
        return pyramid[depth][y]
    # 1.把下方的值交给下一个得到最大值
    # 2.把右下方的值交给下一个得到最大值
    # 1.任务可以下分，2.最优子结构，3.决策
    if "{}_{}".format(depth,y) in info:
        return info["{}_{}".format(depth,y)]
    else:
        left_max = search_max(depth + 1, y)
        right_max = search_max(depth + 1, y+1)
        max_value = pyramid[depth][y]+max(left_max,right_max)
        info["{}_{}".format(depth,y)] = max_value
        return max_value
if __name__ == "__main__":
    print(search_max(0,0))
    print(info)