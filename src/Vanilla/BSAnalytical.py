#Analytical solution for BS

import numpy as np
import pandas as pd
from math import *
import scipy.stats as si
import matplotlib.pyplot as plt

class BSAnalytical:
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


        