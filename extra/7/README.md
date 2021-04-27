### ICING MODEL

###### 1. Construct a 1-D numpy array with values +1 and −1(a=np.array([−1,+1]). Then construct Spin_array of size N. 
###### 2. Calculate initial energy of the system given by the equation mentioned in the question
###### 3. Now we start iteration(it should be sufficiently large)
###### 4. In each iteration choose a random integer between 0 to N-1 it can be done using np.random.randint(0,N). and find the value of the spin regarding this index(let say ith spin is selected) which is σμi = Spin_array[i]. Then calculate change in energy.
###### 5. Now if the change in energy is less, accept it. If change in energy is more, accept it with probability e^(-dE/T)
###### 6. Repeat the process till equilibrium is reached.
###### 7. Plot average energy for different temperatures.
###### 8. Magnetization is average of all the spins. Plot magnetization at different temperatures.

### Running the code
```
jupyter notebook main.ipynb 
```