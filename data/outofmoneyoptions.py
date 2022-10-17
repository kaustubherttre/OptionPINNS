import pandas as pd 
import plotly.express as px
import math
import matplotlib.pyplot as plt
import time
import datetime
import plotly.express as px
import plotly.graph_objects as go
def convert_year_into_days(df):
    for index, row in df.iterrows():
        year_in_sec = row['T'] * 31536000.00
        days = math.ceil(year_in_sec * 1.15741e-5)
        df.loc[index, "Days"] = days
        print(index)
    return df

if __name__ == "__main__":
    # data = pd.read_csv("ProcessedData/PureOptionData.csv")
    # for index, row in data.iterrows():
    #     data.loc[index, "Value"] = max(row["S"] - row["K"], 0)
    #     print(index)
    # pricing_data = data[data["Value"] > 0]

    # pricing_data.to_csv("ValueAddedOptions.csv")

    #remove values from main ds of testing ds
    
    # df = pd.read_csv("ProcessedData/TimeSorted.csv")
    # for index, row in df.iterrows():
    #     df.loc[index, "Moneyness"] = row["S"]/row["K"]
    # df.to_csv("TimeSorted.csv")
    # fig = px.bar(df, x = df.index, y = ['Moneyness'])
    # fig.show()
    # print(df)
    df =  pd.read_csv("ProcessedData/DaysAddedOptions.csv")
    s_df = pd.read_csv("ProcessedData/DaysAddedOptions.csv").sample(1000)
    newdf = pd.concat([df, s_df,]).drop_duplicates(keep=False)
    print(len(s_df), len(df), len(newdf))
    newdf.to_csv('Training_Engine.csv') 
    s_df.to_csv('Testing_Enigne.csv')
    # fig = px.scatter(df, x = df['Days'], y =  df['Moneyness'])
    # fig.add_hline(y=1.1)
    # fig.add_hline(y=1.2)
    # fig.add_hline(y=1.3)
    # fig.show()
    # fig.write_image('../img/EngineCriteria.png')
    



    #print(convert_year_into_days(df))