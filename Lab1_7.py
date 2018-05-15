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
max = 0
min = sys.maxsize
b = [0 for i in range(0, 10)]  # 定义长度为10的数组
for i in range(0, 10):
    b[i] = a[:, i]  # 每一数组存储每一列的元素
for i in range(0, 9):  # 用一个嵌套for输出每一对属性的协方差矩阵，其中右上角和左下角的值为两属性之间的协方差。。
    for j in range(i+1, 10):
        c = np.cov(b[i], b[j])
        print(c)
        if c[0][1] > max:
            max = c[0][1]
        if c[0][1] < min:
            min = c[0][1]
print("最大最小协方差分别为：", max, min)
