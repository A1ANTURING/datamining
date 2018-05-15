from sklearn import preprocessing
import numpy as np
data = np.loadtxt("iris.txt", delimiter=",", usecols=(0, 1, 2, 3), dtype=float)
target = np.loadtxt("iris.txt", delimiter=",", usecols=(4,), dtype=str)
# print(set(target))
print("核矩阵:")
a = np.dot(data, data.T)
k = a*a
print(k)
print("中心化")
mean = np.mean(k)
Ck = k-mean
print(Ck)
print("归一化")
Nk = preprocessing.scale(k)  # Numpy矩阵预处理类库
print(Nk)


