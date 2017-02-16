# -*- encoding: utf-8 -*-
from knock05 import n_gram

X = set(n_gram("paraparaparadise", 2))
Y = set(n_gram("paragraph", 2))

print("X " + str(X))
print("Y " + str(Y))
print("和集合 " + str(X.union(Y)))
print("積集合 " + str(X.intersection(Y)))
print("X - Y " + str(X.difference(Y)))
print("Y - X " + str(Y.difference(X)))
print("seがXに含まれるか？" + str("se" in X))
print("seがYに含まれるか？" + str("se" in Y))