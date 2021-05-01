import numpy as np
from numpy.linalg.linalg import norm
from configuration import Configuration

def read_config():
    f2 = open("./outputs/molecule.xyz", "r")
    raw_points = f2.read()
    points = []
    for line in raw_points.split('\n')[2:]:
        if line=="":
            continue
        atom, x, y, z = line.split()[:4]
        points.append([float(x), float(y), float(z)])
    f2.close()
    return points


if __name__=="__main__":
    new_config = np.array(read_config())
    config_instance = Configuration()
    config_instance.assign_configuration(new_config)
    total_atoms = len(new_config)

    pairs = []
    for i in range(total_atoms):
        for j in range(i+1, total_atoms):
            pairs.append((new_config[i],new_config[j]))
    

    potential = 0
    for (p1, p2) in pairs:
        Rij = norm(config_instance.pbc(p1,p2))
        if Rij!=0:
            val = 4*config_instance.epsilon
            a = config_instance.sigma/Rij
            val = val*( a**12 - a**6 )
            potential += val
    
    print("Lenard Jones Potential of the random configuration = ",potential)