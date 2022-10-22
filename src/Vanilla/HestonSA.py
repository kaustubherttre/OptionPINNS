from math import *
import scipy.stats as ss
import numpy as np
import matplotlib.pyplot as plt
# Defining two dicts here: ModelParams include strike, underlying, time etc. OptimParams includes mean reversion speed, corr coff etc
#Solving this with little bit numerical, using discretization(spell check) for complex integral

# ModelParams = {S, K, T, N}
# OptimParams = {kappa, theta, lambda, rho, V_0}
# This is the solution the is present in Gatheral
class HestonSA:
    def __init__(self, ModelParams, OptimParams):
        
        self.S = ModelParams["S"] # Stock
        self.K = ModelParams["K"] # strike
        self.T = ModelParams["T"] #time to maturity (yrs)
        self.r = ModelParams["r"] #risk free rate
        self.time_iters = ModelParams["time_iters"]
        self.int_iters = ModelParams["int_iters"]
        self.kappa = OptimParams["kappa"] #mean reverison rate
        self.theta = OptimParams["theta"] #long term variance
        self.lamda = OptimParams["lamda"] # variance of volatility
        self.rho = OptimParams["rho"] # correlation coff
        self.i = complex(0,1)
        self.V_0 = OptimParams["V_0"] #inital volatility
        self.exp_aa = (self.theta*self.kappa*self.T)/(self.lamda ** 2)
        self.exp_bb = (-2*self.theta*self.kappa)/(self.lamda ** 2)
        self.P = 0
        self.du = self.int_iters/self.time_iters

        def heston_price(self):
            price = 0
            for j in range(1,self.time_iters):
                u2 = j * self.du
                u1 = complex(u2, -1)
                d1 = d_var(self.rho, self.lamda, u1, self.i, self.kappa)
                d2 = d_var(self.rho, self.lamda, u2, self.i, self.kappa)
                phi1 = phi_function(self, self.kappa, self.rho, self.lamda, self.i, u1, self.T, self.V_0, self.S, self.r, self.K, d1)
                phi2 = phi_function(self, self.kappa, self.rho, self.lamda, self.i, u2, self.T, self.V_0, self.S, self.r, self.K, d2)
                price += ((phi1 - phi2)/(u2*self.i))*self.du
            return self.K*np.real((self.S/self.K-np.exp(-self.r*self.T))/2+price/np.pi)
        def exponential_terms(self):
            exp_1 = (-2*self.theta*self.kappa)/(self.lamda ** 2)
            exp_2 = (self.theta*self.kappa*self.T)/(self.lamda ** 2)
            return exp_1, exp_2

        def d_var(rho, lamda, u, i, kappa):
            aa = (rho*lamda*u*i) - kappa
            bb = (lamda**2)*(u*i+u**2)
            return  np.sqrt(aa**2 + bb)

        def g_var(kappa, rho, lamda, i, u, d):
            #d = d_var(rho, lamda, u, i, kappa)
            g_num = kappa - rho*lamda*i*u - d
            g_den = kappa - rho*lamda*i*u + d
            return g_num, g_den, g_num/g_den

        def phi_function(self, kappa, rho, lamda, i, u, T, V_0, S, r, K,d):
            exp_1, exp_2 = exponential_terms(self)
            g_num, g_den, g = g_var(kappa, rho, lamda, u, i,d)
            p = np.exp(u*i*(np.log(S/K) + r*T)) *((1 - g*np.exp(-d*T))/(1-g))**exp_1
            phi = p*np.exp(exp_2*g_num + V_0*g_num*(1-np.exp(-d*T))/(1-g*np.exp(-d*T))/lamda**2)
            return phi
        self.final_price = heston_price(self)
        print(self.final_price)
