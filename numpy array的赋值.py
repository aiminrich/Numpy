import numpy as np

A = np.arange(4)
print('A is :\n',A)
B = A
C = A
D = B
A[0] = 11
print('current A is :\n',A)
print(B is A)
print('B is :\n',B)
print('C is :\n',C)
print('D is :\n',D)

#如果想要把A的值赋给B的值，但又不想把他们关联起来
E = A.copy()
print('E is :\n',E)
A[2] =520
print('current A is :\n',A)
print('current E is :\n',E)