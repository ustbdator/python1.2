# C:\Users\daojia\PycharmProjects\untitled\venv
import numpy as np
import pandas as pd
from pylab import *
import matplotlib.pyplot as plt #如果后续需要做图还需要导入matplotlib模块
plt.rcParams["font.sans-serif"]=["SimHei"]#输出图像的标题可以为中文正常输出
plt.rcParams["axes.unicode_minus"]=False #可以正常输出图线里的负号

# pd.set_option('max_columns', 10)
# pd.set_option('max_rows', 20)
'''pd.set_option('display.float_format', lambda x: '%.2f' % x)  # 禁用科学计数法
df1 = pd.read_excel("test.xlsx", sheet_name='Sheet1')
df2 = pd.read_excel("test.xlsx", sheet_name='Sheet2')
df3 = df1.merge(df2, how='left', on='月份')
print(df3)
df3.to_excel(excel_writer="vlook.xlsx",sheet_name='单价',index=False)'''##vlookup基本用法

df=pd.read_csv("data.csv",encoding='gb18030')
df1=df.groupby('城市')[['订单TC','准时TC']].agg('sum')
df1['不准时单']=df1['订单TC']-df1['准时TC']
df1['准时率']=df1['准时TC']/df1['订单TC']
df1=df1.apply(lambda x:x.head(5))
print(df1)##数据透视用法

df2=df.pivot_table(values=['订单TC','餐厅名称'],index=['市场','城市'],aggfunc={'订单TC':np.sum,'餐厅名称':np.count_nonzero})#aggfunc={'订单TC':np.sum,'餐厅名称':np.count_nonzero}
print(df2)
df3=df2.reset_index()#重置索引
print(df3)
X=df3.iloc[:,1]
Y=df3.iloc[:,2]
print(X)
print(Y)
print("取df3的前2行")
print(df3[0:2])#取df3的前2行
print("打印df3的总行数")
print(len(df3))
print("打印df3的总列数")
print(df3.columns.size)
print("df3行索引")
print(df3.index)
print("df3列名")
print(df3.columns)
print(df3.dtypes)
print(df3[df3['市场'].str.contains("广州")&df3['餐厅名称']>5])#将列数据字符串化然后筛选
print(df3[df3['餐厅名称']>5])
