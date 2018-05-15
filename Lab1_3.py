#!/usr/bin/python
import numpy as np
fp = open(r"magic04.txt")
result = []
for linea in fp.readlines():  # 逐行读取文本
    linea = [float(x) for x in linea.split(',')[:-1]]  # 以‘，’分割数据，并且不读每行的最后一个数据，且将数据强制转换成float型。
    result.append(linea)  # 将读取的内容加入result数组中
fp.close()
print(result)  # 打印读取结果
a = np.array(result)
n = a.shape[0]
b = np.mean(a, axis=0)
z = a - b   # 数据中心化
print(np.cumsum(np.dot(z, z.T))/n)  # 计算外积
