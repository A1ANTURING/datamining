import numpy as np
fp = open(r"magic04.txt")
result = []
b = []
for linea in fp.readlines():  # 逐行读取文本
    linea = [float(x) for x in linea.split(',')[:-1]]  # 以‘，’分割数据，并且不读每行的最后一个数据，且将数据强制转换成float型。
    result.append(linea)  # 将读取的内容加入result数组中
fp.close()
a = np.array(result)
b = np.mean(a, axis=0)  # 第一问的均值
n = a.shape[0]  # 获得行数
z = a-b  # 中心数据矩阵
print(np.dot(z.T, z)/n)
