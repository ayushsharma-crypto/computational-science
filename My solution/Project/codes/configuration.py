from numpy import random
from numpy.linalg.linalg import norm


class Configuration:

    def __init__(self):
        self.total_atoms = 108
        self.atom = "Argon"
        self.atomic_numer = 18
        self.atomic_mass = 39.948 # amu
        self.units  = "Angstrom"
        self.config = []
        self.L = 18 # Lx = Ly = Lz = 18 Angstrom
        self.epsilon = 0.238 # Kcal/Mol
        self.sigma = 3.4 # Generate RIC with Rij >= 3.4 Angstrom
    
    
    def pbc(self,point1, point2):
        mod_length = (point2 - point1) % self.L # The image in the first cube
        return ((mod_length+self.L/2)%self.L)-self.L/2 # MIC separation vector


    def create_random_configuration(self):
        iterated_times = 0
        while len(self.config) < self.total_atoms:
            random_point = random.rand(3) * self.L

            under_pbc = True
            for point in self.config:
                if norm(self.pbc(random_point,point)) <= self.sigma:
                    under_pbc = False
                    break
            
            if not under_pbc:
                iterated_times += 1
                if iterated_times > 1000000:
                    new_config = [ random_point ]
                    for point in self.config:
                        if (norm(self.pbc(point,random_point)) > self.sigma):
                            # if (norm(point-random_point) > self.sigma):
                            new_config.append(point)
                    self.config = new_config

            else:
                iterated_times = 0
                self.config.append(random_point)
            print(f"Total points = {len(self.config)}")

        
    def read_config(self):
        f2 = open("./outputs/init_conf.xyz", "r")
        raw_points = f2.read()
        points = []
        for line in raw_points.split('\n')[2:]:
            if line=="":
                continue
            atom, x, y, z = line.split()[:4]
            points.append([float(x), float(y), float(z)])
        f2.close()
        return points
        
    def assign_configuration(self,new_config):
        self.config = new_config 
        self.total_atoms = len(new_config)   
    

    def calculate_potential(self):
        print("Total atoms = ",self.total_atoms)
        pairs = []
        for i in range(self.total_atoms):
            for j in range(i+1, self.total_atoms):
                pairs.append((self.config[i],self.config[j]))
        
        potential = 0
        for (p1, p2) in pairs:
            Rij = norm(self.pbc(p1,p2))
            if Rij!=0:
                val = 4*self.epsilon
                a = self.sigma/Rij
                val = val*( a**12 - a**6 )
                potential += val
        return potential