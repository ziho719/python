#string是不可变量，字符串的方法只是返回一个新的字符串
s='hello world'
print(s.replace('world','Mars'))
print(s)

a=[1,2,3,4]
b=a
b[0]=100
print(a)
print(b)