import numpy as np
from sklearn.cluster import DBSCAN
data = np.loadtxt("iris.txt", delimiter=",", usecols=(0, 1, 2, 3), dtype=float)
DB = DBSCAN(eps=0.42, min_samples=5).fit(data)
core_samples_mask = np.zeros_like(DB.labels_, dtype=bool)
core_samples_mask[DB.core_sample_indices_] = True
labels = DB.labels_
n_clusters = len(set(labels))-(1 if -1 in labels else 0)  # 族的数目（忽略噪声）
print("族数目", n_clusters)
print("标签", labels)
for i in range(n_clusters):
    print('cluster', i, ':')
    print(list(data[labels == i].flatten()))

