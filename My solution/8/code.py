import matplotlib.pyplot as plt
import numpy as np


initial_N1 =  [20, 20, 20,  10]
initial_N2 =  [5, 5, 5, 3]
initial_r = [1.5, 2.1, 2.5, 1]
initial_α = [0.2, 0.27, 0.8,  0.8]
initial_β = [0.0001, 0.15, 0.8, 0.8]
initial_c = [0.4, 0.5, 0.45,  0.45]
initial_k = [20, 25, 25, 25]
initial_t = [100, 100, 100, 100]
initial_i = [500, 500 ,500, 500]
loops = 4

for i in range(loops):
    
    N1 = initial_N1[i]
    N2 = initial_N2[i]
    myN1 = initial_N1[i]
    myN2 = initial_N2[i]
    r = initial_r[i]
    α = initial_α[i]
    β = initial_β[i]
    c = initial_c[i]
    k = initial_k[i]
    t = initial_t[i]
    i = initial_i[i]

    instances_N1 = []
    instances_N2 = []
    instances_t = np.linspace(0, t, i)
    dt = instances_t[2]-instances_t[1]

    for tm in instances_t:
        instances_N1.append(N1)
        instances_N2.append(N2)

        ## dN = dN/dt * dt 

        dN1 = - α*N1*N2 + r*N1*(1-N1/k)
        dN2 = - c*N2 + β*N1*N2
        dN1 = dN1 * dt
        dN2 = dN2 * dt

        N1 += dN1
        N2 += dN2
    
    
    plt.figure(figsize=(15,16))
    plot_text = f"N1(0): %.2f\n"%(myN1)
    plot_text += f"N2(0): %.2f\n"%(myN2)
    plot_text += f"k: %.2f\n"%(k)
    plot_text += f"r: %.2f\n"%(r)
    plot_text += f"α: %.2f\n"%(α)
    plot_text += f"β: %.2f\n"%(β)
    plot_text += f"c: %.2f"%(c)

    plt.plot(instances_t, instances_N1, color='g')
    plt.plot(instances_t, instances_N2, color='c')

    plt.title("Prey-Predator Model")
    plt.ylabel("Population")
    plt.xlabel("Time Period")
    plt.legend(["Prey", "Predator"])
    plt.text(-25, 5,plot_text, fontsize=12)
    plt.subplots_adjust(left=0.25)
    plt.show()