s="hello world"
print(s)

s='hello world'
print(s)
#python可以使用单引号和双引号

s='hello'+' world'
print(s)

s='hello'*2
print(s)

l=len(s)
print(l)

line="1 2 3 4 5"
numbers=line.split()
print (numbers)
line="1,2,3,4,5"
numbers=line.split(',')
print(numbers)
#split以分隔符对line进行分割 

s=''
result=s.join(numbers)
print(result)
s=','
result=s.join(numbers)
print (result)
#以s为连接符连接一个str序列,不改变s而是返回一个新的值

s='hello world'
result=s.replace('world','python')
print(result)
#同样不改变s

print('hello world'.upper())
print('HELLO WORLD'.lower())

s='  hello world  '
result=s.strip()
print(result)
result=s.lstrip()
print(result)
result=s.rstrip()
print(result)
#分别返回去除两端空格、左端空格、右端空格的新字符串，括号缺省值为空格，可替换

print(dir(s))
#['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'] 
#字符串的所有方法

a='''hello world.
have a nice day'''
print(a)
#用于生成多行字符串，相当于中间加了\n

a=('hello world. '
    'have a nice day.')
print (a)
a='hello world. '\
    'have a nice day'
print (a)
#用于代码的换行，不是加\n

result=str(1.1+2.2)
print(result)
result=repr(1.1+2.2)
print(result)
#转换为字符串，结果一样

print(hex(255))
print(oct(255))
print(bin(255))
#分别是十六进制、八进制、二进制，返回字符串

print(int('23'))
print(int('FF',16))
print(int('377',8))
print(int('11111111',2))
print(float('3.5'))
#根据传入字符串返回数值，十进制

#format用于格式化字符串，用Format内的参数代替括号
result='{} {} {}'.format('a','b','c')
print (result)
result='{2} {1} {0}'.format('a','b','c')
print (result)
#指定的参数的位置
result='{color} {n} {x}'.format(n=10,x=1.5,color='blue')
print (result)
#指定了变量的名称
result='{color} {0} {x} {1}'.format(10,'foo',x=1.5,color='blue')
print (result)
#混合使用
from math import pi
result='{0:10} {1:10d} {2:10.2f}'.format('foo',5,2*pi)
print(result)
#用 ： 后的参数指定格式

