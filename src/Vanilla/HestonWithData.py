from HestonSA import HestonSA
import pandas as pd
import sys
import matplotlib.pyplot as plt
import plotly.express as px
from julia import Main



def getParams(data):
    t = data[['Mid','OptionStrike','StockLast','Years_to_Expiry','Risk_free_Rate']]
    t = t.rename(columns = {'Mid': 'Price', 'OptionStrike' : 'K', 'StockLast': 'S', 'Years_to_Expiry': 'T', 'Risk_free_Rate': 'r'  })
    return t


def applyHeston(data):
    a = []
    b = []
    Main.include('HestonSA.jl')
    for index, row in data.iterrows():
         ModelParams = {"S": row["S"], "K": row["K"],  "T": row["T"], "r": row["r"], "time_iters": 1000, "int_iters": 100}
         params = [
        9.92183228e-01,  1.55534823e-01,  1.00000000e-02, -7.96029909e-14,
        1.00000000e-03
    ] #time caliberated

         #OptimParams = {"kappa": params[0], "theta":params[1], "lamda":params[2], "rho": params[3], "V_0": params[4]}
         OptimParams = {'kappa': 1.792843050998499, 'theta': 0.31552779855223334, 'lamda': 0.022022107211539868, 'rho': -0.5553479504516986, 'V_0': 0.0892181302056993}
         #OptimParams = {"kappa": 1.58112203, "theta": 0.518175, "lamda": 1, "rho": -1, "V_0":  0.06621402} #x without sample
         #OptimParams = {"kappa": 2.15843823, "theta": 0.31658342, "lamda": 0.02438772, "rho": -0.5755087, "V_0":  0.1} #with sample
         #OptimParams = {"kappa": 0.08307242, "theta": 0.31297369, "lamda": 0.00954286, "rho": -0.0567487, "V_0":  3.32918947} #jac
         #OptimParams = {"kappa": 2.18046836, "theta": 0.30888159, "lamda": 0.02454651, "rho": -0.58138519, "V_0": 0.09985972} #tail
         #OptimParams = {'kappa': 2.1791549391203597, 'theta': 0.30319371690018126, 'lamda': 0.024562356298730856, 'rho': -0.5810309241351336, 'V_0': 0.09879741471092589}
         #Hestonmodel = HestonSA(ModelParams, OptimParams)
         #final_price = Hestonmodel.final_price
         final_price = Main.HestonSA(ModelParams, OptimParams)
         data.loc[index, "HestonPrice"] = final_price
         data.loc[index, "Error_in_Heston"] = row["Price"] - final_price
         data.loc[index, "Diff"] = row["S"] - row["K"]
         print(index)

    return data

if __name__ == '__main__':
    data = pd.read_csv('../../data/ProcessedData/ClassAdded.csv')[:100]
    twoRowData = data
    final_data = applyHeston(twoRowData)
    print(final_data)
    # print(final_data[["HestonPrice", "S","Moneyness", "K", "Error_in_Heston", "T"]])
    # fig = px.line(final_data, x=final_data.index, y=['HestonPrice','Price','Error_in_Heston'], title='Optimization')
    # fig.show()
    # plt.plot(final_data["HestonPrice"], label = "hestonPrice")
    # plt.plot(final_data["Price"], label = "OptionPrice")
    # plt.plot(final_data["Error_in_Heston"], label = "Error")
    # plt.plot(final_data["Diff"], label = "Diff")
    # plt.plot( OptionPrice, label = "OptionPrice" )
    # for i in range(len(hestonPrice)):
    #     error.append(OptionPrice[i] - hestonPrice[i])
    #     print(i)
    # print(error)
    # plt.plot(error, label = "Error")


