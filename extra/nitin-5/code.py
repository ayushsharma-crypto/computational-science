import math

dataFile = open('./starting_config_300k.pdb')
data = dataFile.readlines()

coordinates = []
for i in range(0,3*(len(data)//3),3):
    data[i] = data[i].split()
    Ocoordinate = {'x':float(data[i][5]),'y':float(data[i][6]),'z':float(data[i][7])}
    data[i+1] = data[i+1].split()
    H1coordinate = {'x':float(data[i+1][5]),'y':float(data[i+1][6]),'z':float(data[i+1][7])}
    data[i+2] = data[i+2].split()
    H2coordinate = {'x':float(data[i+2][5]),'y':float(data[i+2][6]),'z':float(data[i+2][7])}
    coordinates.append({'O':Ocoordinate,'H1':H1coordinate,'H2':H2coordinate})

numberOfMol = len(coordinates)
charges = {
    'H1':0.417000,
    'H2':0.417000,
    'O':-0.834000
}
Kc = 332.1
A = 582000
B = 595.0
totalPotential = 0.0
totalVanderwaal = 0.0
Lx=23.623
Ly=22.406
Lz=27.1759

def getTwoMolPotential(i,j):
    potential = 0.0
    
    for molecule1,position1 in coordinates[i].items():
        for molecule2,position2 in coordinates[j].items():
            Rsquare = (abs(position1['x']-position2['x']) - Lx*(round((abs(position1['x']-position2['x']))/Lx)))**2
            Rsquare+= (abs(position1['y']-position2['y']) - Ly*(round((abs(position1['y']-position2['y']))/Ly)))**2
            Rsquare+= (abs(position1['z']-position2['z']) - Lz*(round((abs(position1['z']-position2['z']))/Lz)))**2
            distance = math.sqrt(Rsquare)
            if molecule1=='O' and molecule2=='O':
                Roo = distance
            potential+=((Kc*charges[molecule1]*charges[molecule2])/distance)
    vanderwaal = ((A/(Roo**12))-(B/(Roo**6)))
    return vanderwaal,potential

for i in range(numberOfMol):
    for j in range(i):
        if i!=j:
            vanderwaal, potential = getTwoMolPotential(i,j)
            totalVanderwaal+=vanderwaal
            totalPotential+=potential
print("electrostatic energy: ",totalPotential)
print("Vanderwaal energy:     ",totalVanderwaal)
print("Total energy:         ",totalVanderwaal+totalPotential)