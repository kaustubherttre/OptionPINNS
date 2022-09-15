from HestonSA import HestonSA
import pandas as pd
import sys
import matplotlib.pyplot as plt


def getParams(data):
    t = data[['Mid','OptionStrike','StockLast','Years_to_Expiry','Risk_free_Rate']]
    t = t.rename(columns = {'Mid': 'Price', 'OptionStrike' : 'K', 'StockLast': 'S', 'Years_to_Expiry': 'T', 'Risk_free_Rate': 'r'  })
    return t


def applyHeston(data):
    a = []
    b = []
    
    for index, row in data.iterrows():
         ModelParams = {"S": row["S"], "K": row["K"],  "T": row["T"], "r": row["r"], "time_iters": 1000, "int_iters": 100}
         OptimParams = {"kappa": 0.749131, "theta": 0.459467, "lamda":2.786400, "rho": -0.249205, "V_0": 0.062500}
         Hestonmodel = HestonSA(ModelParams, OptimParams)
         a.append(Hestonmodel.final_price)
         b.append(row["Price"])
         print(index)

        #  data["HestonPrices"] = Hestonmodel.final_price
    return a,b



if __name__ == '__main__':
    data = pd.read_csv('../../data/ProcessedData/ProcessedData.csv')
    twoRowData = data
    error = []
    data_ = getParams(twoRowData)
    heston_data_ = data_.sample(frac =1)
    hestonPrice, OptionPrice = applyHeston(heston_data_)
    plt.plot(hestonPrice, label = "hestonPrice")
    plt.plot( OptionPrice, label = "OptionPrice" )
    for i in range(len(hestonPrice)):
        error.append(OptionPrice[i] - hestonPrice[i])
        print(i)
    plt.plot(error, label = "Error")
    plt.legend()
    plt.show()
