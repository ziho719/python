import numpy as np

#数组属性
a=np.arange(15).reshape(3,5)
print(a)
print(a.shape) #显示每个维度大小
print(a.ndim) #维的个数
print(a.dtype) #数组中元素的类型
print(a.itemsize) #每个元素的字节大小
print(a.size) #总共多少元素
print(type(a))

b=np.array([6,7,8])
print(b)
print(type(b))
#--------------------------------------------------------------------
#数组创建 Array Creation
b=np.array([6,7,8]) #从基础的列表或元组创建
b=np.array((6,7,8))
print(b)
b=np.array([[1,2,3],[2,3,4]])
print(b)
c=np.array([[1,2],[3,4]],dtype=complex)#显式指定类型
print(c)

print(np.zeros((3,4))) #全是0
print(np.zeros_like(a)) #返回与输入数组相同shape的数组
print(np.ones((3,4),dtype=np.int32))#还有empty

a=np.arange(10,30,5) #起始、结束、步长 生成数组 ,起始默认0，步长默认1
print(a)
a=np.linspace(0,2,9) #start,end,numOfElem
print(a)
#--------------------------------------------------------------------
#输出数组 printing arrays

#--------------------------------------------------------------------
#基本操作 Basic Operations
a=np.array([20,30,40,50])
b=np.arange(4)
print(a-b) #np.array的操作基本为逐元素
print(b**2)
print(10*np.sin(a))
print(a<35)

#不用*，在array中用 dot 进行矩阵相乘
A = np.array( [[1,1],
             [0,1]] )
B = np.array( [[2,0],
            [3,4]] )
print(A*B)
print(A.dot(B))
print(np.dot(A, B))

#一些操作，例如 += 和 *= ，可以修改现有数组，而不是创建新的数组。
a+=1
print(A.sum())
print(a.max())
print(a.min()) 

#指定轴
b=np.arange(12).reshape(3,4)
print(b)
print(b.sum())
print(b.sum(axis=0)) #相当于一个for，变化的是b[][][]第几个大括号的变量
print(b.min(axis=1))
print(b.cumsum(axis=1)) #累加和，大概是a[i]+=a[i-1]这种
