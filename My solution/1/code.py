    # -----------------------------------------------------------------------
    # |                                                                     |
    # | For plotting different part of the question on graph please         |
    # | uncomment accordingly the last 10 lines of this file as directed    |
    # |                                                                     |
    # -----------------------------------------------------------------------



import random
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


a_list = [-1,1]
a_probability = [0.5, 0.5]
def stop_point(rand_N):
    var = 0
    for i in range(0, rand_N):
        var = var + (random.choices(a_list,a_probability)[0])
    return var



max_stored_factorial=1000
factorial_dict={}
factorial_dict[0]=1
for i in range(1,max_stored_factorial+1):
    factorial_dict[i]=i*factorial_dict[i-1]

def calculate_factorial(fact_N):
    '''
    This function Calculates (fact_N!)
    '''
    if fact_N <= max_stored_factorial:
        return factorial_dict[fact_N]
    
    var=factorial_dict[max_stored_factorial]
    for i in range(max_stored_factorial+1,fact_N+1):
        var=var*i
    
    return var

# Solving the main part of the question i.e. meeting of both drunk men

def p_meeting():
    x_list=[]
    y_list=[]
    cx_list=[]
    cy_list=[]

    # First computing the analytical solution
    # That is probability of two drunk man meet after
    # N steps is [ (2N)! ]/[ ( (2^N).(N!) )^2 ]


    def calculate_probability(given_N):
        '''
        This function calculates  [ (2N)! ]/[ ( (2^N).(N!) )^2 ]
        which is the required probability
        '''
        numerator = calculate_factorial(2*given_N)
        denominator = calculate_factorial(given_N)
        denominator = denominator*pow(2,given_N)

        prob = numerator/denominator
        prob = prob/denominator

        return prob

    # Now Computational calculation

    total_iteration=70
    for i in range(0,total_iteration):
        count = 0
        a_rand_N= random.randrange(1,70,1)
        cx_list.append(a_rand_N)
        for j in range(0,10000):
            SA = stop_point(a_rand_N)
            SB = stop_point(a_rand_N)
            if SA==SB:
                count=count+1
        cy_list.append(count/10000)


        x_list.append(a_rand_N)
        y_list.append(calculate_probability(a_rand_N))

    plot_graph(x_list,y_list,cx_list,cy_list,'N(number of steps)','Probability','Probability of meeting after N steps VS N')




# Now finding probability of a 
# drunk men to be at origin again.

def p_origin():
    x_list=[]
    y_list=[]
    cx_list=[]
    cy_list=[]


    # First computing the analytical solution
    # That is probability of a drunk man to be at origin after
    # N steps is [ (N)! ]/[ (2^N) . ( (N/2)! )^2 ]
    # if N is even otherwise 0

    def calculate_probability_new(given_N):
        '''
        This function calculates   [ (N)! ]/[ (2^N) . ( (N/2)! )^2 ]
        which is the required probability if N is even otherwise 0.
        '''
        if given_N%2 == 1:
            return 0
        numerator = calculate_factorial(given_N)
        denominator = calculate_factorial(given_N/2)
        prob = numerator/denominator
        denominator = denominator*pow(2,given_N)
        prob = prob/denominator
        return prob

    # Now Computational calculation

    total_iteration=200
    for i in range(0,total_iteration):
        count = 0
        a_rand_N= random.randrange(1,70,1)
        cx_list.append(a_rand_N)
        for j in range(0,1000):
            SA = stop_point(a_rand_N)
            if SA==0:
                count=count+1
        cy_list.append(count/1000)


        x_list.append(a_rand_N)
        y_list.append(calculate_probability_new(a_rand_N))

    plot_graph(x_list,y_list,cx_list,cy_list,'N(number of steps)','Probability','Probability of drunk man to be at origin again after N steps VS N')


# Now finding mean displacement of the drunk men

def mean_displacement():
    # Analytically mean displacement should be 0
    x_list=[]
    y_list=[]
    cx_list=[]
    cy_list=[]

    # Computational calculation
    total_iteration=200
    for i in range(0,total_iteration):
        count=0
        a_rand_N= random.randrange(1,100,1)
        x_list.append(a_rand_N)
        y_list.append(0)        # Because analytically mean=0
        cx_list.append(a_rand_N)
        for j in range(0,10000):
            SA=stop_point(a_rand_N)
            count=count+SA
        cy_list.append(count/10000)
    
    plot_graph(x_list,y_list,cx_list,cy_list,'N(number of steps)','Mean Displacement','Mean Displacement of drunk men in N steps VS N')


# Now finding mean square displacement i.e variance of displacement of the drunk men

def meansq_displacement():
    # Analytically mean square displacement should be N for N steps
    x_list=[]
    y_list=[]
    cx_list=[]
    cy_list=[]

    # Computational calculation
    total_iteration=200
    for i in range(0,total_iteration):
        count=0
        a_rand_N= random.randrange(1,100,1)
        x_list.append(a_rand_N)
        y_list.append(a_rand_N)        # Because analytically mean sq. disp. = variance(disp.) = N
        cx_list.append(a_rand_N)
        temp_list=[]
        for j in range(0,10000):
            SA=stop_point(a_rand_N)
            temp_list.append(SA)
            count=count+SA
        
        mean=count/10000
        final=0
        for item in temp_list:
            final=final+pow((item-mean),2)
        
        variance=final/10000
        cy_list.append(variance)
    
    plot_graph(x_list,y_list,cx_list,cy_list,'N(number of steps)','Mean Square Displacement','Mean Square Displacement of drunk men in N steps VS N')


# uncomment line 231 for part1 and run the file using cmd "python code.py" then wait until simulation gets over
# p_meeting()

# uncomment line 234 for part2 and run the file using cmd "python code.py" then wait until simulation gets over
# p_origin()

# uncomment line 237 for part3 and run the file using cmd "python code.py" then wait until simulation gets over
# mean_displacement()

# uncomment line 240 for part4 and run the file using cmd "python code.py" then wait until simulation gets over
# meansq_displacement()