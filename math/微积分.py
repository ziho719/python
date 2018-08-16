import numpy as np
from scipy.integrate import quad,dblquad,nquad

print (dblquad(lambda t,x:t**2+x**2,0,1,lambda x:0,lambda x:1-x))

print (dblquad(lambda v,u:u,4/3,2,lambda v:1-v/2,lambda v:v-1))




from scipy import integrate  
def g(x):  
    return np.cos(x)**4-np.cos(x)**3*np.sin(x) 
  
#用integrate下的quad函数可以同时求出积分结果和误差  
res,err=integrate.quad(g,-np.pi/2,np.pi/4) #-1和1表示积分上下限，如果是正无穷用np.inf  
print(res,err)  

res,err=integrate.quad(lambda x:1/(1+np.sin(x)),0,2*np.pi)
print(res,err)  