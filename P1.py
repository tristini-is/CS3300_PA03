import numpy as np

#matrix D 3x3
D = np.array([[0.1,0.43,0],
             [0.15,0,0.37],
             [0.23,0.03,0.02]])
#matrix E 3x1
E = np.array([[20000],
             [30000],
             [25000]])
#identity matrix 3x3
I = np.eye(3)

F = I - D
#taking inverse of f
invF = np.linalg.inv(F)
#multiplying invF with E and rounding each number to nearest tenth
X = np.round(np.dot(invF,E), decimals=1)

print(X)