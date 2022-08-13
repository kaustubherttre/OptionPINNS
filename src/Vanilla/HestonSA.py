from math import *
import scipy.stats as ss 
import numpy as np 
import matplotlib.pyplot as plt
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
        self.int_iters = ModelParams["int_iters"]
        self.kappa = OptimParams["kappa"]
        self.theta = OptimParams["theta"]
        self.lamda = OptimParams["lamda"]
        self.rho = OptimParams["rho"]
        self.i = complex(0,1)

        def exponential_terms(self):
            exp_1 = (-2*self.theta*self.kappa)/pow(self.lamda, 2)
            exp_2 = (self.theta*self.kappa*self.T)/pow(self.lamda, 2)
            return exp_1, exp_2

        def d_var(rho, lamda, u, i, kappa):
            aa = (rho*lamda*u*i - kappa)
            bb = lamda**2*(i*u+u**2)
            return (aa**2 + bb) ** 0.5

        def g_var(kappa, rho, lamda, i, u):
            d = d_var(rho, lamda, u, i, kappa)
            g_num = kappa - rho*lamda*i*u - d
            g_den = kappa - rho*lamda*i*u + d
            return g_num, g_den, g_num/g_den

        def phi_function(kappa, rho, lamda, i, u, T, V_0, S, r):
            exp_1, exp_2 = exponential_terms(self)
            d = d_var(rho, lamda, u, i, kappa)
            g_num, g_den, g = g_var(rho, lamda, u, i, kappa)
            aa_g = (1 - g*np.exp(-d*T))/(1-g)
            aa = np.exp(r*T) * S**(i*u) * (aa_g**exp_1)
            bb_inner_exp = (1 - np.exp(d*T))
            bb = np.exp(exp_2*g_num + ((V_0/lamda**2) *g_den*bb_inner_exp))
            print(bb_inner_exp)
            return aa*bb
        
        def imag_terms(i, u, K):
            return i*u*(K**(i*u))
        def integration_term(self, time_iters, int_iters, r, T, i, K):
            du = int_iters/time_iters
            aa = 0.5 * (self.S - self.K*np.exp(-self.r*self.T))
            price = 0
            for j in range(1, time_iters):
                u1 = complex(-1, du*j)
                u2 = du * j
                phi1 = np.exp(r*T) * phi_function(self.kappa, self.rho, self.lamda, self.i, u1, self.T, self.V_0, self.S, self.r)/imag_terms(i, u2, K)
                phi2 = (K * phi_function(self.kappa, self.rho, self.lamda, self.i, u2, self.T, self.V_0, self.S, self.r))/imag_terms(i, u2, K)
                price += aa+ ((phi1-phi2)*du)/np.pi
                #print(price)
            return np.real(price)

        self.final_price = integration_term(self, self.time_iters, self.int_iters, self.r, self.T, self.i, self.K)

        #self.expo = heston_discrete(self)
    #print(self.kappa)

if __name__ == '__main__':
    ModelParams = {"S":95, "K": 100, "V_0": 0.1, "T": 2, "r": 0.03, "time_iters": 10000, "int_iters": 1000}
    OptimParams = {"kappa": 1.5768, "theta": 0.0398, "lamda": 0.575, "rho": 0.5711}
    model = HestonSA(ModelParams, OptimParams)
    #print(model.phi_func)
    #print(model.d_var(ModelParams["rho"], ModelParams["lamda"],100, complex(0,1), ModelParams["kappa"]))
    a = model.final_price
    print(a)
        
