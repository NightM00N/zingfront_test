# -*- coding:utf-8 -*-

'''
@author: zjm
@file: 3_wangzhe.py
@time: 2019/5/12 0:59
@desc: 智慧农药，二叉树树形递归
'''
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

result = []

def targets(people, letters, result, result_dict={}):
    if not result_dict:# 初始化
        result_dict["people"] = people
        result_dict["x"] = 0
        result_dict["y"] = 0
        result_dict["xy"] = []
    # 计算该步各英雄血量
    people = {}
    for i in result_dict["people"].keys():
        result_dict["people"][i][0] += letters[result_dict["x"]][result_dict["y"]]
        if result_dict["people"][i][0] > 0:
            people[i] = result_dict["people"][i]
    result_dict["people"] = people
    # 记录路径坐标
    result_dict["xy"].append(str(result_dict["x"])+","+str(result_dict["y"]))
    # 英雄全部阵亡，回溯
    if len(people) == 0:
        return
    # 获取地图深度
    x_len = len(letters[0])
    y_len = len(letters)
    # 终点
    if result_dict["x"] + 1 >= x_len and result_dict["y"] + 1 >= y_len:
        result.append(result_dict)


    if result_dict["x"]+1 < x_len:# 下
        result_dict["x"] += 1
        targets(people, letters, result, result_dict)
    if result_dict["y"]+1 < y_len:# 右
        result_dict["y"] += 1
        targets(people, letters, result, result_dict)


targets(people, letters, result)
print(result)