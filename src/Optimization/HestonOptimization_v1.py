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


data = pd.read_csv('../../data/ProcessedData/PureOptionData.csv').head(100)

def timer(func):
    def wrapperFunction(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f"Function {func.__name__} took {t2-t1}s")
        return result
    return wrapperFunction


@timer
def error_function(x):
    
    kappa, theta, lamda, rho, V_0 = [param for param in x]
    OptimParams = {"kappa": kappa, "theta": theta, "lamda": lamda, "rho": rho, "V_0": V_0  }
    ModelParams = {"S":data["S"], "K": data["K"], "T": data["T"], "r": data["r"], "time_iters": 10000, "int_iters": 1000}
    error = np.sum((data["Price"] - HestonSA(ModelParams, OptimParams).final_price)**2/ len(data["Price"]))
    return error




if __name__ == '__main__':
    
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

    res = minimize(error_function, x0, tol = 1e-3, method = 'SLSQP', options = {'maxiter': 1e4}, bounds = boundary)
    print(res)
    # kappa, theta, lamda, rho, V_0 

    # t = [ 0.749131, 0.459467, 2.786400, -0.249205, 0.062500]
    # res = minimize(heston_optimization, t, method="CG", options={'disp': True})
    #print(res)
    #print(data)
    # print(heston_optimization(x)) 



