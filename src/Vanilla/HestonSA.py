import math 
import scipy.stats as ss 
import numpy as np 

# Defining two dicts here: ModelParams include strike, underlying, time etc. OptimParams includes mean reversion speed, corr coff etc
#Solving this with little bit numerical, using discretization(spell check) for complex integral

# ModelParams = {S, K, T, V_0, N}
# OptimParams = {kappa, theta, lambda, rho}
class HestonSA:
    def __init__(self, ModelParams, OptimParams):
        self.S = ModelParams["S"]
        self.K = ModelParams["K"]
        self.V_0 = ModelParams["V_0"]
        self.T = ModelParams["T"]
        self.N = ModelParams["N"]
        self.kappa = OptimParams["kappa"]
        self.theta = OptimParams["theta"]
        self.lambda = OptimParams["lambda"]
        self.rho = OptimParams["rho"]

    #print(self.kappa)

if __name__ == '__main__':
    ModelParams = {"kappa" : 2}
    model = HestonSA(0, ModelParams)
    print(model.kappa)
