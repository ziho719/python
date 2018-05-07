def add(x,y):
    '''add two numbers'''
    a=x+y
    return a

def add2(x=1,y=2):
    a=x+y
    return a

print(add2())
print(add2(x=2))
print(add2(y=3))

#接收不定参数, *... 表示数目不定
def add3(x,*args):
    total=x
    for arg in args:
        total+=arg
    return total

print(add3(1,2,3,4,5))
print(add3(1,2,3))

def add4(x,**kwargs):
    """一个不定的字典"""
    total=x
    for arg,value in kwargs.items():
        print ("adding",arg)
        total+=value
    return total

print(add4(10,y=2,z=4)) 

#返回多个值
from math import atan2

def to_polar(x, y):
    r = (x**2 + y**2) ** 0.5
    theta = atan2(y, x)
    return r, theta

r, theta = to_polar(3, 4) #元组的解包
print (r, theta)

#元组形式传入
z=(2,3)
print(add(*z)) # *是必须的

#字典形式传入
z={'x':2,'y':3}
print(add(**z))


