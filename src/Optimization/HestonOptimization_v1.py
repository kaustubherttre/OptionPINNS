import sys
sys.path.insert(0, '../../src/Vanilla/')
from HestonSA import HestonSA
import matplotlib.pyplot as plt
from numpy import gradient as grad
import numpy as np


class HestonCaliberation:
    def __init__(self, ModelParams):
        self.ModelParams = ModelParams
        def mapArray(arr):
            return {"kappa": arr[0] , "theta": arr[1], "lamda": arr[2], "rho": arr[3]}
    


if __name__ == '__main__':
    ModelParams = {"S":95, "K": 100, "V_0": 0.25, "T": 2, "r": 0.03, "time_iters": 10000, "int_iters": 1000}
    model = HestonCaliberation(ModelParams)
    print(model.array)




# class HestonCaliberation():
#     def __init__(self, OptimParams, ModelParams):

#         ModelParams = {"S":95, "K": 100, "V_0": 0.25, "T": 2, "r": 0.03, "time_iters": 10000, "int_iters": 1000}
#         for i in range(10000,1,-1):
#             OptimParams = {"kappa": 1.5768, "theta": i/100000, "lamda": 0.575, "rho": -0.5711}
#             Hestonmodel = HestonSA(ModelParams, OptimParams)
#             a.append(Hestonmodel.final_price)
#             print(i)
#         plt.plot(a)
#         plt.show()