import numpy as np
from matplotlib import pyplot as plt
from configuration import Configuration


hartree2J = 4.359744e-18
amu2kg = 1.660538782e-27
bohr2m = 0.52917720859e-10
c = 2.99792458E8


class Frequency:

    def __init__(self, configuration, hessString):

        self.mol = configuration
        self.hess = hessString
        self.N = len(configuration.config)

        m = []
        for i in range(self.N):
            m += [1/(configuration.atomic_mass)**0.5]*3
        self.MM = np.diag(m)
        self.m = m

        self.frequency_output("./outputs/modes.xyz")


    def get_MWhessian(self):

        H0 = np.matrix([i.split() for i in self.hess.splitlines()], float)
        mwH = np.dot(self.MM, np.dot(H0, self.MM))
        return mwH

    def get_frequencies(self):

        self.e, self.l = np.linalg.eigh(self.get_MWhessian())
        self.Q = np.matrix(self.MM)*np.matrix(self.l)
        freq = []
        conv = np.sqrt(hartree2J/(amu2kg*bohr2m**2)
                       ) / (c*2*np.pi)  # dimensional analysis
        # print(conv)
        for i in self.e:
            if i < 0:
                freq.append((-i)**0.5*conv)
            else:
                freq.append(i**0.5*conv)

        return freq

    def frequency_output(self, output):

        mol = self.mol
        freq = self.get_frequencies()

        t = open(output, "w")
        for i in range(3*self.N):
            t.write("%d\n%s cm^{-1}\n" % (self.N, str(freq[i])))
            for j in range(self.N):
                atom = 'Ar'
                x, y, z = mol.config[j, 0], mol.config[j, 1], mol.config[j, 2]
                dx, dy, dz = self.Q[3*j, i], self.Q[3*j+1, i], self.Q[3*j+2, i]
                t.write("{:s}{:12.7f}{:12.7f}{:12.7f}\n".format(atom, x, y, z))
            t.write("\n")
        t.close()
        a = np.array(freq)
        plt.hist(a, bins=100)
        plt.title("Frequency Histogram")
        # plt.savefig("hist.png")
        plt.show()

        return None



if __name__=="__main__":
    config_instance = Configuration()
    new_config = np.array(config_instance.read_config("./outputs/final_conf.xyz"))
    config_instance.assign_configuration(new_config)
    hessian = open("./outputs/hessian.dat", "r").read()
    _ = Frequency(config_instance, hessian)