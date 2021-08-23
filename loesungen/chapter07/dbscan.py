from sklearn.datasets import load_iris
from sklearn.cluster import DBSCAN
import numpy as np

X, y = load_iris(return_X_y=True)
dbscan = DBSCAN(eps = 0.6, min_samples = 4).fit(X)
labels = dbscan.labels_
print(labels)
n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
print("Anzahl Cluster:", n_clusters)
n_noisy = len([1 for sample in labels if sample == -1])
print("Anzahl nicht eindeutig zuzuordnender Elemente:", n_noisy)
