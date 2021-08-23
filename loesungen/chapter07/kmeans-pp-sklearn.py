from sklearn.datasets import load_iris
from sklearn.cluster import kmeans_plusplus
import numpy as np

X, y = load_iris(return_X_y=True)
centers, indices = kmeans_plusplus(X, n_clusters = 3)
print("Zentroide:")
print(centers)
print("Anzahl Exemplare pro Cluster:", indices)
