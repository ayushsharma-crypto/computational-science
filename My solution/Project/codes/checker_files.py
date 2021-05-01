import numpy
from numpy.linalg.linalg import norm

def read_config():
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

def check_random_conf_correctness():
    f1 = open("temp.txt", "w")
    config = numpy.array(read_config())
    sigma = 3.4
    for p1 in config:
        for p2 in config:
            [a,b,c]=p1
            [x,y,z]=p2
            if (a==x)and(b==y)and(c==z):
                continue
            if (norm(p1-p2) <= sigma):
                print(f"P1 = {p1} and P2 = {p1}\n", file=f1)
    f1.close()

check_random_conf_correctness()