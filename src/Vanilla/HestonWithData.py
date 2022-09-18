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
         data.loc[index, "HestonPrice"] = Hestonmodel.final_price
         data.loc[index, "Error_in_Heston"] = row["Price"]- Hestonmodel.final_price
         print(index)

    return data

if __name__ == '__main__':
    data = pd.read_csv('../../data/ProcessedData/ProcessedData.csv')
    twoRowData = data[:100]
    error = []
    data_ = getParams(twoRowData)
    heston_data_ = data_
    final_data = applyHeston(heston_data_)
    print(final_data)
    # plt.plot(hestonPrice, label = "hestonPrice")
    # plt.plot( OptionPrice, label = "OptionPrice" )
    # for i in range(len(hestonPrice)):
    #     error.append(OptionPrice[i] - hestonPrice[i])
    #     print(i)
    # print(error)
    # plt.plot(error, label = "Error")
    # plt.legend()
    # plt.show()
