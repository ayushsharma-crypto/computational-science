import numpy as np
import matplotlib.pyplot as plt
def definite_integral_show(start, end, N):
	"""Approximate the definite integral of f(x)dx between start and end using
	N random points

	Arguments:
	N -- the number of random points to use
	"""

	def f(x,y):
		return np.multiply(x**2,y)

	#First, let's compute fmax. We do that by evaluating f(x) on a grid
	#of points between start and end
	#This assumes that f is generally smooth. If it's not, we're in trouble!
	x = np.arange(start, end, 0.01)
	y = np.arange(start, end, 0.01)
	z = f(x,y)
	f_max = max(z)


	#Now, let's generate the random points. The x's should be between
	#start and end, so we first create points beterrm 0 and (end-start), and 
	#then add start
	#The y's should be between 0 and fmax
	x_rand = start + np.random.random(N)*(end-start)
	y_rand = start + np.random.random(N)*(end-start)
	z_rand = 0 +  np.random.random(N)*f_max


	#Now, let's find the indices of the poitns above and below
	#the curve. That is, for points below the curve, let's find
	#   i s.t. z_rand[i] < f(x_rand,y_rand)[i]
	#And for points above the curve, find
	#   i s.t. z_rand[i] >= f(x_rand,y_rand)[i]
	ind_below = np.where(z_rand < f(x_rand,y_rand))
	ind_above = np.where(z_rand >= f(x_rand,y_rand))

	return f_max*(end-start)*len(ind_below[0])/N


# PART A
num_points = np.array(range(1,1000))
I_values1 = [definite_integral_show(0,1,i) for i in num_points]
I_values1 = np.array(I_values1)

plt.plot(num_points,I_values1)
plt.xlabel("Number of Points (N)")
plt.ylabel("Integral Value")
plt.title("I vs N")

plt.figure()
plt.show()


# PART B
N = 20
num_trails = 100
I_values2 = [definite_integral_show(0,1,N) for i in range(num_trails)]
I_values2 = np.array(I_values2)

plt.plot(np.array(range(num_trails)),I_values2)
plt.xlabel("Number of Trials")
plt.ylabel("Integral Value for N = 20")
plt.title('I vs trials (N=20)')
plt.figure()

print("STANDARD DEVIATION FOR N = %d AND NUM_TRAILS = %d is %f"%(N,num_trails,np.std(I_values2)))
plt.show()


# PART C
N = 1000
num_trails = 100
I_values3 = [definite_integral_show(0,1,N) for i in range(num_trails)]
I_values3 = np.array(I_values3)

plt.plot(np.array(range(num_trails)),I_values3)
plt.xlabel("Number of Trials")
plt.ylabel("Integral Value for N = 1000")
plt.title('I vs trials (N=1000)')

print("STANDARD DEVIATION FOR N = %d AND NUM_TRAILS = %d is %f"%(N,num_trails,np.std(I_values3)))
plt.figure()
plt.show()


# PART D
N = np.array(range(1,1000))
num_trails = 500
std_vs_N = []
for n in N:
	I_values = [definite_integral_show(0,1,n) for i in range(num_trails)]
	I_values = np.array(I_values)
	std_vs_N.append(np.std(I_values))

std_vs_N = np.array(std_vs_N)
plt.plot(N,std_vs_N)
plt.plot(N,1/np.sqrt(N))
plt.xlabel("Number of Points (N)")
plt.legend(('Standard Deviation (500 trials)','1/sqrt(N)'))
plt.title('Comparison of Monte Carlo with 1/sqrt(N)')

plt.figure()
plt.show()
