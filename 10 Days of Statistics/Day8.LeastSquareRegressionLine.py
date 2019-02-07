# Enter your code here. Read input from STDIN. Print output to STDOUT
"""HackerRank doesn't support sklearn
from sklearn import linear_model
import numpy as np

xl = [95, 85, 80, 70, 60]
x = np.asarray(xl).reshape(-1, 1)
y = [85, 95, 70, 65, 70]
lm = linear_model.LinearRegression()
lm.fit(x, y)
#print(lm.intercept_)
#print(lm.coef_[0])
print('%0.3f' %lm.predict([80]))
"""
n = 5
X = [95, 85, 80, 70, 60]
Y = [85, 95, 70, 65, 70]

b = (n*sum([X[i]*Y[i] for i in range(n)]) - sum(X)*sum(Y)) / (n*sum([X[i]**2 for i in range(n)]) - sum(X)**2)
a = sum(Y)/n - b*(sum(X)/n)
print('%0.3f' %(a + b*80))
