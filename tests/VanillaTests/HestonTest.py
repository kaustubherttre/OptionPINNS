import sys
sys.path.append('../../src/Vanilla/')
import matplotlib.pyplot as plt
from HestonSA import HestonSA


if __name__ == '__main__':
    a = []
    for i in range(1,1000, 1):
        ModelParams = {"S":95, "K": 100,  "T": 2, "r": i/10000, "time_iters": 1000, "int_iters": 100}
    
        OptimParams = {"kappa": 0.749131, "theta": 0.459467, "lamda":2.786400, "rho": -0.249205, "V_0": 0.062500}
        Hestonmodel = HestonSA(ModelParams, OptimParams)
        a.append(Hestonmodel.final_price)
        print(i)
    #print(Hestonmodel.final_price)
    plt.plot(a)
    plt.show()
