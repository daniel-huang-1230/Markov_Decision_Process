import numpy as np
#function that returns the max of the four iput arguments
def max_of_four(a,b,c,d):
    list=[a,b,c,d]
    max=np.max(list)
    return max

#the algorithm that computes the maximum state-value functions
def value_iteration(V,R,action_west, action_north,
                    action_east, action_south,r):
    for s in xrange(len(V)):     #for all states s
        #while(1):
        for k in range(1500):
            V_k=V[s]

            a_west=0
            for i in xrange(len(action_west)):
                if(action_west[i][0]==s+1):
                    a_west=a_west+action_west[i][2]*V[int(action_west[i][1])-1]



            a_north=0
            for i in xrange(len(action_north)):
                if(action_north[i][0]==s+1):
                    a_north=a_north+action_north[i][2]*V[int(action_north[i][1])-1]

            a_east=0
            for i in xrange(len(action_east)):
                if(action_east[i][0]==s+1):
                    a_east=a_east+action_east[i][2]*V[int(action_east[i][1])-1]

            a_south=0
            for i in xrange(len(action_south)):
                if(action_south[i][0]==s+1):
                    a_south=a_south+action_south[i][2]*V[int(action_south[i][1])-1]

            V_kplus1=R[s]+r*max_of_four(a_west,a_north,a_east,a_south)

            V[s]=V_kplus1  #update the state value

            #check for convergence
            if V_kplus1-V_k<0.00001:


                break;  #break out of while loop

    return
#pre-process the data from files
action_west=np.genfromtxt("prob_a1.txt")
action_north=(np.genfromtxt("prob_a2.txt"))
action_east=(np.genfromtxt("prob_a3.txt"))
action_south=(np.genfromtxt("prob_a4.txt"))
R=np.genfromtxt("rewards.txt")


V=[0]*81   #initialize a list to store all state-values and set them to zeros at first
r = 0.9925 #discount factor


value_iteration(V, R, action_west, action_north, action_east, action_south, r)

for s in xrange(len(V)):
    if V[s]!=0:
        print(s+1,V[s])

