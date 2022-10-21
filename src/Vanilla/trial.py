import julia 
from julia import Main
from julia.api import Julia
Main.include('HestonSA.jl')

Main.heston_pricing(1,2)