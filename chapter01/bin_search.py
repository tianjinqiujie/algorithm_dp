#-*- coding:utf-8 -*-
# 二分查找（折半查找）
import random
def random_list(start,end,length):
    data_list = []
    for i in range(length):
        data_list.append(random.randint(start,end))
    return data_list

data = random_list(1,100,10)
data = sorted(data)
# data = [1,3,4,6,7,8,11,23,45,65,76,87,88,91,92,96,98,100]

def search2(left,right,data_list,target):
    if left > right:
        return -1
    mid = int((left + right)/2)
    if data_list[mid] == target:
        return mid
    elif data_list[mid] < target:
        # 如果中间值小于目标值，则继续在右侧二分查找
        return search2(mid+1,right,data_list,target)
    else:
        # 如果中间值大于目标值，则继续在左侧二分查找
        return search2(left,mid-1,data_list,target)


def search(data_list,target):
    left = 0
    right = len(data_list) - 1
    target_post = -1
    while left <= right:
        # 1.找到[left，right]中间的值
        mid = int((left+right)/2)
        # 2.判断中间位置的值和目标值的大小
        if data_list[mid] == target:
            target_post = mid
            break
        elif data_list[mid] < target:
            # 如果中间值小于目标，则在右侧继续二分查找
            left = mid + 1
        else:
            # 如果中间值大于目标，则在左侧继续二分查找
            right = mid - 1
    return target_post

if __name__ == "__main__":
    print(data)
    target = random.randint(0,len(data)-1)
    print(data[target])
    pos = search(data,data[target])
    if pos >=0:
        print("查询到数据，所在位置:{}".format(pos))
    else:
        print("目标不在列表中")