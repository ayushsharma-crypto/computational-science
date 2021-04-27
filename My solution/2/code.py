import random,math
import matplotlib.pyplot as plt

def plot_graph(x_list,y_list,cx_list,cy_list,x_label,y_label,title):
    '''
    This function will plot the graph
    '''
    czipped_list = zip(cx_list,cy_list)
    csorted_pairs = sorted(czipped_list)

    ctuples = zip(*csorted_pairs)
    cx_list, cy_list = [ list(tuple) for tuple in  ctuples]

    plt.plot(cx_list,cy_list,'b-')

    zipped_list = zip(x_list,y_list)
    sorted_pairs = sorted(zipped_list)

    tuples = zip(*sorted_pairs)
    x_list, y_list = [ list(tuple) for tuple in  tuples]

    plt.plot(x_list,y_list,'r-')

    plt.ylabel(y_label)
    plt.xlabel(x_label)
    plt.title(title)
    plt.legend([
        'Computational Data',
        'Analytical Data'
    ])
    plt.show()


def rand_x_y():
    x=random.uniform(0,1)
    y=random.uniform(0,1)
    return x,y

x_list=[]
y_list=[]
cx_list=[]
cy_list=[]
total_iteration=100000
for j in range(0,total_iteration):
    count=0
    total_coins=random.randrange(1,2000,1)
    for i in range(0,total_coins):  #monte-carlo simulation
        x,y=rand_x_y()
        r=math.sqrt(pow(x,2)+pow(y,2))
        if(r<=1):
            count=count+1
        
    temp_pi=4*(count/total_coins)

    x_list.append(total_coins)
    y_list.append(3.14)
    cx_list.append(total_coins)
    cy_list.append(temp_pi)

plot_graph(x_list,y_list,cx_list,cy_list,'N(Number of stones/pebbles)','Value of Pi','Pi Vs N')