import sys
sys.path.insert(0, '../src/Vanilla/')
import matplotlib.pyplot as plt
from HestonSA import HestonSA
import numpy as np

def plotting_function(a):
    for x in range(len(a)):
        plt.plot([0,a[x].real],[0,a[x].imag],'ro-',label='python')
    limit=np.max(np.ceil(np.absolute(a))) # set limits for axis
    plt.xlim((-limit,limit))
    plt.ylim((-limit,limit))
    plt.ylabel('Imaginary')
    plt.xlabel('Real')
    plt.show()

if __name__ == '__main__':
    price = []
    ModelParams = {"S":95, "K": 100, "V_0": 0.1, "T": 2, "r": 0.03, "time_iters": 10000, "int_iters": 1000}
    OptimParams = {"kappa": 0.5, "theta": 0.0398, "lamda": 0.25, "rho": 0.5711}
    model = HestonSA(ModelParams, OptimParams)
    # for i in range(1,2000):
    #     OptimParams = {"kappa": i/1000, "theta": 0.0398, "lamda": 0.575, "rho": 0.5711}
    #     model = HestonSA(ModelParams, OptimParams)
    #     print(i)
    # #print(model.d_var(ModelParams["rho"], ModelParams["lamda"],100, complex(0,1), ModelParams["kappa"]))
    #     price.append(model.final_price)
    print(model.final_price)
    plt.plot(model.incP)
    plt.show()

