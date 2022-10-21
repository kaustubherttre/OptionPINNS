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
    df = CSV.read(string(PATH,FILENAME), DataFrame)
end
getData(PATH,FILENAME)
