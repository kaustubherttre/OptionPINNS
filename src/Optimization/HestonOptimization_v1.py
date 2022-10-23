from random import random
import sys
sys.path.insert(0, '../../src/Vanilla/')
from HestonSA import HestonSA
import matplotlib.pyplot as plt
from numpy import gradient as grad
import numpy as np
import pandas as pd
from scipy.optimize import minimize, broyden2, broyden1
from scipy import optimize
from time import time
from julia import Main
Main.include('../Vanilla/HestonSA.jl')


class HestonOptimization:
    def __init__(self, data):
        self.data = data
        def error_function(x):
            error = []
            kappa, theta, lamda, rho, V_0 = [param for param in x]
            OptimParams = {"kappa": kappa, "theta": theta, "lamda": lamda, "rho": rho, "V_0": V_0  }
            for index, rows in data.iterrows():
                ModelParams = {"S":data.loc[ index,"S"].item(), "K": data.loc[index,"K"].item(), "T": data.loc[index,"T"].item(), "r": data.loc[index,"r"].item(), "time_iters": 10000, "int_iters": 1000}
                heston_price = HestonSA(ModelParams, OptimParams).final_price
                error.append((data.loc[ index, "Price"] - heston_price)**2 /len(data))
                if(len(error) == len(data)):
                    print(np.sum(error))
                    return(np.sum(error))
        params = {
            "kappa":{"x0": 3.0, "lub": [1e-3, 5.0]},
            "theta":{"x0": 0.05, "lub": [1e-3, 1.0]},
            "lamda":{"x0": 0.03, "lub": [1e-2, 1.0]},
            "rho":{"x0": -0.8, "lub": [-1, 0.0]},
            "V_0":{"x0": 0.1, "lub": [1e-3, 0.1]},
        }
        x0 = [param["x0"] for key, param in params.items()]
        print(error_function(x0))
        boundary = [param['lub'] for key, param in params.items()]
        result = minimize(error_function, x0, tol = 1e-2, method = 'SLSQP', options = {'maxiter': 1e3}, bounds = boundary)
        self.res = result

if __name__ == '__main__':
    data = pd.read_csv('../../data/ProcessedData/ClassAdded.csv')
    class_data = data.loc[data['Class'] == 'C11'][:10]
    model = HestonOptimization(class_data)
    print(model.res)


