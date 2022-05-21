import numpy as np

#数组。
array = np.array([[1,2,3],           #把矩阵列表转为数组
 [2,3,4]])
print(array)

print('number of dimention:',array.ndim)          #查看是几维数组
print('shape:',array.shape)                                #查看他的行数和列数
print('size:',array.size)                                     #查看array总共有多少元素
