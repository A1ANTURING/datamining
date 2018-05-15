#!/usr/bin/python
import numpy as np
import scipy.stats as st
from matplotlib.pyplot import plot
from matplotlib.pyplot import show
fp = open(r"magic04.txt")
result = []
b = []
for linea in fp.readlines():  # 逐行读取文本
    # 以‘，’分割数据，并且不读每行的最后一个数据，且将数据强制转换成float型。
    linea = [float(x) for x in linea.split(',')[:-1]]
    result.append(linea)  # 将读取的内容加入result数组中
fp.close()
a = np.array(result)
print(a.shape[0])  # 获得行数
b = a[:, 0]
print(b.var())
c = float(np.max(b)-np.min(b))/a.shape[0]  # 获得步长，为了精确强制转换为float
x = np.arange(np.min(b), np.max(b), c)
loc = (np.max(b)+np.min(b))/2  # 获得均值
scala = b.var()  # 获得方差
y = st.norm.pdf(x, loc, scala)  # 统计函数库script
plot(x, y)
show()
