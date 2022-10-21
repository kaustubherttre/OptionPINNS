

# Defining two dicts here: ModelParams include strike, underlying, time etc. OptimParams includes mean reversion speed, corr coff etc
#Solving this with little bit numerical, using discretization(spell check) for complex integral

# ModelParams = {S, K, T, r}
# OptimParams = {κ, θ, λ, ρ, V_0}
# This is the solution the is present in Gatheral
%%time
function heston_pricing(ModelParams, OptimParams)
    println(ModelParams, OptimParams)
end

