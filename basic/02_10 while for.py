i=0
totol=0
while i<10:
    print (i,' ')
    i+=1
    totol+=i
print (totol)

alphabet=['a','b','c','d']
for character in alphabet:
    print(character)
    
total=0
for i in range(100):
    total+=i
print(total)

#continue
total=0
for i in range(10):
    if i%2:
        continue
    print (i)

#break与else

#当循环正常结束时，else执行
#通过break跳出，else不执行



#执行
values = [7, 6, 4, 7, 19, 2, 1]
for x in values:
    if x <= 10:
        print ('Found:', x)
        break
else:
    print ('All values greater than 10')
#不执行
values = [11, 12, 13, 100]
for x in values:
    if x <= 10:
        print ('Found:', x)
        break
else:
    print ('All values greater than 10')

#循环遍历字典元素
d={'x':1,'y':2,'z':3}
for key in d:
    print (key,"corresponds to",d[key])

#或者d.items()
for key,value in d.items():
    print(key,'corresponds to',value)

#并行迭代
names=['a','b','c','d']
ages=[1,2,3,4]
for i in range(len(names)):
    print(names[i],'is',ages[i],'years old')
#或zip
for name,age in zip(names,ages):
    print(name,'is',age,'years old')

#按索引迭代
strings=['aa','aab','bbcaa']
index=0
for string in strings:
    if 'ab' in string:
        strings[index]='change'
    index+=1
print(strings)

#或使用emumerate
for index,string in enumerate(strings):
    if 'ca' in string:
        strings[index]='change2'
print(strings)

#列表推导式,简便地生成列表
values = [10,21,4,7,12]
squares = [x**2 for x in values]
print(squares)

squares = [x**2 for x in values if x<=10]
print(squares)

#也可以生成集合和字典
squares_set = {x**2 for x in values if x<=10}
print(squares_set)
squares_dict={x:x**2 for x in values if x<=10}
print(squares_dict)

#利用列表推导式计算
total = sum(x**2 for x in values if x<=10)
print(total)