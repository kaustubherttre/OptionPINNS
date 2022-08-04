#Analytical solution for BS

import numpy as np
import pandas as pd
from math import *
import scipy.stats as si
import matplotlib.pyplot as plt
# def euro_vanilla_call(S, K, T, r, sigma):
    
#     #S: spot price
#     #K: strike price
#     #T: time to maturity
#     #r: interest rate
#     #sigma: volatility of underlying asset
    
#     d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
#     d2 = (np.log(S / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    
#     call = (S * si.norm.cdf(d1, 0.0, 1.0) - K * np.exp(-r * T) * si.norm.cdf(d2, 0.0, 1.0))
    
#     return call

class BSAnalytical:
    def __init__(self, Smin, Smax, K, r, T, sigma, n_shares, n_time):
        self.Smin = Smin
        self.Smax = Smax
        self.K = K
        self.r = r
        self.T = T
        self.sigma = sigma
        self.N = n_shares
        self.M = n_time
        self.dt = (self.T/self.M)
        self.dS = (self.Smin + self.Smax)/self.N
        def vanila_call(Smin, Smax, K, r, T, dT, dS, N, M):
            prices = []
            for i in range(1,N):
                for j in range(1,M):
                    d1 = (np.log( (Smin + i*dS) / K) + (r + 0.5 * sigma ** 2) * (j*dT)) / (sigma * np.sqrt(j*dT))
                    d2 = (np.log( (Smin + i*dS) / K) + (r - 0.5 * sigma ** 2) * (j*dT)) / (sigma * np.sqrt((j*dT)))
                    call = ((Smin + i*dS) * si.norm.cdf(d1, 0.0, 1.0) - K * np.exp(-r * (j*dT) ) * si.norm.cdf(d2, 0.0, 1.0))
                prices.append(call)
            return prices
                    
            
        self.d1 = vanila_call(self.Smin, self.Smax, self.K, self.r, self.T, self.dt, self.dS, self.N, self.M)
if __name__ == '__main__':
    model = BSAnalytical(0,20,10,1,0.2,0.25, 100 , 1000)
    print(model.d1)
    plt.plot(model.d1)
    plt.show()

        