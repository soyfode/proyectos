from sklearn import datasets
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

iris = datasets.load_iris()
print(type(iris))
print(iris.keys())
print(type(iris.target))
print(150,4)

X = iris.data
Y = iris.target
df = pd.DataFrame(X, columns = iris.feature_names)
# print(df.head())

_ = pd.plotting.scatter_matrix(df,c=Y,figsize=[8,8],s=150,marker='D')
plt.show()


