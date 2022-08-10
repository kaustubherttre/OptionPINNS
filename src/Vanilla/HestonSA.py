import math 
import scipy.stats as ss 
import numpy as np 

# Defining two dicts here: ModelParams include strike, underlying, time etc. OptimParams includes mean reversion speed, corr coff etc
#Solving this with little bit numerical, using discretization(spell check) for complex integral

# ModelParams = {S, K, T, V_0, N}
# OptimParams = {kappa, theta, lambda, rho}
class HestonSA:
    def __init__(self, ModelParams, OptimParams):
        self.S = ModelParams["S"] # Stock
        self.K = ModelParams["K"] # strike
        self.V_0 = ModelParams["V_0"] #inital volatility
        self.T = ModelParams["T"] #time to maturity (yrs)
        self.r = ModelParams["r"] #risk free rate
        self.time_iters = ModelParams["time_iters"]
        self.asset_iters = ModelParams["asset_iters"]
        self.kappa = OptimParams["kappa"]
        self.theta = OptimParams["theta"]
        self.lamda = OptimParams["lamda"]
        self.rho = OptimParams["rho"]
        self.i = complex(0,1)

        def exponential_terms(self):
            exp_1 = (-2*self.theta*self.kappa)/pow(self.lamda, 2)
            exp_2 = (self.theta*self.kappa*self.T)/pow(self.lamda, 2)
            return exp_1, exp_2
        
        def heston_discrete(self):

            exp1, exp2 = exponential_terms(self)
            return exp1
        self.expo = heston_discrete(self)
    #print(self.kappa)

if __name__ == '__main__':
    ModelParams = {"S":95, "K": 100, "V_0": 0.1, "T": 2, "r": 0.03, "time_iters": 10000, "asset_iters": 1000}
    OptimParams = {"kappa": 1.5768, "theta": 0.0398, "lamda": 0.575, "rho": 0.5711}
    model = HestonSA(ModelParams, OptimParams)
    print(model.expo)
