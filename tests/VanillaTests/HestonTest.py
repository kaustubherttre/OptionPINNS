import sys
sys.path.append('../../src/Vanilla/')
import matplotlib.pyplot as plt
from HestonSA import HestonSA


if __name__ == '__main__':
    a = []
    ModelParams = {"S":95, "K": 100,  "T": 2, "r": 0.03, "time_iters": 10000, "int_iters": 1000}
    
    OptimParams = {"kappa": 0.749131, "theta": 0.459467, "lamda":2.786400, "rho": -0.249205, "V_0": 0.062500}
    Hestonmodel = HestonSA(ModelParams, OptimParams)
    print(Hestonmodel.final_price)
