#!/usr/bin/python
import numpy as np
import sys
fp = open(r"magic04.txt")
result = []
for linea in fp.readlines():  # 逐行读取文本
    linea = [float(x) for x in linea.split(',')[:-1]]  # 以‘，’分割数据，并且不读每行的最后一个数据，且将数据强制转换成float型。
    result.append(linea)  # 将读取的内容加入result数组中
fp.close()
a = np.array(result)
b = [0 for i in range(0, 10)]  # 定义长度为10的数组
max = 0
min = sys.maxsize
for i in range(0, 10):
    b[i] = a[:, i]  # 每一数组存储每一列的元素
    print(b[i].var())  # 打印每一列的方差
    if b[i].var() > max:
        max = b[i].var()
    if b[i].var() < min:
        min = b[i].var()
print("最大最小方差分别为：", max, min)


