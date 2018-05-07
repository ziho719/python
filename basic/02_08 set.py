#创建集合
a=set()
print(type(a))

l=[1,2,3,1]
a=set(l)
print(a)

a={1,2,3,1}
print(a)

#取并
a={1,2,3,4}
b={3,4,5,6}
print(a.union(b))
print(b.union(a))
print(a|b)
print(a)

#取交集
print(a.intersection(b))
print(a&b)

#差集
print(a.difference(b))
print(b.difference(a))
print(a-b)

#对称差，(a-b)|(b-a)
print(a.symmetric_difference(b))
print(a^b)

#包含关系
a={1,2,3}
b={1,2}
print(b.issubset(a))
print(b<=a)
print(a.issubset(a))
print(a<=a)
print(a<a)

#add
a.add(5)
a.add(3)
print(a)

#update添加多个元素
a.update([5,6,7])
print(a)

#remove、pop、discard
a.remove(6) #不存在会报错
print(a)
a.pop() #随机
print(a)
a.discard(3)
a.discard(3) #不会报错
print(a)

#_update会修改原元素
a={1,2,3}
b={1,2}
a.difference_update(b)
print(a)

#不可变集合frozeset
s=frozenset([1,2,3,'a',1])

#可以作为字典的键，和元组比较frozeset不区分顺序
flight_distance={}
city_pair=frozenset(['A','NY'])
flight_distance[city_pair]=2948
print(flight_distance)
print(flight_distance[frozenset(['NY','A'])])

