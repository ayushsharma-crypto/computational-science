import matplotlib.pyplot as plt
import numpy as np


# x = [0, 0, 0, 0, 0]
# p = [1, 2, 3, 4, 5]
# k = 1/10
# m = 2

# x_axis = np.empty((len(x), 1000))
# p_axis = np.empty((len(p), 1000))
# # Analytical Code
# for i in range(len(x)):
#     for j in range(1000):
#         x_axis[i, j] = x[i]
#         p_axis[i, j] = p[i]
#         x[i] = x[i] + p[i]/m*0.1
#         p[i] = p[i] - k*x[i]*0.1

# plt.figure(figsize=(20, 10))
# for i in range(len(x)):
#     H = 1/2*(k*x[i]**2+p[i]**2/m)
#     plt.plot(x_axis[i], p_axis[i], label = f"H={H}")

# plt.xlabel("x")
# plt.ylabel("momentum")

# plt.legend()

# plt.show()

# plt.figure(figsize=(20, 10))
# for i in range(len(x)):
#     plt.plot(x_axis[i]**2)

# plt.xlabel("Time")
# plt.ylabel("Mean square")
# plt.show()


m = 2
K = 1/10
x = [ 1, 0, 2, -1, 0, 0]
P = [ 1, 2, 0, 4, 5, 6]

dt = 0.1
iteration = 1000
x_time = np.zeros((len(x), iteration))
P_time = np.zeros((len(P), iteration))

for i in range(len(x)):
    for j in range(iteration):
        x_time[i][j] = x[i]
        P_time[i][j] = P[i]
        x[i] = x[i] + P[i]/m*0.1
        P[i] = P[i] - K*x[i]*0.1
    H = 0.5*(K*x[i]**2+P[i]**2/m)
    plt.plot(x_time[i], P_time[i], label = "H is " + str(H))


plt.xlabel("x (x-axis)")
plt.ylabel("P (y-axis)")

plt.legend()
plt.title("P vs X for m = 2 and K = 0.5")
plt.show()

for i in x_time:
    plt.plot(i**2)
plt.xlabel("Time")
plt.ylabel("MSD")

plt.show()
