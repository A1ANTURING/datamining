import math
import numpy as np
data = np.loadtxt("iris.txt", delimiter=",", usecols=(0, 1, 2, 3), dtype=float)
D1 = [[data[i][j]**2 for j in range(len(data[i]))] for i in range(len(data))]  # 算矩阵中每个数的平方
# 算矩阵中每行数据两两互乘
a = math.sqrt(2)  # 得到根号2
d2 = [[a * data[i][0] * data[i][k]] for i in range(len(data))for k in range(1, 4)]
D2 = np.array(d2).reshape(150, 3)  # 将一维矩阵变为二维矩阵
d3 = [[a * data[i][1] * data[i][k]] for i in range(len(data))for k in range(2, 4)]
D3 = np.array(d3).reshape(150, 2)
d4 = [[a * data[i][2] * data[i][k]] for i in range(len(data))for k in range(3, 4)]
D4 = np.array(d4).reshape(150, 1)
D = np.hstack((D1, D2, D3, D4))  # 将四个矩阵进行按行拼接
print(D)
mean = np.mean(D)
Cd = D-mean  # 矩阵中心化
Cd /= np.std(Cd)  # 矩阵归一化
print("矩阵归一化", Cd)
