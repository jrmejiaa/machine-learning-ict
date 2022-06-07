import numpy as np


def metropolis_hastings(func, x0, L, cov):

    n_dim = len(x0)
    X = np.zeros((L,n_dim))

    xi = x0

    acceptances = 0

    mvn_vars = np.random.multivariate_normal(mean = np.zeros(n_dim), cov = cov,size = L)

    uni_vars = np.random.rand(L)

    for i in range(L):
        x_prime = xi + mvn_vars[i]

        r = np.min((1,func(x_prime)/func(xi)))

        if uni_vars[i] < r :
            xi = x_prime
            acceptances += 1
        X[i] = xi

    acceptance_ratio = acceptances / L

    return X, acceptance_ratio

