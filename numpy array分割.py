import numpy as np

A = np.arange(12).reshape((3,4))
print('A为:\n',A)

#横向分割，分成2块
B = np.split(A,2,axis=1)
print('B为:\n',B)

#纵向分割，分割成三块
C = np.split(A,3,axis=0)
print('C为:\n',C)

#横向分割成3块，不等分
D = np.array_split(A,3,axis=1)
print('D is :\n',D)

E = np.vsplit(A,3)
print('E is :\n',E)

F = np.hsplit(A,2)
print('F is :\n',F)