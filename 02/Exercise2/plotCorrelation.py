import numpy as np
import matplotlib.pyplot as plt

def plotCorrelationCoefficient(X,max_lag):

    Xc = X - np.mean(X,0)

    n_dim = X.shape[1]
    L = X.shape[0]
    x_axis = np.linspace(0,max_lag-1,max_lag)
    r = np.zeros((max_lag,n_dim))

    norm = (Xc**2).sum(0)/L
    for k in range(max_lag):
        r[k,:] = (Xc[:-k-1] * Xc[k+1:]).sum(0)/((L-k)*norm)

    return r