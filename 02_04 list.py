l=[1,2.0,'hello']
print(l)
#使用[]

empty=[]
print(empty)

empty=list()
print(empty)
#空列表的生成

length=len(l)
print(length)

a=[1,2,3]
b=[3.2,'hello']
print(a+b)
print(l*2)
#加号连接，乘号复制

a=[10,11,12,13,14]
print(a[0])
print(a[-1])
print(a[2:-1])

s='hello world'
#   s[0]='H'
#字符串是常量不能修改

a[0]=100
print(a)

a[1:3]=[1,2]
print(a)
a[1:3]=[1,2,3,4]
print(a)
a[1:3]=[]
print(a)

a=[10,11,12,13,14]
a[::2]=[1,2,3]
print(a)
#对于不连续的分片，数目必须一致

a=[1002,'a','b','c']
del(a[0])
print(a)

a=[1002,'a','b','c']
del(a[1:])
print(a)

a=[1,2,1,2,1]
del(a[::2])
print(a)
#del方法可以删除

a=[10,11,12,13,14]
print(10 in a)
print(10 not in a)
#用in测试从属关系

a=[10,'eleven',[12,13]]
print(a[2])
print(a[2][1])
#列表可以包含列表

a=[1,2,3,2,1]
c=a.count(1)
print(c)
#返回出现次数

print(a.index(1))
#返回第一次出现位置

#print(a.index(12))
#没有直接throw

a=[10,11,12]
a.append([11,12])
print(a)
a.extend([14,16])
print(a)
#均改变列表，append整个添加到末尾，extend相当于a+=b

a=[10,11,12,13,14]
a.insert(3,'a')
print(a)
#'a'成为index为3的元素

a.remove('a')
print(a)
#删除第一个出现

p=a.pop(2)
print(p)
print(a)
#删除传入index的元素并返回

a=[12,1,24,4,11,3]
a.sort()
print(a)
#sort改变原列表的排序

a=[12,1,24,4,11,3]
b=sorted(a)
print(a)
print(b)
#sorted

a=[1,2,3,4,5,6]
a.reverse()
print(a)

a=[1,2,3,4,5,6]
b=a[::-1]
print(a)
print(b)
#不改变原列表的reverse

