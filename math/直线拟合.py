import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
import pandas as pd

from sklearn.metrics import r2_score
 
#直线方程函数
def f_1(x, A, B):
    return A*x + B


def plot_test():
 
    plt.figure()
 
    #拟合点
    # x0 = np.array([34.70,36.10,37.61,39.20,40.69,42.15,43.70,45.17])
    # y0 = np.array([17.70,17.80,17.90,18.00,18.10,18.20,18.30,18.40])
    x0 = np.array([42,43,44,45,46,47,50])
    y0 = np.array([4.25,4.34,4.43,4.54,4.64,4.74,5.03])
 
    #绘制散点
    #plt.scatter(x0[:], y0[:], 25, "red",label='data')
    
    plt.plot(x0,y0,'o',color='red',markersize=4,label='data')

    
 
    #直线拟合与绘制
    res=optimize.curve_fit(f_1, x0, y0)
    print(res)
    A1, B1 = res[0]
    
    x1 = np.arange(41, 51, 0.01)
    y1 = A1*x1 + B1
    plt.plot(x1, y1, "blue",label="fitting model")
    #r2
    y_pred=A1*x0+B1
    s1=pd.Series(y0)
    s2=pd.Series(y_pred)
    r=s1.corr(s2)
 

    plt.legend(loc='lower right')
    plt.text(42,5,"slope:     "+str(round(A1,6)),fontsize=13)
    plt.text(42,4.9,"intercept:"+str(round(B1,6)),fontsize=13)
    plt.text(42,4.8,'r:        '+str(round(r,7)),fontsize=13)
    plt.xlabel('t')
    plt.ylabel('U_t')
 
    plt.show()
 
    return


plot_test()