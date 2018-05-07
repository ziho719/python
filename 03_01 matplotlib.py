import matplotlib
import numpy as np

#plot---matplotlib.pyplot.plot(*args * args, **kwargs * * kwargs)
import matplotlib.pyplot as plt

#---------------------------------------------------------------------------
#20

#---------------------------------------------------------------------------
#19

#---------------------------------------------------------------------------
#18

#---------------------------------------------------------------------------
#17

#---------------------------------------------------------------------------
#16

#---------------------------------------------------------------------------
#15

#---------------------------------------------------------------------------
#14
x = np.arange(0, 2*np.pi, 0.02)
y = np.sin(x)
y1 = np.sin(2*x)
y2 = np.sin(3*x)
ym1=np.ma.masked_where(y1>0.5,y1) #大概可以筛选一下？
ym2=np.ma.masked_where(y2<-0.5,y2)

lines = plt.plot(x, y, x, ym1, x, ym2, 'o')
plt.setp(lines[0], linewidth=4)
plt.setp(lines[1], linewidth=2)
plt.setp(lines[2], markersize=10)

plt.legend(('No mask', 'Masked if > 0.5', 'Masked if < -0.5'),
           loc='upper right')
plt.title('Masked line demo')
plt.show()
#---------------------------------------------------------------------------
#13
def f13(t):
    'a damped exponential 阻尼系数？'
    s1 = np.cos(2 * np.pi * t)
    e1 = np.exp(-t)
    return s1 * e1
t1 = np.arange(0.0, 5.0, .2)

l = plt.plot(t1, f13(t1), 'ro')
plt.setp(l, markersize=30)         #magic
plt.setp(l, markerfacecolor='C0')

plt.show()

#---------------------------------------------------------------------------
#12 主轴里插入轴
np.random.seed(19981222)
dt=0.001
t=np.arange(0.0,10.0,dt)
r=np.exp(-t[:1000]/0.05)  #脉冲响应？
x=np.random.randn(len(t))  #返回和t维数相同的随机数组
s=np.convolve(x,r)[:len(x)] * dt #卷积？！

plt.plot(t,s)
plt.axis([0,1,1.1*np.min(s),2*np.max(s)])
plt.xlabel('time(s)')
plt.ylabel('current(mA)')
plt.title('Gaussian colored noise')

#insert 1
a=plt.axes([.65,.6,.2,.2],facecolor='k')
n,bin,patches =plt.hist(s,400,density=True)  #直方图
plt.title('Probability')
plt.xticks([])  #刻度什么的
plt.yticks([])
#insert 2
a=plt.axes([0.2,0.6,.2,.2],facecolor='k')
plt.title('Impulse response')
plt.plot(t[:len(r)],r)
plt.xlim(0,0.2)
plt.xticks([])
plt.yticks([])
plt.show()
#---------------------------------------------------------------------------
#11
t = np.arange(-1, 2, .01)
s = np.sin(2 * np.pi * t)
plt.plot(t, s)

#y=0 的红粗线
plt.axhline(linewidth=8,y=0,color='#d62728')
#默认下x=1的线
plt.axvline(x=1)
#指定区域
plt.axhline(y=0.5,xmin=0.25,xmax=0.75,linewidth=8,color='#1f77b4')

plt.axhspan(0.25,0.75,facecolor='0.5',alpha=0.5)
plt.axvspan(1.25,1.55,facecolor='#2ca02c',alpha=0.5)
plt.axis([-1,2,-1,2])
plt.show()
#---------------------------------------------------------------------------
#10
t=np.arange(0.01,5.0,0.01)
s1=np.sin(2*np.pi*t)
s2=np.exp(-t)   #对linspace不能用
s3=np.sin(4*np.pi*t)

ax1=plt.subplot(311)
plt.plot(t,s1)
plt.setp(ax1.get_xticklabels(),fontsize=6)#Set a property on an artist object?

# share x only  看图的时候会一起移动
ax2=plt.subplot(312,sharex=ax1)
plt.plot(t,s2)
plt.title('small title')
plt.setp(ax2.get_xticklabels(),visible=False)

#share x y
ax3=plt.subplot(313,sharex=ax1,sharey=ax1)
plt.plot(t,s3)
plt.xlim(0.01,5.0)
plt.suptitle('This is a somewhat long figure title', fontsize=16)#大标题
plt.show()
#---------------------------------------------------------------------------
#9
t = np.arange(0.0, 2.0, 0.01)
s1 = np.sin(2*np.pi*t)
s2 = np.sin(4*np.pi*t)
plt.figure(1)
plt.subplot(211)
plt.plot(t, s1)
plt.subplot(212)
plt.plot(t, 2*s1)
plt.figure(2)    #切换窗口来画图
plt.plot(t, s2)
plt.figure(1)
plt.subplot(211)
plt.plot(t, s2, 's')
ax = plt.gca()
ax.set_xticklabels([])

plt.show()  #就是说这样会show 出好几个窗口
#---------------------------------------------------------------------------
#8 Invert Axes
t=np.arange(0.01,5.0,0.01)
s=np.exp(-t)
plt.plot(t,s)

plt.xlim(5,0) #x的limit,就是这句让x反过来了
plt.xlabel('decreasing time(s)')
plt.ylabel('volt(mV)')
plt.title('should be growing...')
plt.grid(True)
plt.show()
#---------------------------------------------------------------------------
#example 7 Pyplot Scales
from matplotlib.ticker import NullFormatter 

np.random.seed(19981222)

y=np.random.normal(loc=0.5,scale=0.4,size=1000)#从正态(高斯)分布中随机抽取样本。
y=y[(y>0) &(y<1)] #按位与，为什么这么写 
y.sort()
x=np.arange(len(y)) #使用默认值后为arange(0,len(y),1)

plt.figure(1)

    #linear
plt.subplot(221)
plt.plot(x,y)
plt.yscale('linear') #设置y轴的缩放
plt.title('linear')
plt.grid(True)     #轴线，坐标轴打开

    #log
plt.subplot(222)
plt.plot(x,y)
plt.yscale('log')  #没有缩放就是线性
plt.title('log')
plt.grid(True)

    #symmetric log
plt.subplot(223)
plt.plot(x,y-y.mean()) #返回平均值
plt.yscale('symlog',linthreshy=0.01)
plt.title('symlog')
plt.grid(True)

    #logit
plt.subplot(224)
plt.plot(x,y)
plt.yscale('logit')
plt.title('logit')
plt.grid(True)

plt.gca().yaxis.set_minor_formatter(NullFormatter())
plt.subplots_adjust(top=0.92,bottom=0.08,left=0.1,right=0.95,hspace=0.25,                   wspace=0.35)
plt.show()
#---------------------------------------------------------------------------
#6
t=np.arange(0.0,2.0,0.01)
s=np.sin(2*np.pi*t)

plt.plot(t,s)
plt.title(r'$\alpha_i > \beta_i$',fontsize=20) 
plt.text(1,-0.6,r'$\sum_{i=0}^\infty x_i$',fontsize=20)
plt.text(0.6,0.6,r'$\mathcal{A}\mathrm{sin}(2 \omega t)$',fontsize=20)
plt.xlabel('time (s)')
plt.ylabel('volts (mV)')
plt.show()
#---------------------------------------------------------------------------
#5
def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)

t1=np.arange(0.0,5.0,0.1)
t2=np.arange(0.0,5.0,0.02)

plt.figure(1) #几个窗口，这里当然没用
plt.subplot(211) #2*1的块中的块1上作图
plt.plot(t1,f(t1),'bo',t2,f(t2),'k')

plt.subplot(212)
plt.plot(t2,np.cos(2*np.pi*t2),'r-')
plt.show()
#---------------------------------------------------------------------------
#4
ax =plt.subplot(121) #分成几块作图，这里好像没用,现在有了
t1=np.arange(0.0,1.0,0.01)
for n in [1,2,3,4]:
    plt.plot(t1,t1**n,label="n=%d"%(n,))

leg=plt.legend(loc='best',ncol=2,mode="expand",shadow=True,fancybox=True) #图例标注
leg.get_frame().set_alpha(0.5)
plt.show()
#---------------------------------------------------------------------------
#3
t=np.arange(0.,5.,0.2) #均匀间隔值的数组
plt.plot(t,t,'r--',t,t**2,'bs',t,t**3,'g^')
plt.show()
#---------------------------------------------------------------------------
#example 2
plt.plot([1,2,3,4],[1,4,9,16],'ro')
plt.axis([0,6,0,20])
plt.show()
#---------------------------------------------------------------------------
#example 1
plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()


