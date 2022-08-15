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
        self.kappa = OptimParams["kappa"] #mean reverison rate
        self.theta = OptimParams["theta"] #long term variance
        self.lamda = OptimParams["lamda"] # variance of volatility
        self.rho = OptimParams["rho"] # correlation coff
        self.i = complex(0,1)

        def exponential_terms(self):
            exp_1 = (-2*self.theta*self.kappa)/(self.lamda ** 2)
            exp_2 = (self.theta*self.kappa*self.T)/(self.lamda ** 2)
            return exp_1, exp_2

        def d_var(rho, lamda, u, i, kappa):
            aa = (rho*lamda*u*i) - kappa 
            
            bb = (lamda**2)*(u*i+u**2)
            #print("Inside dvar", np.sqrt(aa**2 + bb))
            return  np.sqrt(aa**2 + bb)

        def g_var(kappa, rho, lamda, i, u, d):
            #d = d_var(rho, lamda, u, i, kappa)
            g_num = kappa - rho*lamda*i*u - d
            g_den = kappa - rho*lamda*i*u + d
            return g_num, g_den, g_num/g_den

        def phi_function(kappa, rho, lamda, i, u, T, V_0, S, r, K):
            exp_1, exp_2 = exponential_terms(self)
            d = d_var(rho, lamda, u, i, kappa)
            g_num, g_den, g = g_var(kappa, rho, lamda, u, i,d)
            p_1 = (1 - g*np.exp(-d*T))/(1-g)
            p_2 = np.exp(u*i*(np.log(S/K) + r*T))
            phi_pre = p_2 * p_1**exp_1
            phi = phi_pre*np.exp(exp_2*g_num + V_0*g_num*(1-np.exp(-d*T))/(1-g*np.exp(-d*T))/lamda**2)
            return phi

        def integration_term(self, time_iters, int_iters, r, T, i, K):
            du = int_iters/time_iters
            price = 0
            for j in range(1, time_iters):
                u2 = du * j
                u1 = complex(u2, -1)
                phi1 = phi_function(self.kappa, self.rho, self.lamda, self.i, u1, self.T, self.V_0, self.S, self.r, self.K)
                phi2 = phi_function(self.kappa, self.rho, self.lamda, self.i, u2, self.T, self.V_0, self.S, self.r,self.K)
                price += ((phi1 - phi2)/(u2*i))*du
            return K*np.real((self.S/K-np.exp(-r*T))/2+price/np.pi)
        
        def plotting_function(self, time_iters, int_iters):
            du = int_iters/time_iters
            price = []
            phi_1 = []
            phi_2 = []
            for j in range(1, time_iters):
                u2 = du * j
                u1 = complex(u2, -1)
                phi_1.append(phi_function(self.kappa, self.rho, self.lamda, self.i, u1, self.T, self.V_0, self.S, self.r, self.K))
                phi_2.append(phi_function(self.kappa, self.rho, self.lamda, self.i, u2, self.T, self.V_0, self.S, self.r,self.K))
            return phi_1, phi_2
        self.phi_1, self.phi_2 = plotting_function(self, self.time_iters, self.int_iters)



        self.final_price = integration_term(self, self.time_iters, self.int_iters, self.r, self.T, self.i, self.K)


if __name__ == '__main__':
    ModelParams = {"S":95, "K": 100, "V_0": 0.1, "T": 2, "r": 0.03, "time_iters": 10000, "int_iters": 1000}
    OptimParams = {"kappa": 1.5, "theta": 0.03, "lamda": 0.5, "rho": -0.5}
    model = HestonSA(ModelParams, OptimParams)
    a = model.final_price
    print(a)
