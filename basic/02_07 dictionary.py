#字典 dictionary,在一些编程语言中也称为 hash ,map,是一种由键值对组成的数据结构

#使用{}或dict()来创建一个空的字典
a={}
print(type(a))
a=dict()
print(type(a))

#插入键值
a['one']='this is number 1'
a['two']='this is number 2'
print(a)

#查看键值
print(a['one'])

#更新键值
a['one']='this is 1'
print(a)

#初始化字典
b={'one':'this is one','two':2}
print(b)

#字典按插入顺序显示，不能使用索引0，1，2……

#键必须不可变，值可以是任意python对象

#浮点数不适合做键

#元组(1,2)和(2,1)是不同的键

print(a.get('one'))
print(a.get('1'))
print(a.get('1','Wrong'))
#get(self,key,default=None)当键不存在时返回default指定的值

print(a.pop('two'))
print(a)
#print(a.pop('1'))
print(a.pop('1','Wrong'))
#pop必须传入default

del a['one']
print(a)

#用update方法更新字典,效果拔群
person={}
person['first']='ziho'
person['last']='huang'
person['born']=1998
print(person)
person_modifications={'first':'ziho_','middle':'zhihao'}
person.update(person_modifications)
print(person)

#in查询键
print('first' in person)
print('like' in person)

#keys,values,items方法，返回列表，item是键值对组成的列表
print(person.keys())
print(person.values())
print(person.items())

print(len(person)) #返回长度

#clear方法,若使用a={}，只是指向新的字典
a={1:1.1,2:2.2}
print(a)
a.clear()
print(a)

#copy与deepcopy,copy是浅复制,deepcopy属于copy模块，是深复制
a={1:1.1,2:[1,2,3]}
b=a.copy()
b[1]=9
b[2].remove(2)
print(a)
print(b)

from copy import deepcopy
a={1:1.1,2:[1,2,3]}
b=deepcopy(a)
b[1]=9
b[2].remove(2)
print(a)
print(b)

#fromkeys提取字典的键，default=None为值，创建新的字典，
#调用时dict.或{}.
person2=dict.fromkeys(person,'default')
print(person2)