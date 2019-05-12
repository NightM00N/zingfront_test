# -*- coding:utf-8 -*-

'''
@author: zjm
@file: 1_superset.py
@time: 2019/5/11 19:23
@desc: 判断A是不是B的超集
'''


def JudgeSuperset(A, B):
    A_list = list(A)
    B_list = list(B)
    # A串比B串小时直接返回False
    if len(A_list) < len(B_list):
        return False
    for i in B_list:
        if i in A_list:
            A_list.remove(i)
        else:
            return False
    return True

if __name__ == '__main__':
    print(JudgeSuperset("abccd", "abcc"))  # True
    print(JudgeSuperset("abccd", "abbcc"))  # False
    print(JudgeSuperset("abccd", "adcc"))  # True
    print(JudgeSuperset("abcc", "abccd"))  # False

# 时间复杂度：O(n)
# 空间复杂度：O(m+n)
