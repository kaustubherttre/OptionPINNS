import numpy as np
import pandas as pd
import datetime as dt
from statistics import mean
from math import sqrt,pi,log
import time
from scipy.interpolate import interp1d
from scipy.stats import norm
from scipy.optimize import brentq
import datetime as dt
from datetime import datetime
import sys
sys.path.append(0, '../data/ProcessedData')

#only functional python
# doing this on a notebook
def call_payoff(S , K):
    return np.maximum(S-K, 0)
def N(x):
    return norm.cdf(x)

def bs_C_value(S,K,r,t,v):
    d1 = (1.0/(v * np.sqrt(t))) * (np.log(S/K) + (r + 0.5 * v**2.0) * t)
    d2 = d1 - (v * np.sqrt(t))
    return N(d1) * S - N(d2) * K * np.exp(-r * t)

def bs_P_value(S,K,r,t,v):
    d1 = (1.0/(v * np.sqrt(t))) * (np.log(S/K) + (r + 0.5 * v**2.0) * t)
    d2 = d1 - (v * np.sqrt(t))
    return  N(-d2) * K * np.exp(-r * t) - N(-d1) * S 

def call_iv_char(S,K,r,t,v,call_price):
    return call_price - bs_C_value(S,K,r,t,v)

def put_iv_char(S,K,r,t,v,put_price):
    return put_price - bs_P_value(S,K,r,t,v)

def C_iv(S,K,r,t,call_price, a = -2.0, b = 2.0, tol = 1e-6):
    S_1 = S
    K_1 = K
    r_1 = r
    t_1 = t
    call_price_1 = call_price

    def fun(v):
        return call_iv_char(S_1,K_1,r_1,t_1,v,call_price_1)
    try:
        res = brentq(fun, a = a, b = b, xtol = tol)
        return np.nan if res <=1.0e-6 else res
    except ValueError:
        return np.nan
def P_iv(S,K,r,t,put_price, a = -2.0, b = 2.0, tol = 1e-6):
    S_1 = S
    K_1 = K
    r_1 = r
    t_1 = t
    put_price_1 = put_price

    def fun(v):
        return put_iv_char(S_1,K_1,r_1,t_1,v,put_price_1)
    try:
        res = brentq(fun, a = a, b = b, xtol = tol)
        return np.nan if res <=1.0e-6 else res
    except ValueError:
        return np.nan
def getput(x):
    S = x['StockLast']
    K = x['OptionStrike']
    r = x['Risk_free_Rate']
    t = x['Years_to_Expiry']
    mid = x['Mid']
    return P_iv(S, K, r, t, mid)
    
def getting_iv(x):
    option_type = x['OptionType']
    S = x['StockLast']
    K = x['OptionStrike']
    r = x['Risk_free_Rate']
    t = x['Years_to_Expiry']
    mid = x['Mid']
    meth = '{0}_iv'.format(option_type)
    return float(globals().get(meth)(S, K, r, t, mid))
    
    
def func(x):
    return np.exp( -0.5 * x * x)/ (sqrt(2.0 * pi))
def get_c_delta(x):
    S = x['StockLast']
    K = x['OptionStrike']
    r = x['Risk_free_Rate']
    t = x['Years_to_Expiry']
    vol = x['Imp_Vol']
    d1 = (1.0/(vol * np.sqrt(t))) * (np.log(S/K) + (r + 0.5 * vol**2.0) * t)
    return N(d1)
def get_gamma(x):
    S = x['StockLast']
    K = x['OptionStrike']
    r = x['Risk_free_Rate']
    t = x['Years_to_Expiry']
    vol = x['Imp_Vol']
    d1 = (1.0/(vol * np.sqrt(t))) * (np.log(S/K) + (r + 0.5 * vol**2.0) * t) 
    return func(d1) / (S * vol * sqrt(t))
def get_vega(x):
    S = x['StockLast']
    K = x['OptionStrike']
    r = x['Risk_free_Rate']
    t = x['Years_to_Expiry']
    vol = x['Imp_Vol']
    d1 = (1.0/(vol * np.sqrt(t))) * (np.log(S/K) + (r + 0.5 * vol**2.0) * t)
    
    return (S * func(d1) * sqrt(t)) / 100.0
def get_c_rho(x):
    S = x['StockLast']
    K = x['OptionStrike']
    r = x['Risk_free_Rate']
    t = x['Years_to_Expiry']
    vol = x['Imp_Vol']
    d1 = (1.0/(vol * np.sqrt(t))) * (np.log(S/K) + (r + 0.5 * vol**2.0) * t)
    d2 = d1 - (vol * np.sqrt(t))
    rho = K * t * np.exp(-r * t) * N(d2)
    return rho / 100.0
def get_c_theta(x):
    S = x['StockLast']
    K = x['OptionStrike']
    r = x['Risk_free_Rate']
    t = x['Years_to_Expiry']
    vol = x['Imp_Vol']
    d1 = (1.0/(vol * np.sqrt(t))) * (np.log(S/K) + (r + 0.5 * vol**2.0) * t)
    d2 = d1 - (vol * np.sqrt(t))
    theta = -((S * func(d1) * vol) / (2.0 * np.sqrt(t))) + (r * K * np.exp(-r * t) * N(-d2))
    return theta / 365.0
def option_moneyness(x):
    S = x['StockLast']
    K = x['OptionStrike']
    return K/S
def log_options_moneyness(x):
    S = x['StockLast']
    K = x['OptionStrike']
    return log(S/K)
def std_moneyness(x):
    S = x['StockLast']
    d = x['Imp_Vol']
    K = x['OptionStrike']
    t = x['Years_to_Expiry']
    m = log(S/K)/(d* sqrt(t))
    return m
def days_till_exp(x):
    exp = x['ExpirationDate']
    date_str = datetime.strptime(exp,'%Y-%m-%d %H:%M:%S')
    time_of_capture = x['TimeStamp']
    time_of_c = datetime.strptime(time_of_capture,'%Y-%m-%d-%H:%M:%S')
    return (date_str - time_of_c).days + 1
def years_till_exp(x):
    exp = x['ExpirationDate']
    date_str = time.strptime(exp,'%Y-%m-%d %H:%M:%S')
    number_of_seconds = time.mktime(date_str)
    time_of_capture = x['TimeStamp']
    time_of_c = datetime.strptime(time_of_capture,'%Y-%m-%d-%H:%M:%S')
    
    seconds_now = time_of_c.timestamp()
    sec_untill_exp = number_of_seconds - seconds_now
    sec_in_year = 31536000.00
    return max(sec_untill_exp / sec_in_year, 1e-10)
duration = [30, 90, 180, 360, 720, 1080, 1800]
rates = [0.0005, 0.0009, 0.001, 0.0011, 0.00112, 0.0012, 0.0025]
def us_interest_rates_for_a_tBill(x):
    days = x['Days_to_Expiry']
    durations = [i for i in range(30, 1801)]
    inter = interp1d(duration, rates, kind = 'linear')
    interp = inter(durations)
    return round(interp[max(days, 30) - 30], 8)
def getting_mid(x):
    bid = x['Bid']
    ask = x['Ask']
    last = x['Last']
    if ask == 0.0 or bid == 0.0:
        return last
    else:
        return (ask + bid)/ 2.0
#implied volatility 
def option_values(x):
    option_type = x['OptionType']
    S = x['StockLast']
    K = x['OptionStrike']
    r = x['Risk_free_Rate']
    t = x['Years_to_Expiry']
    vol = x['Imp_Vol']
    meth = 'bs_{0}_value'.format(option_type)
    return float(globals().get(meth)(S, K, r, t, vol)) 
def error_of_BS(x):
    mid = x['Mid']
    call = x['Option_Value']
    return mid - call



