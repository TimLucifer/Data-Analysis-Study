import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# ---------------------------
"""
0    1                    a    1
1    2                    b    2
2    3                   c    3
3    4                   d    4
未指定index和指定后 x.index：
RangeIndex(start=0, stop=4, step=1)
Index(['a', 'b', 'c', 'd'], dtype='object')
"""
# x1 = Series([1, 2, 3, 4])
# x2 = Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
# d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# x3 = Series(d)

# ---------------------------
# data = {'chinese': [11, 22, 33, 44, 55], 'english': [12, 23, 34, 45, 56],
#         'math': [22, 33, 44, 55, 66]}
# df1 = DataFrame(data)
# df2 = DataFrame(data, index=['S1', 'S2', 'S3', 'S4', 'S5'],
#                 columns=['english', 'chinese', 'math'])

# ---------------------------
# score = DataFrame(pd.read_excel('data.xlsx'))
# score.to_excel('data1.xlsx')

# ---------------------------
"""
    数据清洗
    一般会遇到以下几种情况：
    1.删除DataFrame中不必要的行或列。
    2.重命名列名columns， 让列表更容易识别。
    3.去重复的值。
    4.格式问题：
        更改数据格式
         df2['chinese'] = df2['chinese'].astype('str')
        数据间的空格
         df2['chinese'] = df2['chinese'].map(str.strip)
         df2['chinese'] = df2['chinese'].str.strip('$')
        大小写转换
         df2.columns = df2.columns.str.upper()
         df2.columns = df2.columns.str.lower()
         df2.columns = df2.columns.str.title()
        查找空值
         df2.isnull()
         df2.isnull().any 查看那列存在空值
        
"""
# example:

data = {'Chinese': [66, 95, 93, 90, 80], 'English': [65, 85, 92, 88, 90], 'Math': [30, 98, 96, 77, 90]}
df2 = DataFrame(data, index=['ZhangFei', 'GuanYu', 'ZhaoYun', 'HuangZhong', 'DianWei'],
                columns=['English', 'Math', 'Chinese'])

#  1.
# df2 = df2.drop(columns=['chinese'])
# df2 = df2.drop(index=['S1'])

#  2.
# df2.rename(columns={'chinese': 'yu_wen', 'math': 'shu_xue'}, inplace=True)

#  3.  ！！去重复行
# df = df2.drop_duplicates()

#  4. 很多时候数据格式不规范，可以用astype函数来规范数据格式
# df2['chinese'] = df2['chinese'].astype('str')
# df2['chinese'].astype(np.int64)
# df2['chinese'] = df2['chinese'].map(str.strip)
# df2['chinese'] = df2['chinese'].str.strip('$')
# df2.columns = df2.columns.str.upper()
# df2.columns = df2.columns.str.lower()
# df2.columns = df2.columns.str.title()

# ---------------------------
"""
使用apply函数对数据清洗
"""


# df2['Chinese'] = df2['Chinese'].astype('str')
# df2['Chinese'] = df2['Chinese'].apply(str.upper)
def double_df(x):
    return x * 2


def plus(df, n, m):
    df['new1'] = (df['Chinese'] + df['English']) * m
    df['new2'] = (df['Chinese'] + df['English']) * n
    return df


df2 = df2.apply(plus, axis=1, args=(2, 3,))

# df2['Chinese'] = df2['Chinese'].apply(double_df)
print(df2)
