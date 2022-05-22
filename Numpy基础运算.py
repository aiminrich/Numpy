import numpy as np

a = np.array([10,20,30,40])
b = np.arange(4)
print('a为:',a)
print('b为:',b)
c = a-b
print('c为:',c)
#加法
d = a + b
print('d为：',d)

#乘法
e = b**2
print('e为:',e)

#三角函数的运算
f = 10*np.sin(a)    #cos、tan类似
print('f为:',f)

#判断array里有多少个值，有哪些值小于某个数，大于某个数，等于某个数
print('b中小于3的元素为：',b<3)    #大于等于都类似，返回一个布尔值

#运算二维矩阵
g = np.array([[1,2],
                      [2,3]])
print('g为:',g)
h = np.arange(4).reshape((2,2))
print('h为:',h)

#1.运行矩阵的乘法
i = g*h   #逐个相乘
i_dot = np.dot(g,h)    #矩阵相乘
i_dot_2 = g.dot(h)
print('i为:',i)
print('i_dot为:',i_dot)
print('i_dot_2为：',i_dot_2)

j = np.random.random((2,4))    #创建一个随机生成的array，需要给定的参数是：shape（形状）2行4列
print('j为:\n',j)
#找矩阵的最大值、最小值、求和
print('j元素求和结果为:\n',np.sum(j,axis=1))   #axis表示求和的方式，如果在行数中求和，axis=1;如果在列数中求和，axis=0
print('j中最小值为:\n',np.min(j))
print('j中最大值为:\n',np.max(j))