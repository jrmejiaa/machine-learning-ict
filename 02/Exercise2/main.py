import numpy as np
import matplotlib.pyplot as plt
from metropolis_hastings import metropolis_hastings
from plotCorrelation import plotCorrelationCoefficient

#1a)
def rosenbrock(x):
    """
    Unnormalized version of Rosenbrock function

    """
    return np.exp(-(100 * (x[1] - x[0]**2)**2 + (1-x[0])**2)/20)

L = 100000
sigma = 0.5
x0 = np.array([0,10])

cov = sigma**2 * np.eye(2)

X,acceptance_ratio = metropolis_hastings(rosenbrock,x0,L,cov)

fig, ax = plt.subplots()

#i) Plot the 2d sequence
ax.plot(X[:,0],X[:,1])
ax.set_xlabel('x1')
ax.set_ylabel('x2')
plt.show()

#ii) plot the trace for each dimension
fig , axs= plt.subplots(2)
axs[0].plot(np.linspace(0,L-1,L),X[:,0])
axs[0].set_ylabel('x1')
axs[1].plot(np.linspace(0,L-1,L),X[:,1])
axs[1].set_ylabel('x2')
axs[1].set_xlabel('iterations')
plt.show()

# iii) Plot the acceptance rate vs sigma
sigma_min = 0
sigma_delta = 0.05
sigma_n = np.linspace(1,20,20)

sigma_ar = sigma_min + sigma_delta * sigma_n

acceptance_ratios = np.zeros_like(sigma_ar)

for i in range(len(sigma_ar)):
    sigma = sigma_ar[i]
    cov = sigma**2 * np.eye(2)
    X,acceptance_ratios[i] = metropolis_hastings(rosenbrock,x0,L,cov)

fig,ax = plt.subplots()
plt.plot(sigma_ar,acceptance_ratios,'-')
ax.set_xlabel("sigma")
ax.set_ylabel('acceptance ratio')
plt.show()
print("test")


#1b)
sigma_ar = [0.1, 0.5 , 1.0]

for i in range(len(sigma_ar)):
    sigma = sigma_ar[i]
    cov = sigma**2 * np.eye(2)
    X2, acceptance_ratio = metropolis_hastings(rosenbrock,x0,L,cov)
    r = plotCorrelationCoefficient(X2,2000)
    fig,axs = plt.subplots(2)
    axs[0].plot(np.linspace(1,2000,2000),r[:,0])
    axs[1].plot(np.linspace(1, 2000, 2000), r[:, 1])
    plt.show()

r = plotCorrelationCoefficient(X[int(L/2):],2000)
fig, axs = plt.subplots(2)
axs[0].plot(np.linspace(1, 2000, 2000), r[:, 0])
axs[1].plot(np.linspace(1, 2000, 2000), r[:, 1])
plt.show()
