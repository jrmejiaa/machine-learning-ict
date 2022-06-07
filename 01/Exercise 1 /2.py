import numpy as np
import matplotlib.pyplot as plt

## Exercise 2 a
n = 1000
p = 0.3
m = [1000,10000,100000]

for i in m:
    Bernoulli_Successes = np.zeros((i))
    for l in range(i):
        Bernoulli_Successes[l] = np.random.binomial(1,p,n).sum()
    Binomial_Samples = np.random.binomial(n,p,i)

    fig,ax = plt.subplots()
    ax.hist(Bernoulli_Successes,color='b',bins=np.linspace(200,399,200),label='Bernoulli',alpha=0.5,density=True)
    ax.hist(Binomial_Samples,color='r',bins=np.linspace(200,399,200),label='Binomial',alpha=0.5,density= True)
    ax.legend()
    fig.show()

    Bernoulli_hist, bins1 = np.histogram(Bernoulli_Successes,bins=np.linspace(0,n,n+1))
    Binomial_hist, bins2 = np.histogram(Binomial_Samples,bins=np.linspace(0,n,n+1))
    ## Normalize the distributions
    Bernoulli_hist = Bernoulli_hist / i
    Binomial_hist = Binomial_hist/i

    mse = ((Bernoulli_hist-Binomial_hist)**2).mean()
    print("The mean square difference between the histograms for m=",i, "is", "%s" % mse)


#Exercise 2b
n = 1000
m = 10000
p = [0.1,0.01,0.001]

for i in p:
    Binomial_Samples = np.random.binomial(n,i,m)
    Poisson_Samples = np.random.poisson(n*i,m)



    fig,ax = plt.subplots()
    ax.hist(Poisson_Samples,color='b',bins=np.linspace(0,2*n*i+5,int(2*n*i)+6),label='Poisson',alpha=0.5,density=True)
    ax.hist(Binomial_Samples,color='r',bins=np.linspace(0,2*n*i+5,int(2*n*i)+6),label='Binomial',alpha=0.5,density= True)
    ax.legend()
    fig.show()

    Poisson_hist, bins1 = np.histogram(Poisson_Samples,bins=np.linspace(0,n,n+1))
    Binomial_hist, bins2 = np.histogram(Binomial_Samples,bins=np.linspace(0,n,n+1))
    ## Normalize the distributions
    Poisson_hist = Poisson_hist / m
    Binomial_hist = Binomial_hist/m

    mse = ((Poisson_hist-Binomial_hist)**2).mean()
    print("The mean square difference between the histograms for p =",i," is", "%s" % mse)
