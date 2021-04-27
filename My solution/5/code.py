import math


if __name__=="__main__":
    inputFile = open('./starting_config_300k.pdb')
    filedata = inputFile.readlines()


    cumulativePotential = 0.0
    cumulativeVanderwaal = 0.0
    KC = 332.1
    A = 582000
    B = 595.0

    charges = {
        'O':-0.834000,
        'H1':0.417000,
        'H2':0.417000,
    }


    Lx=23.623
    Ly=22.406
    Lz=27.1759

    coOrdinate = []
    limit = (len(filedata)//3)
    for i in range(0,3*limit,3):
        filedata[i] = filedata[i].split()

        co = filedata[i]
        Ocoordinate = {
            'x':float(co[5]),
            'y':float(co[6]),
            'z':float(co[7])
            }

        filedata[i+1] = filedata[i+1].split()
        co = filedata[i+1]
        H1coordinate = {
            'x':float(co[5]),
            'y':float(co[6]),
            'z':float(co[7])
            }

        filedata[i+2] = filedata[i+2].split()
        co = filedata[i+2]
        H2coordinate = {
            'x':float(co[5]),
            'y':float(co[6]),
            'z':float(co[7])
            }

        coOrdinate.append({
            'O':Ocoordinate,
            'H1':H1coordinate,
            'H2':H2coordinate
            })




def getTwoMolPotential(i,j):
    myPotential = 0.0
    L1 = coOrdinate[i].items()
    L2 = coOrdinate[j].items()
    for molecule1,position1 in L1:
        for molecule2,position2 in L2:

            dx = position1['x'] - position2['x']
            dy = position1['y'] - position2['y']
            dz = position1['z'] - position2['z']

            a = (abs(dx) - Lx*(round((abs(dx))/Lx)))**2
            b = (abs(dy) - Ly*(round((abs(dy))/Ly)))**2
            c = (abs(dz) - Lz*(round((abs(dz))/Lz)))**2
            Rsquare = a + b + c

            dist = math.sqrt(Rsquare)

            myPotential+=((KC*charges[molecule1]*charges[molecule2])/dist)

            if molecule1=='O' and molecule2=='O':
                Roo = dist
            
    return [ ((A/(Roo**12))-(B/(Roo**6))) ,myPotential]

for i in range(len(coOrdinate)):
    for j in range(i):
        if i!=j:
            tup = getTwoMolPotential(i,j)
            [vanderwaal, potential] = tup
            cumulativeVanderwaal+=vanderwaal
            cumulativePotential+=potential


print("Total energy:         ",cumulativeVanderwaal+cumulativePotential)
print("Electrostatic Energy: ",cumulativePotential)
print("Vanderwaal Energy:     ",cumulativeVanderwaal)