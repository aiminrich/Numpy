import numpy as np

A = np.array([1,1,1])
B = np.array([2,2,2])
print('A为:\n',A)
print('B为:\n',B)

#将A、B两个array上下合并
print('A、B上下合并结果为:\n',np.vstack((A,B)))

#将A、B进行行合并
print('A、B进行行合并结果为:\n',np.hstack((A,B)))

#如何将A转置
print('A的转置为:\n',A[:,np.newaxis])
C = A[:,np.newaxis]
D = B[:,np.newaxis]
E = np.vstack((C,D))
F = np.hstack((C,D))
print('E为:\n',E)
print('F为:\n',F)

G = np.concatenate((A,B,B,A))   #进行多个array的合并
print('G为:\n',G)
H = np.concatenate((C,D,D,C),axis=0)
print('H为:\n',H)

