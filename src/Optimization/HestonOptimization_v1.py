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


class HestonOptimization:
    def __init__(self, data):
        self.data = data
        def error_function(x):
            error = 10
            
            kappa, theta, lamda, rho, V_0 = [param for param in x]
            OptimParams = {"kappa": kappa, "theta": theta, "lamda": lamda, "rho": rho, "V_0": V_0  }
        
            OptimParams = {"kappa": kappa, "theta": theta, "lamda": lamda, "rho": rho, "V_0": V_0  }
            print(OptimParams)
            print(" No Voilation")
            ModelParams = {"S":data["S"], "K": data["K"], "T": data["T"], "r": data["r"], "time_iters": 10000, "int_iters": 1000}
            error = np.sum((data["Price"] - HestonSA(ModelParams, OptimParams).final_price)**2/ len(data["Price"]))
            print(error)
            return error
        params = {
            "kappa":{"x0": 3, "lb": [1e-3, 5]},
            "theta":{"x0": 0.05, "lb": [1e-3, 1]},
            "lamda":{"x0": 0.03, "lb": [1e-2, 1]},
            "rho":{"x0": -0.8, "lb": [-1, 0]},
            "V_0":{"x0": 0.1, "lb": [1e-3, 0.1]},
        }
        x0 = [param["x0"] for key, param in params.items()]
        print(error_function(x0))
        boundary = [param['lb'] for key, param in params.items()]
        result = minimize(error_function, x0, tol = 1e-2, method = 'SLSQP', options = {'maxiter': 1e3}, bounds = boundary)
        self.res = result.x

if __name__ == '__main__':
    data = pd.read_csv('../../data/ProcessedData/ClassAdded.csv')
    class_data = data.loc[data['Class'] == 'C14']
    model = HestonOptimization(class_data)
    print(model.res)


