import numpy as np
import matplotlib.pyplot as plt

D = 3
L = 10

dx = 0.125
dt = 0.001
X = np.arange(-L, L, dx)


N = [5, 50, 500, 5000, 50000]
len_N = len(N)
for i in range(len_N):
    PD = [(0 if i != 0 else 1) for i in X]
    for _ in range(N[i]):
        tempPD = []
        K = (D*dt/(dx*dx))
        for _ in range(len(PD)):
            tempPD.append(0)
        for j in range(1, len(PD) - 1):
            tempPD[j] = PD[j] + K * (PD[j+ 1] + PD[j-1] - 2*PD[j])
        PD = tempPD

    plt.plot(X, PD , label = f"N = {N[i]}")

plt.legend()
plt.show()

#########################################
# Now for 2-Dimension
#########################################


    
def ODE2D(Dx, Dy, L,N = [10, 100, 1000, 10000]):
    dx = 0.125
    dy = 0.125
    dt = 0.001
    X = np.arange(-L, L, dx)
    Y = np.arange(-L, L, dy)
    lenX = len(X)
    lenY = len(Y)
    lenN = len(N)
    PD = np.zeros((lenX, lenY))


    for index in range(lenN):
        
        for x in range(lenX):
            for y in range(lenY):
                if (X[x] == 0 and Y[y] == 0):
                    PD[x][y] = 1
                else:
                    PD[x][y] =  0
        Kx = Dx / (dx*dx)
        Ky = Dy / (dy*dy)
        Kxy = Dx*Dy / ((dx*dx)*(dy*dy))
        s = 1
        e = len(PD)-1
        for u in range(N[index]):
            prob_temp = np.zeros((lenX, lenY))
            for i in range(s,e):
                for j in range(1, len(PD[i])-1):
                    ny = Ky * (PD[i+1][j]+ PD[i-1][j] - 2*PD[i][j] )
                    nx = Kx * (PD[i][j+1]+ PD[i][j-1] - 2*PD[i][j] )
                    nxy = Kxy * ( PD[i-1][j-1] + PD[i+1][j+1] + PD[i-1][j+1] + PD[i+1][j-1] - 4*PD[i][j] )
                    prob_temp[i][j] = PD[i][j] + dt*nx + ny*dt + nxy*(dt**2)
            PD = prob_temp

        plt.xlabel("x co-ordinate")
        plt.ylabel("y co-ordinate")
        # plt.contour(X, Y, PD, antialiased=False)
        plt.imshow(PD, extent = [-L, L, -L, L], cmap="inferno")
        if Dx == Dy:
            plt.title(f"Dx = Dy and Time Step = {N[index]}")
        elif Dx > Dy:
            plt.title(f"Dx > Dy and Time Step = {N[index]}")
        else:
            plt.title(f"Dx < Dy and Time Step = {N[index]}")
        plt.show()



ODE2D(1, 1, 5)
ODE2D(1, 3, 5)
ODE2D(3, 1, 5)