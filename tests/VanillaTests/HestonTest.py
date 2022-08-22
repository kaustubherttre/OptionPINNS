import sys
sys.path.append('../../src/Vanilla/')

from HestonSA import HestonSA


if __name__ == '__main__':
    ModelParams = {"S":95, "K": 100, "V_0": 0.25, "T": 2, "r": 0.03, "time_iters": 10000, "int_iters": 1000}
    OptimParams = {"kappa": 1.5, "theta": 0.03, "lamda": 0.5, "rho": -0.5}
    Hestonmodel = HestonSA(ModelParams, OptimParams)
    a = Hestonmodel.final_price
    print(a)

