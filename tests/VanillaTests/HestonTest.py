import sys
sys.path.append('../../src/Vanilla/')
import matplotlib.pyplot as plt
from HestonSA import HestonSA


if __name__ == '__main__':
    a = []
    ModelParams = {"S":95, "K": 100, "V_0": 0.25, "T": 2, "r": 0.03, "time_iters": 10000, "int_iters": 1000}
    for i in range(10000,1,-1):
        OptimParams = {"kappa": 1.5768, "theta": i/100000, "lamda": 0.575, "rho": -0.5711}
        Hestonmodel = HestonSA(ModelParams, OptimParams)
        a.append(Hestonmodel.final_price)
        print(i)
    plt.plot(a)
    plt.show()


