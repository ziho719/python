#元组不可变，用（）生成
t=(10,11,12,13,14)
print(t)

print(t[0])
print(t[0:3])

#单个元素的元组生成
a=(10,)
print(a)
print(type(a))

a=(10)
print(a)
print(type(a))

a=[10,11,11]
b=tuple(a)
print(a)
print(b)

print(a.count(11))
print(a.index(11))
#可以使用不变的方法

