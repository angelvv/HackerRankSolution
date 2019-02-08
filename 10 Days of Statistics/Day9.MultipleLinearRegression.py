# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
from sklearn.linear_model import LinearRegression

# read inputs for: X_train, Y_train
m,n = [int(x) for x in input().split()]

X_train, Y_train = [], []
for _ in range(n):
    data = input().split()
    X_train.append(data[:-1])
    Y_train.append(data[-1])
X_train = np.array(X_train, float)
Y_train = np.array(Y_train, float)

# fit LinearRegression classifier
clf = LinearRegression()
clf.fit(X_train, Y_train)

# predict for each set of test features
q = int(input())
for _ in range(q):
    prediction = clf.predict(np.array(input().split(), float).reshape(1, -1))
    print(*prediction)  #asterisk doing unpacking