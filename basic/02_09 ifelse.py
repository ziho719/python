x=0.5
if x>0:
    print('x > 0')
#缩进代表起始

x=0
if x>0:
    print('x>0')
elif x<0:
    print(x<0)
else:
    print('x==0')

#逻辑连接
x=10
y=-5
if x>0 and y<0:
    print("x>0 and y<0")

if x>0 or y>0:
    print("||")

#False None 0 空字符串等会作为 假

if -1<0<1 :
    print('-1<0<1')
#连续的判断