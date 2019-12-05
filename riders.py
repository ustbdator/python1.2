### 将每日下载的骑手数据命名放入目标文件夹，运行程序即可以得到环胜骑手工时汇总数据
import numpy as np
import pandas as pd
from pylab import *
df_BJ=pd.read_csv("beijing.csv",encoding='gb18030')
df_HZ=pd.read_csv("hangzhou.csv",encoding='gb18030')
df_NB=pd.read_csv("ningbo.csv",encoding='gb18030')
df_QZ=pd.read_csv("quzhou.csv",encoding='gb18030')
print(df_BJ.dtypes)
df1=df_BJ[df_BJ['供应商'].str.contains("环胜|虚拟")]
print(df1.dtypes)
df2=df_HZ[df_HZ['供应商'].str.contains("环胜")]
df3=df_HZ[df_HZ['供应商'].str.contains("虚拟")]
df3=df3[df3['骑士姓名'].str.contains("环胜")]
df4=df_NB[df_NB['供应商'].str.contains("环胜")]
df5=df_NB[df_NB['供应商'].str.contains("虚拟")]
df5=df5[df5['骑士姓名'].str.contains("环胜")]
#df3=[df_NB[df_NB['供应商'].str.contains("环胜")],df_NB[df_NB['供应商'].str.contains("虚拟")&df_NB['骑手姓名'].str.contains("环胜")]]
df6=df_QZ[df_QZ['供应商'].str.contains("环胜")]
df_all=pd.concat([df1,df2,df3,df4,df5,df6])
df_all['日期']=pd.to_datetime(df_all['日期'],format='%Y/%m/%d')
df_all['日期']=df_all['日期'].dt.date
df_all.to_excel(excel_writer="本日骑手数据.xlsx",sheet_name='骑手数据',index=False)