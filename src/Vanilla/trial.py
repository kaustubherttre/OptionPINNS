import julia 
from julia import Main
from julia.api import Julia
Main.include('HestonSA.jl')
ModelParams = {'S': 636.16, 'K': 595, 'T': 0.028310534, 'r': 0.0005, 'time_iters': 10000, 'int_iters': 1000}
OptimParams = {'kappa': 3.0, 'theta': 0.05, 'lamda': 0.03, 'rho': -0.8, 'V_0': 0.1}

print(Main.HestonAnalytical.HestonSA(ModelParams, OptimParams))