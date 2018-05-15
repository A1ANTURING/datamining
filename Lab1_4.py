import numpy as np
from matplotlib.pyplot import plot
from matplotlib.pyplot import show
fp = open(r"magic04.txt")
result = []
b = []
for linea in fp.readlines():  # 逐行读取文本
    linea = [float(x) for x in linea.split(',')[:-1]]  # 以‘，’分割数据，并且不读每行的最后一个数据，且将数据强制转换成float型。
    result.append(linea)  # 将读取的内容加入result数组中
fp.close()  # print(result) 打印读取结果
a = np.array(result)
b = a[:, 0]  # 第一列数据
c = a[:, 1]  # 第二列数据
print("相关系数为:")
print(np.corrcoef(b, c))
t = np.arange(len(b))
plot(t, b, lw=1)
plot(t, c, lw=2)
show()
