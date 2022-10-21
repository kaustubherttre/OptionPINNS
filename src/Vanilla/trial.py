import julia 
from julia import Main
from julia.api import Julia
Main.include('HestonSA.jl')

ModelParams = {"S":95, "K": 100,  "T": 2, "r": 0.002, "time_iters": 1000, "int_iters": 100}
OptimParams = {"kappa": 0.749131, "theta": 0.459467, "lamda":2.786400, "rho": -0.249205, "V_0": 0.062500}

print(Main.HestonSA(ModelParams, OptimParams))