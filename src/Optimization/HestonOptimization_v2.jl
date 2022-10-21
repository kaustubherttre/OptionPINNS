import XLSX
using DataFrames
using CSV
include("../../src/Vanilla/HestonSA.jl")
using .HestonAnalytical

ModelParams = Dict("S" => 95, "K" =>  100,  "T" =>  2, "r" =>  0.002, "time_iters" =>  1000, "int_iters" =>  100)
OptimParams = Dict("kappa" => 0.749131, "theta" => 0.459467, "lamda" =>2.786400, "rho" => -0.249205, "V_0" => 0.062500)
HestonSA(ModelParams, OptimParams)

PATH = "data/ProcessedData/"
FILENAME = "ClassAdded.csv"
function getData(PATH,FILENAME)
    return CSV.read(string(PATH,FILENAME), DataFrame)
end
df = getData(PATH,FILENAME)

function error_function(x)

    κ, θ, λ, ρ, V_0 = [param for param in x]
    OptimParams = Dict("kappa" => κ, "theta" => θ, "lamda" => λ, "rho" => ρ, "V_0" => V_0)
    return df
end
array = [9.92183228e-01,  1.55534823e-01,  1.00000000e-02, -7.96029909e-14, 1.00000000e-03]
error_function(array)
