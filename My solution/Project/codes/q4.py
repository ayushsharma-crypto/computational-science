import numpy as np
from multiprocessing import Pool, Manager
import functools
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


class Hessian:
    
    def __init__(self,configuration, disp_size = 0.005):
        self.mol = configuration
        self.h = disp_size
        self.N = len(configuration.config)
        self.energy = {}
        self.calculate_hessian()
    
    def find_E(self, i, j, hi, hj):
        """
        :params i,j: indices of atoms 1,2
        :params hi,hj: displacements of atoms 1,2 (-1, 0, or 1, corresponds to -h, 0, or h)
        """
        key = "X%dX%d_%d%d" % (i, j, hi, hj)
        return self.energy[key]

    def set_energy(self, key, geom, d=None):
        e = calculate_potential(np.array(geom))
        if d != None:
            d[key] = e
            return
        self.energy[key] = e

    def process(self, i, d):
        h, N, geom = self.h, self.N, self.mol.config
        for j in range(i):
            forward = "X%dX%d_11" % (i, j)
            reverse = "X%dX%d_-1-1" % (i, j)
            geom_copy2 = np.array(self.mol.config)

            geom_copy2[i//3, i % 3] = geom_copy2[i//3, i % 3] + h
            geom_copy2[j//3, j % 3] = geom_copy2[j//3, j % 3] + h

            self.set_energy(forward, geom_copy2, d)

            geom_copy2[i//3, i % 3] = geom_copy2[i//3, i % 3] - 2*h
            geom_copy2[j//3, j % 3] = geom_copy2[j//3, j % 3] - 2*h

            self.set_energy(reverse, geom_copy2, d)

    def run_disps(self):

        h, N, geom = self.h, self.N, self.mol.config
        self.set_energy("X0X0_00", geom)

        ####   Run single displacements   ####
        print("Runing single displacements...\n")
        for i in tqdm(range(3*N)):
            forward = "X%dX0_10" % i
            reverse = "X%dX0_-10" % i
            geom_copy = np.array(self.mol.config)
            geom_copy[i//3, i % 3] = geom_copy[i//3, i % 3]+h
            self.set_energy(forward, geom_copy)

            geom_copy[i//3, i % 3] = geom_copy[i//3, i % 3]-2*h
            self.set_energy(reverse, geom_copy)
        ####   Run double displacements    ######
        print("Running Parallel Processing for double displacements. It will take much time ~30 min...\n")
        mylist = [*range(3*N)]
        pool = Pool()
        D = Manager().dict()  # Create a multiprocessing Pool
        pool.map(functools.partial(self.process, d=D), mylist)
        pool.close()
        pool.join()
        self.energy.update(D)

    def make_Hessian(self):

        self.run_disps()

        h, N = self.h, self.N
        E0 = self.find_E(0, 0, 0, 0)
        self.H = np.zeros((3*self.N, 3*self.N))
        print("Making Hessian...\n")
        for i in tqdm(range(3*N)):
            for i in range(3*N):
                self.H[i, i] = (self.find_E(i, 0, 1, 0) +
                                self.find_E(i, 0, -1, 0)-2*E0)/(h**2)
                for j in range(0, i):
                    self.H[i, j] = (self.find_E(i, j, 1, 1)+self.find_E(i, j, -1, -1)-self.find_E(
                        i, 0, 1, 0)-self.find_E(j, 0, 1, 0)-self.find_E(j, 0, -1, 0)-self.find_E(i, 0, -1, 0)+2*E0)
                    self.H[i, j] /= 2*h**2
                    self.H[j, i] = self.H[i, j]

    def make_eigh(self):
        w, v = np.linalg.eigh(self.H)
        np.savetxt("./outputs/eigen_vectors.dat", v, "%15.7f", " ", "\n")
        np.savetxt("./outputs/eigen_values.dat", w, "%15.7f", " ", "\n")
    
    def calculate_hessian(self):
        self.make_Hessian()
        self.make_eigh()
        np.savetxt("./outputs/hessian.dat", self.H, "%15.7f", " ", "\n")


if __name__=="__main__":
    config_instance = Configuration()
    new_config = np.array(config_instance.read_config("./outputs/final_conf.xyz"))
    config_instance.assign_configuration(new_config)
    config_instance.convert_to_bohr()
    _ = Hessian(config_instance, 0.00001)