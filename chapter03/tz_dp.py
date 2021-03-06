#-*- coding:utf-8 -*-

values = [
    [0,20,50,65,80,85,85],
    [0,20,40,50,55,60,65],
    [0,25,60,85,100,110,115],
    [0,25,40,50,60,65,70]
 ]

pre_max = values[3]
for k in range(len(values)-1,-1,-1):
    new_pre_max = [0]
    for i in range(10,61,10):
        # i代表假设手中有i万元
        value_list = []
        for j in range(0,i+1,10):
            value_list.append(pre_max[int(j/10)] + values[k-1][int((i-j)/10)])
        new_pre_max.append(max(value_list))
    pre_max = new_pre_max

print(pre_max)