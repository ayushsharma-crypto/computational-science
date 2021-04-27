import numpy as np
import matplotlib.pylab as plt
from tqdm import tqdm 

def calculateEM(N, J, spinArray, temperatureArray, loopIteration):
    energyArray = []
    magnetizationArray = []
    energyArray = np.array(energyArray)
    magnetizationArray = np.array(magnetizationArray)


    for i in tqdm(range(len(temperatureArray))):
        initialState = spinArray.copy()
        magneticMoment = np.sum(initialState) # magnetic moment
        interactionEnergy = 0
        for j in range(N-1):
            interactionEnergy = interactionEnergy + -J*initialState[j]*initialState[j+1]
        
        β = 1/temperatureArray[i]
        E = []
        M = []
        for j in range(loopIteration):
            randomIndex = np.random.randint(0, N)
            randomSpin = initialState[randomIndex]
            dM = -2*randomSpin

            previousIndex = (randomIndex-1)%N
            nextIndex = (randomIndex+1)%N
            dE = 2*J*randomSpin*(initialState[previousIndex]+initialState[nextIndex])
            
            if(np.exp(-β*dE) > np.random.uniform()):
                initialState[randomIndex] *= -1
                interactionEnergy += dE
                magneticMoment += dM
                
            if (j> N/10 ) and not (j%N):
                E.append(interactionEnergy)
                M.append(abs(magneticMoment))

        
        E = np.array(E)
        M = np.array(M)
        energyArray = np.append(energyArray, np.mean(E))
        magnetizationArray = np.append(magnetizationArray, np.mean(M))
    
    return energyArray, magnetizationArray


N = 500 # Number of Lattice Points & Spin
J = 1.2 # Spin interaction constant
spinArray = np.random.choice([1, -1],size=N)
temperatureArray = np.linspace(0.01, 8, 40)
energyArray, magnetizationArray = calculateEM(N, J, spinArray, temperatureArray, 500000)

T = np.linspace(0.01,8,1000)
analyticEnergyArray = -N*J*np.tanh(J/T)


fig,((ax1)) = plt.subplots(nrows = 1,ncols= 1,figsize = (10,10))
fig,((ax2)) = plt.subplots(nrows = 1,ncols= 1,figsize = (10,10))

ax1.set_title("Energy vs Temperature")
ax1.scatter(temperatureArray,energyArray,color = 'r',label = "Computational")
ax1.plot(T,analyticEnergyArray,label = "Theoretical")


ax2.set_title("Magnetization vs Temperature")
ax2.plot(temperatureArray,magnetizationArray/N,label = "Computational")

plt.legend()
plt.show()