from autograd import grad
import autograd.numpy as np
from tqdm import tqdm
from configuration import Configuration



def pbc(point1, point2):
    L = 18
    mod_length = (point2 - point1) % L # The image in the first cube
    return ((mod_length+L/2)%L)-L/2 # MIC separation vector



def calculate_potential(config):
    total_atoms = 108
    epsilon = 0.238
    sigma = 3.4
    pairs = []
    for i in range(total_atoms):
        for j in range(i+1, total_atoms):
            pairs.append((config[i],config[j]))
    
    potential = 0
    for (p1, p2) in pairs:
        Rij = np.linalg.norm(pbc(p1,p2))
        if Rij!=0:
            val = 4*epsilon
            a = sigma/Rij
            val = val*( a**12 - a**6 )
            potential += val
    return potential

if __name__=="__main__":
    config_instance = Configuration()
    new_config = np.array(config_instance.read_config("./outputs/init_conf.xyz"))
    config_instance.assign_configuration(new_config)
    potential = config_instance.calculate_potential()
    print("Lenard Jones Potential of the Initial configuration = ",potential)

    gradient = grad(calculate_potential)
    weight_history = [new_config]
    cost_history = [calculate_potential(new_config)]

    print("Running Steepest Descend Algorithm to Calculate Minimum Potential Energy...")

    iteration_heuristic = 200
    alpha_heuristic = 0.135
    for i in tqdm(range(iteration_heuristic)):
        new_config -= alpha_heuristic*gradient(new_config)
        weight_history.append(new_config)
        cost_history.append(calculate_potential(new_config))
    
    f = open("./outputs/gradient_descent_log.txt","w+")
    f.write(f"Lenard Jones Potential of the Initial configuration = {potential}\n")
    f.write(f"Lenard Jones Potential of the Final configuration = {np.min(np.array(cost_history))}\n\n")

    f.write(f"Energy Logs after each Iteration till {iteration_heuristic} iterations:\n")
    for i in range(iteration_heuristic+1):
        f.write(f"Iteration = {i} Total Energy = {cost_history[i]}\n")
    f.close()
    

    f = open("./outputs/final_conf.xyz","w+")
    f.write(f"{108}\n")
    f.write(f"\n")
    for line in new_config:
        f.write(f"C {line[0]} {line[1]} {line[2]}\n")
    f.close()