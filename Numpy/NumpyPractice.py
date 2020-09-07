import numpy as np

"""
Numpy数学运算
"""
# from NumPy_Math import NumPyMath
# ----------------------
"""
    引用NumPy后，通过array函数创建数组，如多重数组，将一个数组作为一个元素
    嵌套起来。
    shape属性获得数组的大小
    dtypt获得元素的属性。
"""
# a = np.array([1, 2, 3])
# b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# b[1, 1] = 10

# ----------------------
"""
    结构数组：
    在C语言中，可以定义结构数组，通过struct定义结构类型，结构中的字段
    占用连续的内存空间，每一个结构体占用的内存大小都相同。
    
    NumPy中用dtype定义结构类型，在定义数组的时候，用array指定结构数组的类型
    dtype=person_type。
    查看字段的值：xxx = peoples[:]['chinese'],计算平均值使用np.mean。
"""
# person_type = np.dtype({
#     'names': ['name', 'age', 'chinese', 'math', 'english'],
#     'formats': ['S32', 'i', 'i', 'i', 'f']
# })
# peoples = np.array([('S1', 10, 20, 30, 40), ('S2', 20, 30, 40, 50.1),
#                     ('S3', 30, 40, 50, 60.2), ('S4', 40, 50, 60, 70.3)], dtype=person_type)

# ----------------------
"""
    ufunc运算 (universal function) 可对数组中的每个元素进行函数操作。采用C语言实现。
"""
# 初始值，终值，步长。不包含终值。
# x1 = np.arange(1, 11, 2)
# linspace (linear space) 线性等分向量。 初始值，终值，元素个数。包含终值。
# x2 = np.linspace(1, 9, 5)

# ----------------------
"""
    统计函数
    数据中的最大值，最小值，平均值。是否符合正态分布，方差，标准差多少等等。
    amin 最小值， amax 最大值 ptp 最值与最小值差
    percentile 统计数组的百分位数 范围(0%-100%)
    median 中位数 mean 平均数
    average 加权平均值 wts权重
    std 标准差：方差的算术平方根。在数学意义上，代表一组数据离平均值的分散程度。
    var 方差：每个数值与平均值之差的平方和的平均值
"""
# a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
"""
[1, 2, 3]
[4, 5, 6]       axis=0 Y轴     axis=1 X轴
[7, 8, 9]
"""
# print(np.amin(a), np.amin(a, 0), np.amax(a), np.amax(a, 0))
# print(np.ptp(a))
# print(np.percentile(a, 50), np.percentile(a, 50, axis=0))

# b = np.array([1, 2, 3, 4])
# wts = np.array([1, 2, 3, 4])
# print(np.average(b, weights=wts))

# ----------------------
"""
    NumPy 排序
    sort(a, axis=-1, kind='quicksort', order=None)
    默认快速排序(quicksort, mergesort, heapsort, 分别为快速排序，和并排苏， 堆排序)
    axis=-1默认 沿着数组的最后一个轴排序 axis=None代表采用扁平化方式作为一个向量进行排序。
    order 对于结构化的数组可以指定按照某个字段进行排序。
"""
# a = np.array([[14, 3, 2], [2, 4, 1]])
# print(np.sort(a), np.sort(axis=None))

# sort_type = np.dtype({
#     'names': ['T1', 'T2', 'T3', 'T4'],
#     'formats': ['i', 'i', 'i', 'i']
# })
#
# sort_list = np.array([(5, 3, 1, 8),
#                       (1, 3, 2, 5),
#                       (8, 5, 6, 9),
#                       (5, 6, 8, 7)], dtype=sort_type)
#
# print(sort_list)

