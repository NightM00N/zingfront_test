# -*- coding:utf-8 -*-
'''
@author: zjm
@file: 3_wangzhe.py
@time: 2019/5/12 0:59
@desc: 智慧农药，二叉树树形递归
'''

import json
from pprint import pprint
from copy import deepcopy

# 地图
letters = [
    [133, -523, -558, 846, -907, -1224, -1346, 787, -411, -1826],
    [-1478, -853, -1401, 341, -26, 759, -444, 174, -1594, -2000],
    [861, -584, 670, 696, 676, -1674, -1737, -1407, -484, 246],
    [133, -1669, -419, -382, -895, 732, -1278, -1802, -527, 862],
    [133, 544, -1943, 563, -380, -1268, 266, -1309, -1946, 85],
    [133, -1631, -168, 741, -211, -1070, -1873, -554, 243, -901],
    [133, 971, -21, -1111, 463, 944, -127, -1414, -1463, -1287],
    [133, -1886, -1159, -73, 555, -426, -190, -1750, -1028, -188],
    [133, -1654, -931, -1100, -433, -1643, -1281, -455, 904, -126],
    [-1494, -632, 243, 90, 993, 322, 32, -388, -225, 952],
]
# 英雄
people = {
    'mq': [10000, 100],
    'cyj': [5000, 200],
    'ys': [2000, 500],
    'k': [1000, 1000],
    'drj': [100, 2000],
}

# 获取地图深度
x_len = len(letters[0])
y_len = len(letters)
print(f'x_len {x_len} y_len {y_len}')


def targets(_people, result_dict=None):
    if result_dict is None:
        result_dict = {}

    if len(result_dict) == 0:  # 初始化
        result_dict["people"] = _people
        result_dict["x"] = 0
        result_dict["y"] = 0
        result_dict["xy"] = []

    # 计算该步各英雄血量
    # print(f' Y {result_dict["y"]} X {result_dict["x"]}')
    _people = {}
    for i in result_dict["people"].keys():
        result_dict["people"][i][0] += letters[result_dict["y"]][result_dict["x"]]
        if result_dict["people"][i][0] > 0:
            _people[i] = result_dict["people"][i]

    # print('\t', f'{letters[result_dict["y"]][result_dict["x"]]}', 'PEOPLE: ', _people)
    result_dict["people"] = _people
    # 记录路径坐标
    result_dict["xy"].append(str(result_dict["x"]) + "," + str(result_dict["y"]))
    # 英雄全部阵亡，回溯
    if len(_people) == 0:
        # print(f'DEAD X {result_dict["x"]} Y {result_dict["y"]}')
        return []
    # 终点
    if result_dict["x"] + 1 >= x_len and result_dict["y"] + 1 >= y_len:
        # _result.append(result_dict)
        return [result_dict]

    x_arr = deepcopy(result_dict)
    y_arr = deepcopy(result_dict)
    end1 = end2 = []
    if x_arr["x"] + 1 < x_len:
        # print('# TO RIGHT')
        x_arr["x"] += 1
        end1 = targets(_people, x_arr)
        # result_dict["x"] -= 1
    if y_arr["y"] + 1 < y_len:
        # print('# TO DOWN')
        y_arr["y"] += 1
        end2 = targets(_people, y_arr)
        # result_dict["y"] -= 1
    end = [*end1, *end2]
    # print('\t\t', end)
    return end


def good(arr):
    max_mq=max_cyj=max_ys=max_k=max_drj = 0
    route_mq =route_cyj =route_ys =route_k =route_drj = []
    for item in arr:
        # print(item)
        if "mq" in item['people'] and item['people']['mq'][0] > max_mq:
            max_mq = item['people']['mq'][0]
            route_mq = item
        if "cyj" in item['people'] and item['people']['cyj'][0] > max_cyj:
            max_cyj = item['people']['cyj'][0]
            route_cyj = item
        if "ys" in item['people'] and item['people']['ys'][0] > max_ys:
            max_ys = item['people']['ys'][0]
            route_ys = item
        if "k" in item['people'] and item['people']['k'][0] > max_k:
            max_k = item['people']['k'][0]
            route_k = item
        if "drj" in item['people'] and item['people']['drj'][0] > max_drj:
            max_drj = item['people']['drj'][0]
            route_drj = item
    # 打印各个英雄的最佳路线，即存活，且血量最高
    print(route_mq)
    print(route_cyj)
    print(route_ys)
    print(route_k)
    print(route_drj)
    # return json.dumps(route_mq)


if __name__ == '__main__':
    tmp_arr = targets(people)
    print(tmp_arr, len(tmp_arr))
    # pprint(tmp_arr)
    good(tmp_arr)
    # print(good(tmp_arr))

# 时间复杂度： O(n^2)
# 空间复杂度：O(n^2)