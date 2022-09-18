import sys
sys.path.insert(0, '../../src/Vanilla/')
from HestonSA import HestonSA
import matplotlib.pyplot as plt
from numpy import gradient as grad
import numpy as np
import pandas as pd
from scipy.optimize import minimize, broyden2, broyden1
from scipy import optimize

def heston_optimization(x):
    ModelParams = {"S":665.00, "K": 570, "T": 0.116724, "r": 0.000587, "time_iters": 10000, "int_iters": 1000}
    OptimParams = {"kappa": x[0], "theta": x[1], "lamda": x[2], "rho": x[3], "V_0": x[4]  }
    Hestonmodel = HestonSA(ModelParams, OptimParams)
    return 100.200 - Hestonmodel.final_price

def getData():
    return pd.read_csv('../../data/ProcessedData/PureOptionData.csv')


if __name__ == '__main__':
    data = pd.read_csv('../../data/ProcessedData/PureOptionData.csv')
    t = [ 0.749131, 0.459467, 2.786400, -0.249205, 0.062500]
    res = minimize(heston_optimization, t, tol=1e-2, method="SLSQP", options={'maxiter': 1e1})
    #print(res)
    print(res)
    # print(heston_optimization(x)) 



