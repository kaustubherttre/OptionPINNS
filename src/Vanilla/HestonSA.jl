

# Defining two dicts here: ModelParams include strike, underlying, time etc. OptimParams includes mean reversion speed, corr coff etc
#Solving this with little bit numerical, using discretization(spell check) for complex integral

# ModelParams = {S, K, T, r}
# OptimParams = {κ, θ, λ, ρ, V_0}
# This is the solution the is present in Gatheral

function HestonSA(ModelParams, OptimParams)
    S = ModelParams["S"] # Stock
    K = ModelParams["K"] # strike
    T = ModelParams["T"] #time to maturity (yrs)
    r = ModelParams["r"] # rate of return
    time_iters = ModelParams["time_iters"]
    int_iters = ModelParams["int_iters"]
    κ = OptimParams["kappa"] #mean reverison rate
    θ = OptimParams["theta"] #long term variance
    λ = OptimParams["lamda"] # variance of volatility
    ρ = OptimParams["rho"] # correlation coff
    ι = 0+1im
    V_0 = OptimParams["V_0"] #inital volatility
    e_aa = (θ*κ*T)/(λ ^ 2)
    exp_bb = (-2*θ*κ)/(λ ^ 2)
    P = 0
    du = int_iters/time_iters
    exp_1, exp_2 = exponential_terms(θ, κ, λ, T)
    price = 0
    for i = 1:time_iters
        u2 = i * du
        u1 = u2 - 1im
        d1 = d_var(ρ, λ, u1, ι, κ)
        d2 = d_var(ρ, λ, u2, ι, κ)
        ϕ1 = ϕ_function(θ, κ, ρ, λ, ι, u1, T, V_0, S, r, K, d1)
        ϕ2 = ϕ_function(θ, κ, ρ, λ, ι, u2, T, V_0, S, r, K, d2)
        price += ((ϕ1 - ϕ2)/(u2*ι))*du
    end
    P = K*real((S/K-exp(-r*T))/2+price/pi)
    return P
end
function exponential_terms(θ, κ, λ, T)
    exp_1 = (-2*θ*κ)/(λ ^ 2)
    exp_2 = (T*θ*κ)/(λ ^ 2)
    return exp_1, exp_2
end
function d_var(ρ, λ, u, ι, κ)
    aa = (ρ*λ*u*ι) - κ
    bb = (λ^2)*(u*ι+u^2)
    return sqrt(aa ^ 2 + bb)
end
function g_var(κ, ρ, λ, ι, u, d)
    g_num = κ - ρ*λ*ι*u - d
    g_den = κ - ρ*λ*ι*u + d
    return g_num, g_den, g_num/g_den
end
function ϕ_function(θ, κ, ρ, λ, ι, u, T, V_0, S, r, K, d)
    exp_1, exp_2 = exponential_terms(θ, κ, λ, T)
    g_num, g_den, g = g_var(κ, ρ, λ, ι, u, d)
    p = exp(u*ι*(log(S/K) + r*T)) *((1 - g*exp(-d*T))/(1-g))^exp_1
    ϕ = p*exp(exp_2*g_num + V_0*g_num*(1-exp(-d*T))/(1-g*exp(-d*T))/λ^2)
    return ϕ
end


# def g_var(kappa, rho, lamda, i, u, d):
#             #d = d_var(rho, lamda, u, i, kappa)
#             g_num = kappa - rho*lamda*i*u - d
#             g_den = kappa - rho*lamda*i*u + d
#             return g_num, g_den, g_num/g_den
