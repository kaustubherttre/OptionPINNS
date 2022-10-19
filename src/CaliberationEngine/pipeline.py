from cgi import parse_multipart
import json
from matplotlib.pyplot import get
import pandas as pd
import numpy as np
import sys
import plotly.express as px
sys.path.insert(0, '../../src/Vanilla/')
from HestonSA import HestonSA

def getParamsFromClass(data):
    json_file_path = 'params.json'
    with open(json_file_path, 'r') as j:
        params_dict = json.loads(j.read())
    for index, row in data.iterrows():
        ModelParams = {"S": row["S"], "K": row["K"],  "T": row["T"], "r": row["r"], "time_iters": 1000, "int_iters": 100}
        data_class = data.loc[index,'Class']
        if data_class in params_dict.keys():
            params = params_dict[data_class]
            OptimParams = {"kappa": params[0], "theta":params[1], "lamda":params[2], "rho": params[3], "V_0": params[4]}
            Hestonmodel = HestonSA(ModelParams, OptimParams)
            data.loc[index, "HestonPrice"] = Hestonmodel.final_price
            data.loc[index, "Error_in_Heston"] = row["Price"] - Hestonmodel.final_price
            print(index)
    return data
    
if __name__ == '__main__':
    data = pd.read_csv('../../data/ProcessedData/ClassAdded_test.csv')
    final_data = getParamsFromClass(data)
    df = final_data[final_data['HestonPrice'].notna()]
    classes = df['Class'].unique()
    error_dict = []
    for c in classes:
        my_df = df.loc[df['Class']==c]
        error = my_df['Error_in_Heston'].sum()/len(my_df['Error_in_Heston'])
        max_error = my_df['Error_in_Heston'].max()
        min_error = my_df['Error_in_Heston'].min()
        error_dict.append({'Class': c, 'Error': error, 'MaxError': max_error, 'MinError': min_error})

    error_df = pd.DataFrame(error_dict).sort_values('Class', axis = 0)
    print(error_df)
    fig = px.bar(error_df, x = 'Class', y = 'Error', color = 'MaxError', barmode="group")
    fig.show()