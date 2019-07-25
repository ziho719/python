import numpy as np
import matplotlib.pyplot as plt


def f_1(x):
    return (3.155-4.939*10**-7*x**2-1.541*10**5*x**-2+2.077*10**10*x**-4)**0.5


def plot_test():
 
    plt.figure()

    x = np.arange(430, 730, 0.1)
    y = f_1(x)

    plt.plot(x, y, "blue")

    x1 = np.array([486.1,589.3,656.3])
    y1=f_1(x1)

    plt.text(600,3.5,"x                     y",fontsize=10)
    for i in range(len(x1)):
        plt.text(600,3.4-0.1*i,str(round(x1[i],6))+"       "+str(round(y1[i],6)),fontsize=10)
   
    plt.plot(x1, y1, 'o',color='red',markersize=4)

    plt.show()

plot_test()