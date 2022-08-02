from math import *
import numpy as np
import pandas as pd

class BSNumerical:
    def __init__(self, Smin, Smax, K, T, r, sigma):
        N = 160
        self.Smin = 0
        self.Smax = 100
        self.K = 10
        self.T = 1
        self.r = 0.2
        self.sigma = 0.25
        self.N = N #number of shares
        self.M = 1600 #time points
        self.dt = (self.T/self.M)
        self.dS = (self.Smin + self.Smax)/self.N
        self.V = [[0 for i in range(self.N)] for i in range(self.M)]
        def define_initial_conditions(self, Smin, K, N, V, dS):
            for i in range(1,N):
                V[1][i] =  max(i*dS - K, 0)
            return V
        self.iniV = define_initial_conditions(self, Smin, K, N, V, dS)


if __name__ == '__main__':
    model = BSNumerical(0,100,10,1,0.2,0.5)
    print(model.iniV)


