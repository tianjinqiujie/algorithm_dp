#-*- coding:utf-8 -*-
# 斐波那契

from _collections import defaultdict

total = defaultdict(int)


def fib_test(k):  # 递归
    # 求解第k个数的值
    assert k > 0, "k必须大于0"
    if k in [1, 2]:
        return 1
    global total
    if k in total:
        result = total[k]
    else:
        result = fib_test(k - 1) + fib_test(k - 2)
        total[k] = result
    return result


def fib_test2(k):  # 非递归
    # 求解第k个数的值
    assert k > 0, "k必须大于0"
    if k in [1, 2]:
        return 1
    k_1 = 1
    k_2 = 2
    for i in range(3, k + 1):
        global total
        total[k] += 1
        tmp = k_1
        k_1 = k_1 + k_2
        k_2 = tmp
    return k_1


if __name__ == "__main__":
    from datetime import datetime
    # 搜索+记忆算法
    start_time = datetime.now()
    print(fib_test2(4))
    print("递归耗时：{}".format((datetime.now() - start_time).total_seconds()))
    print(total)