import random
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import f

#  I1 = ∫ 3x^2 dx
#  I2 = ∫ ∫ x^2 y dxdy

f1 = lambda x: 3 * (x ** 2)
f2 = lambda x,y: (x ** 2) * y

def calculateI1(N):
    diff = 1 # Assumed range 0 to 1. So, diff = b-a = 1-0 =1
    summation = 0
    for i in range(N):
        xi = random.uniform(0, 1)
        fi = f1(xi)
        summation += fi*diff
    return summation/N

def calculateI2(N):
    diff = 1 # Assumed range 0 to 1. So, diff = b-a = 1-0 =1
    summation = 0
    for i in range(N):
        xi = random.uniform(0, 1)
        yi = random.uniform(0, 1)
        fi = f2(xi,yi)
        summation += fi*diff
    return summation/N


def IvsN():
    listN = np.array([ i for i in range(1,100)])
    vectorizedI1 = np.vectorize(calculateI1)
    vectorizedI2 = np.vectorize(calculateI2)
    listI1 = vectorizedI1(listN).tolist()
    listI2 = vectorizedI2(listN).tolist()
    listN = listN.tolist()

    plt.figure(figsize=(15,16))
    plt.plot(listN, listI1, color='r')
    plt.plot(listN, listI2, color='b')
    plt.title("I vs N")
    plt.ylabel("Integrated Value")
    plt.xlabel("N(Number of points)")
    plt.legend(["I1", "I2"])
    plt.show()

def IvsT(N,T):
    listN = np.array([ N for _ in range(T)])
    vectorizedI1 = np.vectorize(calculateI1)
    vectorizedI2 = np.vectorize(calculateI2)
    listI1 = vectorizedI1(listN)
    listI2 = vectorizedI2(listN)
    SD1 = np.std(listI1)
    SD2 = np.std(listI2)
    listI1 = listI1.tolist()
    listI2 = listI2.tolist()
    listT = [ i for i in range(1,T+1) ]

    plt.figure(figsize=(15,16))
    plt.plot(listT, listI1, color='r')
    plt.plot(listT, listI2, color='b')
    plt.title(f"I vs T for N={N} & T = {T}")
    plt.ylabel(f"Integrated Value for N = {N}")
    plt.xlabel("T(Number of trial)")
    plt.text(-2.5, 0.5, f"SD1={SD1} , SD2={SD2}", bbox=dict(facecolor='red', alpha=0.5))
    plt.legend(["I1", "I2"])
    plt.show()

    return SD1, SD2

def IvsTvsN(T):
    I1_list = []
    I2_list = []
    for N in range(1, 101):
        listN = np.array([ N for _ in range(T)])
        vectorizedI1 = np.vectorize(calculateI1)
        vectorizedI2 = np.vectorize(calculateI2)
        listI1 = vectorizedI1(listN)
        listI2 = vectorizedI2(listN)
        SDI1 = np.std(listI1)
        SDI2 = np.std(listI2)
        I1_list.append(SDI1)
        I2_list.append(SDI2)
    
    listN = [ i for i in range(1,101)]
    sqrtN = 1/np.sqrt(np.array(listN))
    plt.figure(figsize=(15,16))
    plt.plot(listN, I1_list, color='r')
    plt.plot(listN, I2_list, color='b')
    plt.plot(listN, sqrtN, color='c')
    plt.title("SD of (I vs trials) vs N")
    plt.ylabel(f"Integrated Value for T={T}")
    plt.xlabel("N(Number of points)")
    plt.legend(["I1", "I2", "1/sqrt(N)"])
    plt.show()


IvsN()
SD1, SD2 = IvsT(20, 100)
print(SD1, SD2)
SD1, SD2 = IvsT(1000, 100)
print(SD1, SD2)
IvsTvsN(100)