import numpy as np

A = np.arange(3,15)
print('A为:\n',A)
print('A的第2个值为:\n',A[2])

#二维Array中
B = np.arange(3,15).reshape((3,4))
print('B为:\n',B)
print('B的第二行为:\n',B[2])
print('B的第二行为:\n',B[2,:])
print('B的第一行第一列为:\n',B[1][1])
print('B的第一行第一列为:\n',B[1,1])
print('B的第一列为:\n',B[:,1])
print('B的第一行从第一位到第二位的值为:\n',B[1,1:3])

'''应用：运用for循环'''
#迭代B的每一行
for row in B:
    print('B的每一行依次为:\n',row)
#迭代B的每一列
for column in B.T:
    print('B的每一列依次为:\n',column)

#迭代项目
print('B.flat为:\n',B.flatten())
for item in B.flat:
    print(item)