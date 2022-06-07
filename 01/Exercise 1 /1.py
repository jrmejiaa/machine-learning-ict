import numpy as np
import matplotlib.pyplot as plt



### Exercise 1a
p = 0.5
n = 1000
# Using the binomial function with 1 as first parameter to sample from binomial distribution
Bernoulli_samples = np.random.binomial(1,p,n)
cum_sum = np.zeros((n,1))
avg = np.zeros((n,1))

for k in range(n-1):
    cum_sum[k+1] = cum_sum[k] + Bernoulli_samples[k+1]
    avg[k+1] = cum_sum[k+1]/(k+1)

plt.plot(np.linspace(1,n,n),avg)
plt.xlabel("iterations")
plt.ylabel('average')
plt.show()

### Exercise 1b
n = 1000
m = 10
avg = np.zeros((n,m))
for k in range(n):
    for l in range(m):
        Bernoulli_samples = np.random.binomial(1,p,k+1)
        avg[k,l] = np.mean(Bernoulli_samples)

plt.plot(np.linspace(1,n,n),avg,'.',markersize=2.5)
plt.ylabel('iterations')
plt.show()
#Plotting only every 10th value, so the plot is more readable
plt.errorbar(np.linspace(1,n,n)[0:n:10],np.mean(avg,1)[0:n:10],np.std(avg,1)[0:n:10])
plt.ylabel("iterations")
plt.show()
