#Analytical solution for BS

import numpy as np
import pandas as pd
from math import *

class BSAnalytical:
    def __init__(self, Smin, Smax, K, r, T, sigma, n_shares, n_time):
        self.Smin = Smin
        self.Smax = Smax
        self.K = K
        self.r = r
        self.T = T
        self.sigma = sigma
        self.n_shares = n_shares
        self.n_time = n_time
        self.dt = (self.T/self.M)
        self.dS = (self.Smin + self.Smax)/self.N
        
        