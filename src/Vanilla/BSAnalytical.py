#Analytical solution for BS

import numpy as np
import pandas as pd
from math import *
import scipy.stats as si
import matplotlib.pyplot as plt

class BSAnalyticalRange:
    def __init__(self, Smin, Smax, K, r, T, sigma, n_shares):
        self.Smin = Smin
        self.Smax = Smax
        self.K = K
        self.r = r
        self.T = T
        self.sigma = sigma
        self.N = n_shares
        self.dS = (self.Smin + self.Smax)/self.N
        def vanila_call(Smin, Smax, K, r, T, dS, N):
            prices = []
            for i in range(1,N):
                d1 = (np.log( (Smin + i*dS) / K) + (r + 0.5 * sigma ** 2) * (T)) / (sigma * np.sqrt(T))
                d2 = (np.log( (Smin + i*dS) / K) + (r - 0.5 * sigma ** 2) * (T)) / (sigma * np.sqrt((T)))
                call = ((Smin + i*dS) * si.norm.cdf(d1, 0.0, 1.0) - K * np.exp(-r * (T) ) * si.norm.cdf(d2, 0.0, 1.0))
                prices.append(call)
            return prices
            
        self.prices = vanila_call(self.Smin, self.Smax, self.K, self.r, self.T, self.dS, self.N)

class BSAnalyticalAbs:
     def __init__(self, S, K, r, T, sigma):
        self.S = S
        self.K = K
        self.r = r
        self.T = T
        self.sigma = sigma
        def vanila_call(S, K, r, T):
            d1 = (np.log( (S) / K) + (r + 0.5 * sigma ** 2) * (T)) / (sigma * np.sqrt(T))
            d2 = (np.log( (S) / K) + (r - 0.5 * sigma ** 2) * (T)) / (sigma * np.sqrt((T)))
            call = ((S) * si.norm.cdf(d1, 0.0, 1.0) - K * np.exp(-r * (T) ) * si.norm.cdf(d2, 0.0, 1.0))
            return call
        self.prices = vanila_call(self.S, self.K, self.r, self.T)

if __name__ == '__main__':
    model_ana_abs =  BSAnalyticalAbs(95,100,0.03,2, 0.25)
    print(model_ana_abs.prices)

            




        